
all: html pdf

html: style.css jeu-troll.md
	python build.py

pdf: print.html
	pandoc print.html -o jeu-troll-brut.pdf -V geometry:margin=1in
