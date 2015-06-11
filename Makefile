
all: html pdf

html: style.css markdown.css jeu-troll.md
	python build.py index2.html

pdf: index-deux.html
	pandoc index.html -o jeu-troll-brut.pdf
