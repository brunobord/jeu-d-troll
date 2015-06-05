
all: html pdf

html: style.css markdown.css jeu-troll.md
	pandoc -t html -f markdown -s -c '//fonts.googleapis.com/css?family=Droid+Serif:400,400italic,700,700italic' -c style.css -c markdown.css jeu-troll.md > index.html

pdf: index.html
	pandoc index.html -o jeu-troll.pdf
