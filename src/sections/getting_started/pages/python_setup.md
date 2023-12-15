---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.0
kernelspec:
  display_name: image-analysis-field-guide
  language: python
  name: python3
---

# 🐍 Setup for scientific image analysis using Python

Python can be used to process, analyze, and visualize your images. There are several ways of installing and setting up Python on your computer. If you have never used Python before, we recommend that you follow the steps below to get your setup ready.

## Install Python using `conda`

If you haven't yet installed Python, Anaconda, or Miniconda on your machine, we recommend you install `Miniconda` which is based on the [conda package manager](https://docs.conda.io/en/latest/). Click on the link below to download the installer:

**Miniconda**: https://docs.conda.io/en/latest/miniconda.html

Once you have downloaded the installer, run it to install Python.

`````{tab-set}
```{tab-item} Windows
1. Run the executable file you just downloaded (`Miniforge3-Windows-x86_64.exe`) and follow the instructions.
2. Launch the *Anaconda Prompt* terminal from the start menu.
```
````{tab-item} Mac / Linux
1. Open your Terminal (you can search for it in spotlight - `cmd` + `space`)
2. Navigate to the folder you downloaded the installer to using `cd`. For example:

```bash
cd ~/Downloads
```

1. Execute the installer with the command below. You can use your arrow keys to scroll up and down to read it/agree to it.

```bash
bash Miniforge3-MacOSX-x86_64.sh -b
```

2. To verify that your installation worked, close your terminal window and open a new one. You should see `(base)` to the left of your prompt.
3. Finally, initialize miniforge with the command below. This ensures that your terminal is set up correctly for your Python installation.

```bash
conda init
```
````
`````

```{admonition} Verify your installation
:class: tip
Verify that you have **conda** installed by typing `conda -V` in your terminal. This should print out a version number.
```

## Set up a Python virtual environment

A virtual environments lets you isolate the packages and dependencies that you need for a specific project. Using virtual environments will ensure that these dependencies do not create conflicts between the different Python projects you may be working on.

Type the following commands in your terminal to create a virtual environment (named `project-env`) using `conda`:

```bash
conda create -n project-env python=3.9
```

The `-n` parameter specifies the name of the virtual environment (here, *project-env*). We also specify the Python version to be 3.9. Python is constantly evolving and new versions are regularly released. At the time of writing, modern versions include 3.8 to 3.11.

```{tip}
You can print a list of the virtual environments available on your machine by typing `conda env list`.
```

## Install packages

Let’s install a few Python packages into your *project-env* environment. To do that, you first have to *activate* the environment.

```bash
conda activate project-env
```

If you successfully activated the environment, you should see `(project-env)` to the left of your command prompt.

**Jupyter lab**

[Jupyter lab](https://jupyter.org/) is a web appliation that you can use to edit and execute Python code. Install it in your environment using the [pip](https://pip.pypa.io/en/stable/) package manager by typing the following command:

```bash
pip install jupyterlab
```

```{admonition} Check your installation
Type `jupyter lab` in your terminal. This should start the Jupyter lab application you just installed in your web browser. To stop Jupyter lab, close the web browser and press `Ctrl+C` in your terminal window.
```

**Image analysis packages**

Many packages exist for image processing and analysis in Python. Some of them are listed below.

```{code-cell} ipython3
:tags: [remove-input]

import pandas as pd
from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)

df = pd.DataFrame.from_dict({
    'Package': [
        '<a href="https://opencv.org/">OpenCV</a>',
        '<a href="https://scikit-image.org/">Scikit-image</a>',
        '<a href="https://scipy.org/">Scipy</a>',
        '<a href="https://simpleitk.org/">SimpleITK</a>',
        '<a href="https://github.com/clEsperanto/pyclesperanto_prototype">py-clesperanto</a>',
    ],
    'Description': [
        "Computer vision library in Python and C++.", 
        "Image processing and analysis in Python.", 
        "Scientific computing in Python.", 
        "Image processing of 3D volumes and medical data.", 
        "GPU-accelerated image processing."
    ],
    'Install command': [
        'pip install opencv-python',
        'pip install scikit-image',
        'pip install scipy',
        'pip install SimpleITK',
        'pip install pyclesperanto',
    ]
})

df
```

The final choice of library to install will depend on your specific project. Nevertheless, to have something to work with, you can already run a `pip install scikit-image` in your virtual environment. Scikit-image will provide you with a useful collection of algorithms for image processing and analysis.

**Napari**

[Napari](https://www.napari.org/) is a multi-dimensional image viewer for Python. It is used to visualize scientific images and the data associated with them, such as segmentation masks, bounding boxes, and keypoints, for example.

With Napari, you can

- visualize timeseries, 2D, 3D, and multi-channel images.
- create interactive visualizations tailored to your needs.
- set up visualizations in a Python script or a [Jupyter notebook](https://jupyter.org/).
- annotate data (draw masks, polygons, etc.).
- use [plugins from the community](https://www.napari-hub.org/) or develop and share your own plugin.

Install [Napari](https://napari.org/stable/) by typing the following command:

```bash
pip install "napari[all]"
```

```{admonition} Check your installation
With your virtual environment activated, type `napari` in your terminal. The Napari viewer should open **in a separate window**.
```

You can also find the official Napari installation instructions [here](https://napari.org/stable/tutorials/fundamentals/installation.html#installation).

## Use a code editor

Code editors provide many useful features, including syntax highlighting, a file system manager, integrated terminals, and code auto-completion. You can also interact with Jupyter notebooks directly in your code editor instead of using your web browser.

We recommend that you pick one of the code editors below.

- [**Visual Studio Code**](https://code.visualstudio.com/) is a generalist, lightweight, and extensible editor. Use it with the Python and Jupyter extensions to easily select virtual environments and run Jupyter notebooks.
- [**Pycharm**](https://www.jetbrains.com/pycharm/) is a powerful and complete IDE for Python, ideal for managing big Python projects.
- [**Spyder**](https://www.spyder-ide.org/) is designed for scientific Python development. The interface lets you visualize current variables and figures in dedicated pannels.

## Summary

Setting up Python for working on your image analysis project typically involves the following steps.

- Install `Python` and `conda` through `Miniconda`.
- Set up a `virtual environment` with `conda` to isolate the Python packages you install from the rest of your system.
- Install packages, such as `Jupyter lab`, `Scikit-image` and `Napari` in your `virtual environment` using `pip`.
- Develop code either in `Jupyter lab` or in a dedicated `code editor`.
