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

# Setup for scientific image analysis using Python

Python can be used to process, analyze, and visualize your images. Follow the steps below to get started using Python.

## 📝 Setup instructions

### Install Python using `conda`

Napari is a Python package. Therefore, to install it, you must first install Python. If you haven't yet installed Python, Anaconda, or Miniconda on your machine, we recommend you install `Miniconda` which is based on the [conda package manager](https://docs.conda.io/en/latest/). Click on the link below to download the installer:

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

### Set up your Python virtual environment

Using a virtual environments is lets you isolate the packages and dependencies that you are using for a specific project, without them interfering with other Python projects you may be working on.

Type the following commands in your terminal to create a virtual environment (named `project-env`) using `conda`:

```bash
conda create -n project-env python=3.9
```

The `-n` parameter specifies the name of the virtual environment (here, *project-env*). We also specify the Python version to be 3.9. Python is constantly evolving and new versions are regularly released. At the time of writing, modern versions include 3.8 to 3.11.

```{tip}
You can check which virtual environments are available on your machine by typing `conda env list`.
```

Next, let’s install a few Python packages into your *project-env* virtual environment. To do that, you first have to *activate* the environment.

```bash
conda activate project-env
```

If you successfully activated the environment, you should see `(project-env)` to the left of your command prompt.

### Install packages

With your `(project-env)` environment activated, install [Napari](https://napari.org/stable/) using the [pip](https://pip.pypa.io/en/stable/) package manager by typing the following commands:

```bash
pip install "napari[all]"
```

Install [Jupyter lab](https://jupyter.org/):

```bash
pip install jupyterlab
```

**Check your installation**

With your virtual environment activated,

- type `napari` in your terminal. The Napari viewer should open **in a separate window**.
- type `jupyter lab` in your terminal. This should start the Jupyter lab application in your web browser. To stop Jupyter lab, close the web browser and press `Ctrl+C` in your terminal window.

```{tip}
Some popular packages for image processing and analysis in Python are listed below.
```

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

### Use an image viewer

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

**Check your installation**

With your virtual environment activated,

- type `napari` in your terminal. The Napari viewer should open **in a separate window**.

```{note}
You can also find the official Napari installation instructions [here](https://napari.org/stable/tutorials/fundamentals/installation.html#installation).
```

### Use a code editor

Todo.

### Summary

You have set up the following:

    - Installed `Python` and `conda` through `Miniconda`.
    - Installed `Napari` which provides you with an image viewer interoperable with Python.

### 📚 Exploring further

The following might be useful:

    - Introduction to Jupyter notebooks
    - Introduction to Python scripts