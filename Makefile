
all: build pdf

build: style.css markdown.css troll.md
	pandoc -t html -f markdown -s -c style.css -c markdown.css troll.md > index.html

pdf: index.html
	pandoc index.html -o troll.pdf
