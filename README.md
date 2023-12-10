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