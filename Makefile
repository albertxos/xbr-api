default:
	@echo 'target: requirements, vss'

requirements:
	python3 -m venv ~/xbr
	source ~/xbr/bin/activate
	pip install --no-cache--update pip cbsh

vss:
	python \
		./extern/vss/vspec2xbr.py \
		./extern/vss/vss_rel_1.0.json \
		./api/namespace/org/genivi/vss
