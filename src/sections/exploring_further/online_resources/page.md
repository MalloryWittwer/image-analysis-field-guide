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
# 🌐 Online resources

Browse our curated list of online resources on the topic of scientific image analysis.

```{code-cell} ipython3
:tags: [remove-input]

import pandas as pd
from itables import init_notebook_mode
from itables import show
from pathlib import Path

init_notebook_mode(all_interactive=True)

df = pd.read_csv(Path.cwd().parents[3] / 'db' / 'online_resources.csv')

df["Name"] = [
    '<a href="{}">{}</a>'.format(link, name)
    for link, name in zip(df["Link"], df["Name"])
]

df.drop('Link', axis='columns', inplace=True)

show(df, classes="display compact", paging=False)
```
