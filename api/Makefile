default:
	@echo "targets: requirements clean html"

clean:
	-rm -rf ./_build

requirements:
	pip install -U pip sphinx sphinx_rtd_theme

html:
	sphinx-build -M html . _build
