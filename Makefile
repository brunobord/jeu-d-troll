
all: html pdf

html: style.css jeu-troll.md
	python build.py index.html

pdf: index.html
	pandoc index.html -o jeu-troll-brut.pdf
