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

# 🛠️ Software tools

Browse our curated list of software tools on the topic of scientific image analysis.

```{code-cell} ipython3
:tags: [remove-input]

import pandas as pd
from itables import init_notebook_mode
from itables import show
from pathlib import Path

init_notebook_mode(all_interactive=True)

df = pd.read_csv(Path.cwd().parents[3] / 'db' / 'software_tools.csv')

df["Software tool"] = [
    '<a href="{}">{}</a>'.format(link, name)
    for link, name in zip(df["Homepage"], df["Software tool"])
]

df.drop(['Homepage', 'Tested and approved by the authors'], axis='columns', inplace=True)

show(df, classes="display compact", paging=False)
```
