from altair import Chart
import json    # built-in
import os.path
import pandas
from subprocess import Popen, PIPE, STDOUT, check_output, CalledProcessError, call


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


def pipe_vl2vg(json_in):
    """Pipes the vega-lite json through vl2vg to generate the vega json output

        Returns: vega-spec json string"""
    p = Popen(["vl2vg"], stdout=PIPE, stdin=PIPE, shell=True)
    vg = p.communicate(input=json.dumps(json_in))[0]
    # f = open('log.json','w')
    # f.write(json.dumps(json_in))
    # f.close()
    return vg


def write2tempfile(input):
    """a helper function that creates a temp file and stores the input passed to it in the file """
    import tempfile
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(input)
    temp.close()
    return temp


def savefile(chart, name, fileformat):
    if (fileformat == 'html'):
        open(name + '.' + fileformat, 'w').write(
            chart.to_html(local_file=False)
        )
    elif (fileformat == 'json'):
        open(name + '.' + fileformat, 'w').write(
            json.dumps(chart.to_dict(data=True))
        )
    elif (fileformat == 'md'):
        file = open(name + '.' + fileformat, 'w')
        str = '\\htmlonly\n<div id="%s"></div>\n<script type="text/javascript">\nplotvl("%s",\n       ' % (
            name, name)
        str += json.dumps(chart.to_dict(data=True))
        str += '\n);\n</script>\n\\endhtmlonly\n'
        file.write(str)
        file.close()
    elif ((fileformat == 'svg') or (fileformat == 'png')):
        tmp = write2tempfile(pipe_vl2vg(chart.to_dict()))
        outfile = vega_to_output(tmp.name, fileformat)
        file = open(name + '.' + fileformat, 'w')
        file.write(outfile)
        file.close()
    elif (fileformat == 'pdf'):
        # check if svg has been generated
        if not os.path.isfile(name + '.svg'):
            savefile(chart, name, 'svg')
        with open(os.devnull, 'w') as devnull:
            # hide stderr
            check_output(['inkscape', '--file=%s.svg' % name,
                          '--export-area-drawing', '--without-gui',
                          '--export-pdf=%s.pdf' % name],
                         stderr=devnull)


def savefile_df(df, name, fileformat):
    if (fileformat == 'html'):
        open(name + '_data.' + fileformat, 'w').write(
            df.to_html()
        )


def save(chart=Chart(),
         df=pandas.DataFrame(),
         plotname="none",
         formats=[],
         sortby=[],
         columns=[]):

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
        elif fileformat in ['html', 'svg', 'png', 'pdf']:
            savefile(chart, name=plotname, fileformat=fileformat)
