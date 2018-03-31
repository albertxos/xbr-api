# XBR API Hub Documentation

This folder contains the sources for building the XBR API Hub documentation and XBR API descriptor bundles.

---


## Why Sphinx?

> If you work in open source, then it's increasingly likely that you've come across the Sphinx documentation tool. Originally written by and for the Python community, the past few years have seen an increasingly rapid adoption by non-Python projects. Recent adopters of Sphinx include the Linux kernel, Open vSwitch and the Dataplane Development Kit (DPDK), while other projects such as QEMU are preparing plans to migrate.
[FOSDEM talk about Sphinx](https://fosdem.org/2018/schedule/event/automating_documentation_with_sphinx_extensions/)


There is now a strong consensus that APIs should be designed from front-to-back with an emphasis on the developer usability of the API. In a crowded economy with many competing products and many competing API implementations, the easy to use and well designed APIs will have an advantage in attracting and retaining developers.

Humans are the key ingredients in API design which means that API design tools and documentation formats must be human readable and writeable. Recent API documentation standards strive to be "human-centric."

https://www.infoq.com/articles/eventlog-api-raml/


## Building the docs

You need the following tools to build the docs:

* [Python](https://python.org)
* [Sphinx](https://pypi.python.org/pypi/Sphinx)
* [Sphinx RTD Theme](https://pypi.python.org/pypi/sphinx_rtd_theme)
* [Sphinx XBR Extension](https://pypi.python.org/pypi/sphinxcontrib_xbr)

Create a new Python virtual env:

```console
python3 -m venv .venv
source .venv/bin/activate
```

Install the requirements (`make requirements`):

```console
pip install-U pip sphinx sphinx_rtd_theme sphinxcontrib_xbr
```

You can now build the docs (`make html`):

```console
sphinx-build -M html . _build
```

The generated docs will be in directory `./_build`. In particular, the root HTML document will be [_build/html/index.html](_build/html/index.html).

To clean up everything (`make clean`):

```console
rm -rf ./_build/*
```

---


## Writing docs

https://github.com/vscode-restructuredtext/vscode-restructuredtext

---


## Getting your API publish

Publishing the API to the official Web site at [https://api.xbr.network](https://api.xbr.network) happens automatically once a PR with the relevant changes to `.rst` source files has been merged.

This triggers of automatic build of HTML pages, publishing to our AWS S3 bucket, and from there via AWS Cloudfront.

So all you need to do is:

* fork this repo
* create a branch, eg `"new_rabbits_api"`
* submit a PR
* work on the feedback in new commits to the PR
* when the PR has a final "GO" flag, it gets merged to master

---

