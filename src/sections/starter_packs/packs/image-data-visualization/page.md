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
![visualization](../../../../images/visualization_lg.png)

# 🌻 Image data visualization

A number of software tools exist to help visualize scientific images and the data associated with them, such as segmentation masks, bounding boxes, and keypoints, for example.

## 🌐 Online resources

```{code-cell} ipython3
:tags: [remove-input]

import pandas as pd
from itables import init_notebook_mode
from itables import show
from pathlib import Path

init_notebook_mode(all_interactive=True)

df = pd.read_csv(Path.cwd().parents[4] / 'db' / 'online_resources.csv')

df["Name"] = [
    '<a href="{}">{}</a>'.format(link, name)
    for link, name in zip(df["Link"], df["Name"])
]

df.drop('Link', axis='columns', inplace=True)

filtered_df = df[df['Keywords'].str.contains('Visualization', na=False)]

show(
    filtered_df,
    classes="display compact", 
    columnDefs=[
        {"width": "100%", "targets": [0]},
        {"className": "dt-left", "targets": [0]}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
)
```

## 💡 Notebook case studies

```{code-cell} ipython3
:tags: [remove-input]

df = pd.read_csv(Path.cwd().parents[4] / 'db' / 'notebook_case_studies.csv')

df["Title"] = [
    '<a href="../../../exploring_further/notebook_case_studies/notebooks/{}">{}</a>'.format(link, name)
    for link, name in zip(df["Link"], df["Title"])
]

df["Image"] = [
    '<img src="../../../../_images/{}" alt="Image" width="500">'.format(image)
    for image in df["Image"]
]

df = df[df['Keywords'].str.contains('Visualization', na=False)]
df.drop(['Link', 'Keywords'], axis='columns', inplace=True)

show(
    df, 
    classes="display compact", 
    columnDefs=[
        {"className": "dt-left", "targets": "_all"}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
)
```

## 🛠️ Software tools

```{code-cell} ipython3
:tags: [remove-input]

df = pd.read_csv(Path.cwd().parents[4] / 'db' / 'software_tools.csv')

df["Software tool"] = [
    '<a href="{}">{}</a>'.format(link, name)
    for link, name in zip(df["Homepage"], df["Software tool"])
]

df.drop(['Homepage', 'Tested and approved by the authors'], axis='columns', inplace=True)

filtered_df = df[df['Used for'].str.contains('Visualization', na=False)]

show(
    filtered_df,
    classes="display compact", 
    columnDefs=[
        {"className": "dt-left", "targets": "_all"}
    ],
    paging=False,
    showIndex=False,
)
```