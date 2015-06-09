
all: html pdf

html: style.css markdown.css jeu-troll.md
	pandoc -t html -f markdown -s -c markdown.css -c style.css jeu-troll.md > index.html

pdf: index.html
	pandoc index.html -o jeu-troll.pdf
