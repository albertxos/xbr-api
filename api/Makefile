.PHONY: clean build test publish

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')
BUILD_DATE=$(shell date -u +"%Y-%m-%d")

default:
	@ echo ""
	@ echo "Targets:"
	@ echo ""
	@ cat Makefile | grep ':$$'

requirements: requirements_apt requirements_pip

requirements_apt:
	sudo apt install -y \
		python3 \
		python3-dev \
		python3-venv \
		awscli

requirements_pip:
	pip install --no-cache --upgrade \
		pip sphinx \
		sphinx_rtd_theme \
		sphinxcontrib_xbr

clean:
	-rm -rf ./_build

build_html:
	sphinx-build -b html . _build

build_xbr:
	sphinx-build -b xbr . _build

# https://s3.eu-central-1.amazonaws.com/xbr.foundation/api/index.html
publish:
	aws s3 cp --recursive --acl public-read \
		${PWD}/_build \
		s3://xbr.foundation/api/
