help:
	@echo "jeu d'troll"
	@echo
	@echo "options:"
	@echo " * html: faire site html"
	@echo " * pdf: faire pdf vilain"
	@echo " * all: faire html et pdf vilain"
	@echo
	@echo "si faire avec tox, faire:"
	@echo
	@echo "   tox -e <cible>"
	@echo ""

all: html pdf

html: style.css jeu-troll.md re-troll.md
	python build.py

pdf: print.html
	pandoc print.html -o jeu-troll-brut.pdf -V geometry:margin=1in
