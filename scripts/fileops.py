import json    # built-in
from subprocess import Popen, PIPE, STDOUT, check_output, CalledProcessError


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
    else:
        tmp = write2tempfile(pipe_vl2vg(chart.to_dict()))
        outfile = vega_to_output(tmp.name, fileformat)
        file = open(name + '.' + fileformat, 'w')
        file.write(outfile)
        file.close()
