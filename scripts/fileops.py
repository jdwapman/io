from altair import Chart
import json    # built-in
import re
import os
import os.path
import pandas
import time
from io import StringIO
from subprocess import Popen, PIPE, STDOUT, check_output, check_call, CalledProcessError, call

from patch import *


def vega_to_output(input_json, fileformat, verbose=False):
    """builds the actual visual plot. """
    executables = {'svg': 'vg2svg',
                   'png': 'vg2png'
                   }
    try:
        exe = executables[fileformat]
    except KeyError as e:
        print(e.output)
    try:
        # call vg2xxx to turn JSON it into xxx
        p = check_output([exe, input_json, ''])
        return p
    except CalledProcessError as e:
        print(e.output)


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


def savefile(chart, name, fileformat, outputdir,
             patchFunctions=[patchTwoLegends]):
    # assumes outputdir exists
    if fileformat in ['html', 'svg', 'png', 'json']:
        chart.savechart(os.path.join(outputdir, name) + '.' + fileformat)
    elif fileformat in ['pdf', 'eps']:
        # check if svg has been generated
        base = os.path.join(outputdir, name)
        if not os.path.isfile(base + '.svg'):
            savefile(chart, name, 'svg', outputdir, patchFunctions)

        # @TODO:
        # @jakevdp suggests rsvg on node:
        # https://github.com/altair-viz/altair/issues/279#issuecomment-265640244

        osx_svg2pdf = '/Users/jowens/Applications/svg2pdf.app/Contents/MacOS/Application Stub'
        if (fileformat == 'pdf') and os.path.isfile(osx_svg2pdf):
            with open(os.devnull, 'w') as devnull:
                try:
                    # check_call worked where check_output didn't
                    check_call(['open', '-a', 'svg2pdf', base + '.svg'],
                               stderr=devnull)
                except CalledProcessError as e:
                    raise RuntimeError("command '{}' returned with error (code {}): {}".format(
                        e.cmd, e.returncode, e.output))
        else:
            with open(os.devnull, 'w') as devnull:
                # hide stderr
                check_output(['inkscape', '--file=%s.svg' % (base),
                              '--export-area-drawing', '--without-gui',
                              '--export-%s=%s.%s' % (fileformat, base, fileformat)],
                             stderr=devnull)


def savefile_df(df, name, fileformat):
    # obsolete
    if (fileformat == 'html'):
        open(name + '_data.' + fileformat, 'w').write(
            df.to_html()
        )


def getChartHTML(chart, anchor=''):
    chart_html = StringIO()
    chart.save(chart_html, format='html')
    # now save only everything inside <body> ... </body>
    chart_html_only = re.search(r'<body>\s*(.+)\s*</body>',
                                chart_html.getvalue(),
                                re.DOTALL).group(1)
    # fix the div id now
    chart_html_only = re.sub(r'<div id="vis"></div>',
                             r'<div id="%s"></div>' % anchor,
                             chart_html_only)
    chart_html_only = re.sub(r'vegaEmbed\("#vis", spec, opt\);',
                             r'vegaEmbed("#%s", spec, opt);' % anchor,
                             chart_html_only)
    # https://github.com/altair-viz/altair/issues/721#issuecomment-379483336
    # "Or you can do the normal trick of writing to a file-like object using io.StringIO to avoid touching the file system."
    return chart_html_only


def save(chart=Chart(),
         df=pandas.DataFrame(),
         plotname="none",
         outputdir="output",
         formats=[],
         sortby=[],
         columns=[],
         mdtext=""):

    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)
    for fileformat in formats:
        if fileformat in ['tablehtml', 'tablemd']:
            suffix = {'tablehtml': '_table.html',
                      'tablemd': '_table.html.md',
                      }
            tablefile = plotname + suffix[fileformat]
            # http://stackoverflow.com/questions/26277757/pandas-to-html-truncates-string-contents
            pandas.set_option('display.max_colwidth', -1)
            with open(os.path.join(outputdir, tablefile), 'w') as f:
                if (fileformat == 'tablemd'):
                    # Give it a title so it looks nice in "Related Pages"
                    f.write('# Source data for %s\n\n' % plotname)
                df.sort_values(sortby).to_html(buf=f,
                                               columns=columns,
                                               index=False,
                                               escape=False)
                if (fileformat == 'tablemd'):
                    f.write('\n')
        elif fileformat == 'md':
            with open(os.path.join(outputdir, plotname + '.' + fileformat), 'w') as f:
                f.write(mdtext)
        elif fileformat == 'csv':
            with open(os.path.join(outputdir, plotname + '.' + fileformat), 'w') as f:
                f.write(df.to_csv())
        elif fileformat in ['html', 'svg', 'png', 'pdf', 'eps', 'json']:
            savefile(chart, name=plotname, fileformat=fileformat,
                     outputdir=outputdir)
