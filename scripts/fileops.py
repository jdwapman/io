from altair import Chart
import json    # built-in
import os
import os.path
import pandas
from subprocess import Popen, PIPE, STDOUT, check_output, CalledProcessError, call

from patch import *


def vega_to_output(input_json, fileformat, verbose=False):
    """builds the actual visual plot. """
    executables = {'svg': 'vg2svg',
                   'png': 'vg2png'
                   }
    try:
        exe = executables[fileformat]
    except KeyError as e:
        print e.output
    try:
        # call vg2xxx to turn JSON it into xxx
        p = check_output([exe, input_json, ''])
        return p
    except CalledProcessError as e:
        print e.output


def pipe_vl2vg(json_in, patchFunctions, debugFiles=False):
    """Pipes the vega-lite json through vl2vg to generate the vega json output

        Returns: vega-spec json string"""
    if debugFiles:
        f = open('vl.json', 'w')
        f.write(json.dumps(json_in))
        f.close()
    p = Popen(["vl2vg"], stdout=PIPE, stdin=PIPE, shell=True)
    vg = p.communicate(input=json.dumps(json_in))[0]
    if debugFiles:
        f = open('vg_prepatch.json', 'w')
        f.write(vg)
        f.close()
    if patchFunctions != []:
        # patchFunctions run on dicts, but only convert if we have patch work
        # to do
        vg_dict = json.loads(vg)
        for fn in patchFunctions:
            vg_dict = fn(vg_dict)
        vg = json.dumps(vg_dict)
    if debugFiles:
        f = open('vg_postpatch.json', 'w')
        f.write(vg)
        f.close()
    return vg


def write2tempfile(input):
    """a helper function that creates a temp file and stores the input passed to it in the file """
    import tempfile
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(input)
    temp.close()
    return temp

vlwrapper = """
  <!-- Container for the visualization {title} -->
  <div id="vis_{title}"></div>
  <script>
  var vlSpec = {spec}
  var embedSpec = {{
    mode: "vega-lite",  // Instruct Vega-Embed to use the Vega-Lite compiler
    spec: vlSpec
  }};
  // Embed the visualization in the container with id `vis_{title}`
  vg.embed("#vis_{title}", embedSpec, function(error, result) {{
    // Callback receiving the View instance and parsed Vega spec
    // result.view is the View, which resides under the
    // '#vis_{title}' element
  }});
  </script>
"""


def savefile(chart, name, fileformat, patchFunctions=[patchTwoLegends]):
    if (fileformat == 'html'):
        open(name + '.' + fileformat, 'w').write(
            chart.to_html(local_file=False)
        )
    elif (fileformat == 'json'):
        open(name + '.' + fileformat, 'w').write(
            json.dumps(chart.to_dict(data=True))
        )
    elif ((fileformat == 'svg') or (fileformat == 'png')):
        tmp = write2tempfile(pipe_vl2vg(chart.to_dict(), patchFunctions))
        outfile = vega_to_output(tmp.name, fileformat)
        file = open(name + '.' + fileformat, 'w')
        file.write(outfile)
        file.close()
    elif (fileformat == 'pdf'):
        # check if svg has been generated
        if not os.path.isfile(name + '.svg'):
            savefile(chart, name, 'svg')

        # @TODO:
        # @jakevdp suggests rsvg on node:
        # https://github.com/altair-viz/altair/issues/279#issuecomment-265640244

        osx_svg2pdf = '/Users/jowens/Applications/svg2pdf.app/Contents/MacOS/Application Stub'
        if os.path.isfile(osx_svg2pdf):
            with open(os.devnull, 'w') as devnull:
                # hide stderr
                check_output([osx_svg2pdf, name + '.svg'],
                             stderr=devnull)
                # haven't got Automator to rename the file yet
                os.rename(name + ' copy.pdf', name + '.pdf')

        else:
            with open(os.devnull, 'w') as devnull:
                # hide stderr
                check_output(['inkscape', '--file=%s.svg' % name,
                              '--export-area-drawing', '--without-gui',
                              '--export-pdf=%s.pdf' % name],
                             stderr=devnull)
    elif (fileformat == 'eps'):
        # check if svg has been generated
        if not os.path.isfile(name + '.svg'):
            savefile(chart, name, 'svg')
        with open(os.devnull, 'w') as devnull:
            # hide stderr
            check_output(['inkscape', '--file=%s.svg' % name,
                          '--export-area-drawing', '--without-gui',
                          '--export-eps=%s.eps' % name],
                         stderr=devnull)


def savefile_df(df, name, fileformat):
    if (fileformat == 'html'):
        open(name + '_data.' + fileformat, 'w').write(
            df.to_html()
        )


def wrapChartInMd(chart, anchor=''):
    str = ''
    str += '\n\\htmlonly\n'
    str += chart.to_html(template=vlwrapper, title=anchor)
    str += '\n\\endhtmlonly\n\n'
    return str


def save(chart=Chart(),
         df=pandas.DataFrame(),
         plotname="none",
         formats=[],
         sortby=[],
         columns=[],
         mdtext=""):

    for fileformat in formats:
        if fileformat == 'tablehtml':
            tablefile = plotname + '_table.html'
            outfile = open(tablefile, 'w')
            # http://stackoverflow.com/questions/26277757/pandas-to-html-truncates-string-contents
            pandas.set_option('display.max_colwidth', -1)
            df.sort_values(sortby).to_html(buf=outfile,
                                           columns=columns,
                                           index=False,
                                           escape=False)
            outfile.close()
        if fileformat == 'tablemd':
            tablefile = plotname + '_table_html.md'
            # http://stackoverflow.com/questions/26277757/pandas-to-html-truncates-string-contents
            pandas.set_option('display.max_colwidth', -1)
            with open(tablefile, 'w') as outfile:
                outfile.write('\\htmlonly\n')
                df.sort_values(sortby).to_html(buf=outfile,
                                               columns=columns,
                                               index=False,
                                               escape=False)
                outfile.write('\\endhtmlonly\n')
        elif fileformat == 'md':
            with open(plotname + '.' + fileformat, 'w') as f:
                f.write(mdtext)
        elif fileformat in ['html', 'svg', 'png', 'pdf', 'eps', 'json']:
            savefile(chart, name=plotname, fileformat=fileformat)
