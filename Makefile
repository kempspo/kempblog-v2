.PHONY: html clean serve publish

html:
	uv run pelican content -o output -s pelicanconf.py

clean:
	rm -rf output

serve:
	uv run pelican --listen --autoreload --port 8000 content -o output -s pelicanconf.py

publish:
	uv run pelican content -o output -s publishconf.py
