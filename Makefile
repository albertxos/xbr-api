vss:
	python \
		./extern/vss/vspec2xbr.py \
		./extern/vss/vss_rel_1.0.json \
		./api/namespace/org/genivi/vss

requirements:
	pip install -r requirements.txt
	pip install -e ./sphinxcontrib_xbr

prepare:
	python3 -m venv ~/cpy3_2
	source ~/cpy3_2/bin/activate
	pip install -U setuptools pip
