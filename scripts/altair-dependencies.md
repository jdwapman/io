Python 3

Altair plus all dependencies:
- https://altair-viz.github.io/getting_started/installation.html
- JupyterLab

Pandas

Selenium and headless Chrome: https://altair-viz.github.io/user_guide/saving_charts.html?highlight=selenium

Altair outputs svg only. We want PDF. So we need something to convert svg to pdf. Everything, generally, looks terrible, and the only halfway decent solution I've found on Mac is Gapplin (http://gapplin.wolfrosch.com/). On Mac I wrote a (very simple) Automator script. https://www.evernote.com/shard/s1/sh/0fa85ceb-e3a3-45d7-a12a-a62c564a6f47/065e9f3a34b1e267 This is hardcoded as `osx_svg2pdf` in `savefile` in `fileops.py`.

Without PDF conversion installed, don't use `pdf` in `formats` in any `save` call.

Without Selenium/headless-Chrome installed, don't use `svg` or `png` or `pdf` in `formats` in any `save` call.

All output lands in an `output` directory in the `scripts` directory.
