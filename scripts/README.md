# io Scripts

This folder contains the scripts to generate visual representation of graph engine outputs. Currently all of the interesting scripts start with `altair`, plus the supporting files `fileops.py`, `filters.py`, and `logic.py`. The input is one or more JSONs output from Gunrock, which are then read into a dataframe and then into plots. Output goes (by default) into an `output` directory, which you should create. An example of transforming JSONs to plots is [on github](https://github.com/gunrock/io/blob/master/scripts/gunrock_plot_example.ipynb). The scripts use [pandas](https://pandas.pydata.org/) for dataframe manipulation and [Altair](https://altair-viz.github.io/) for visualization.

Altair and pandas both require Python 3.

#### List of Dependencies:
* python:
    * pandas [[install directions](https://pandas.pydata.org/pandas-docs/stable/install.html)]
    * numpy (probably a dependency of pandas)
    * Altair [[install directions](https://altair-viz.github.io/getting_started/installation.html) | [dependencies](https://altair-viz.github.io/getting_started/installation.html#dependencies)]
        * JupyterLab works well with Altair [[install directions](https://altair-viz.github.io/getting_started/installation.html#quick-start-altair-jupyterlab)]

With any sort of decent package manager, the necessary vega and vega-lite support will probably be installed along with Altair. However, we do also need vega and vega-lite command-line utilities for plot generation that are _not_ likely installed as dependencies of Altair. These run under `nodejs`, so you'll have to also install `nodejs` and (probably) build with `yarn`:

* [Vega-Lite's command-line utilities](https://vega.github.io/vega-lite/usage/compile.html#cli), specifically `vl2vg`, for which you'll probably have to install the development release (sorry)
* [vega-cli](https://vega.github.io/vega/usage/#cli), which transforms vega specifications into image files (the relevant binaries are `vg2png`, `vg2pdf`, and `vg2svg`)
