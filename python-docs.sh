mkdir docs

pydoctor --make-html --html-output=docs/ src/main.py src/Controller/*.py src/Vista/*.py
