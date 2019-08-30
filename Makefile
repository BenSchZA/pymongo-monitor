.PHONY: shell bootstrap install run clean

shell:
	nix-shell

bootstrap: ## Set up project
	[ -d venv ] || virtualenv --no-site-packages venv

install: bootstrap ## Install deps
	source venv/bin/activate; pip install -Ur requirements.txt

run:
	python main.py

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
