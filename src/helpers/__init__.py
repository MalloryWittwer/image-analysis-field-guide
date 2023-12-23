from pathlib import Path
import pandas as pd
from itables import show
from functools import partial
from typing import List


show_online_resources = partial(
    show,
    classes="display compact", 
    columnDefs=[
        {"width": "100%", "targets": [0]},
        {"className": "dt-left", "targets": [0]}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
    dom="tr"
)

show_notebook_case_studies = partial(
    show,
    classes="display compact", 
    columnDefs=[
        {"className": "dt-left", "targets": [0]}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
    dom="tr"
)

show_software_tools = partial(
    show,
    classes="display compact", 
    columnDefs=[
        {"className": "dt-left", "targets": "_all"}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
)


def filter_online_resources(tags: List[str]):
    df = pd.read_csv(Path.cwd().parents[4] / 'db' / 'online_resources.csv')

    df["Name"] = [
        '<a href="{}">{}</a>'.format(link, name)
        for link, name in zip(df["Link"], df["Name"])
    ]   

    mask = df['Keywords'].str.contains('|'.join(tags), na=False)
    filtered_df = df[mask].copy()
    filtered_df.drop(['Link', 'Keywords'], axis='columns', inplace=True)

    return filtered_df


def filter_notebook_case_studies(tags: List[str]):
    df = pd.read_csv(Path.cwd().parents[4] / 'db' / 'notebook_case_studies.csv')

    df["Title"] = [
        '<a href="../../../exploring_further/notebook_case_studies/notebooks/{}">{}</a>'.format(link, name)
        for link, name in zip(df["Link"], df["Title"])
    ]

    df["Image"] = [
        '<img src="../../../../_images/{}" alt="Image" width="300">'.format(image)
        for image in df["Image"]
    ]

    mask = df['Keywords'].str.contains('|'.join(tags), na=False)
    df = df[mask].copy()
    df.drop(['Link', 'Keywords', 'Description'], axis='columns', inplace=True)

    return df


def filter_software_tools(tags: List[str]):
    df = pd.read_csv(Path.cwd().parents[4] / 'db' / 'software_tools.csv')

    df["Software tool"] = [
        '<a href="{}">{}</a>'.format(link, name)
        for link, name in zip(df["Homepage"], df["Software tool"])
    ]

    df["Technology"] = [
        ''.join(['<button class="btn btn-light btn-xs" onclick="insertText(this)" style="padding: 1px; margin: 4px 2px; font-size: 12px;">{}</button>'.format(keyword) for keyword in str(keywords).split(', ')])
        for keywords in df["Technology"]
    ]

    df["Keywords"] = [
        ''.join(['<button class="btn btn-light btn-xs" onclick="insertText(this)" style="padding: 1px; margin: 4px 2px; font-size: 12px;">{}</button>'.format(keyword) for keyword in str(keywords).split(', ')])
        for keywords in df["Keywords"]
    ] + df["Technology"]

    df.drop('Technology', axis='columns', inplace=True)

    mask = df['Used for'].str.contains('|'.join(tags), na=False)
    filtered_df = df[mask].copy()

    filtered_df.drop(['Homepage', 'Tested and approved by the authors', 'Used for'], axis='columns', inplace=True)

    return filtered_df