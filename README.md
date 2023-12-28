# The Image Analysis Field Guide

## Installation

```
pip install -r requirements.txt
```

## Build the Jupyter book

```
jupyter-book build src/
```

Then, drag and drop `_build/html/index.html` in a web browser.

To also check the external links:

```
jb build src --builder linkcheck
```

## With `docker`

```
docker build -t $(whoami)/$(basename ${PWD}) .
```

Run the jupyter book on `http://localhost:8080/`.

```
docker run --rm -it -p 8080:80 $(whoami)/$(basename ${PWD}):latest
```

Persistent:

```
docker run -dp 8080:80 --name image-analysis-field-guide $(whoami)/$(basename ${PWD}):latest
```

## On GitHub & Pages

- Add your `NOTION_KEY` to the repository **secrets**.
- Tag the repository as `jupyter-book` to have it appear in the official [Gallery](https://executablebooks.org/en/latest/gallery/).

## Launch to your own `JupyterHub`

Edit this part of `_config.yml`:

```yaml
launch_buttons:
  notebook_interface : jupyterlab
  jupyterhub_url: "http://frank1/"  # The URL for your JupyterHub.
```