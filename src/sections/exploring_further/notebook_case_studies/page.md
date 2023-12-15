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
# 💡 Notebook case studies

Browse our collection of Jupyter notebook examples involving scientific image processing and analysis in Python.

```{code-cell} ipython3
:tags: [remove-input]

import pandas as pd
from itables import init_notebook_mode
from itables import show

init_notebook_mode(all_interactive=True)

df = pd.read_csv('./notebook_case_studies.csv')

df["Title"] = [
    '<a href="./{}">{}</a>'.format(link, name)
    for link, name in zip(df["Link"], df["Title"])
]

df["Image"] = [
    '<img src="../../../_images/{}" alt="Image" width="500">'.format(image)
    for image in df["Image"]
]

df.drop(['Link', 'Keywords'], axis='columns', inplace=True)

show(df, classes="display compact", paging=False)
```