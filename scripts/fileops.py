from altair import Chart
import json    # built-in
import re
import os
import os.path
import pandas
import time
from io import StringIO
import subprocess

from patch import *

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


def vl2img(vl_json_in, fileformat):
    """Pipes the vega-lite json through vl2vg then vg2xxx to generate an image

        Returns: output of vg2xxx"""

    # TODO would prefer to do this properly with pipes
    # using | and shell=True is safe though given no arguments
    executables = {'svg': 'vg2svg',
                   'png': 'vg2png',
                   'pdf': 'vg2pdf'
                   }
    try:
        exe = executables[fileformat]
    except KeyError as e:
        print(e.output)
    try:
        return subprocess.check_output("vl2vg | %s" % exe, shell=True,
                                       input=vl_json_in)
    except subprocess.CalledProcessError as e:
        print(e.output)


def savefile(chart, name, fileformat, outputdir):
    # assumes outputdir exists
    if fileformat in ['html', 'json']:
        chart.savechart(os.path.join(outputdir, name) + '.' + fileformat)
    elif fileformat in ['png', 'pdf', 'svg']:
        base = os.path.join(outputdir, name)
        # encode is necessary because we want bytes, not a Unicode str
        contents = vl2img(chart.to_json().encode(), fileformat)
        f = open(base + '.' + fileformat, 'wb')
        f.write(contents)
        f.close()
    else:
        print('Unsupported output file format %s\n', fileformat)


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
                             r'<div id="vis_%s"></div>' % anchor,
                             chart_html_only)
    chart_html_only = re.sub(r'vegaEmbed\("#vis", spec, opt\);',
                             r'vegaEmbed("#vis_%s", spec, opt);' % anchor,
                             chart_html_only)
    # these three patches make the vegaEmbed call use the right div id
    chart_html_only = re.sub(r"const el = document.getElementById\('vis'\);",
                             r"const el_%s = document.getElementById('vis_%s');" % (
                                 anchor, anchor),
                             chart_html_only)
    chart_html_only = re.sub(r'vegaEmbed\("#vis", spec, embed_opt\)',
                             r'vegaEmbed("#vis_%s", spec, embed_opt)' % anchor,
                             chart_html_only)
    chart_html_only = re.sub(r'.catch\(error => showError\(el, error\)\)',
                             r'.catch(error => showError(el_%s, error))' % anchor,
                             chart_html_only)

    # don't allow multiple newlines in a row, or else markdown sees it
    # as a paragraph break
    chart_html_only = re.sub(r'\n+', '\n', chart_html_only)
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
                    f.write(
                        '---\ntitle: Source data for %s\nfull_length: true\n---\n\n# Source data for %s\n\n' % (plotname, plotname))
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
