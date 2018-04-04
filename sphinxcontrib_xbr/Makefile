clean:
	-find . -name "*.pyc" -exec rm {} -f \;
	-find . -type d -name "__pycache__" -exec rm -rf {} \;
	-rm -rf ./dist
	-rm -rf ./build
	-rm -rf ./*.egg-info/
	-rm -rf ./.tox
	-rm -rf ./.pytest_cache

install:
	#pip install -e .
	python setup.py install
