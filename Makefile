
all: html pdf

html: style.css markdown.css jeu-troll.md
	python build.py

pdf: index.html
	pandoc index.html -o jeu-troll-brut.pdf
