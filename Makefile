
all: html pdf

html: style.css jeu-troll.md
	python build.py index.html
	python build.py print.html print.html

pdf: print.html
	pandoc print.html -o jeu-troll-brut.pdf -V geometry:margin=1in
