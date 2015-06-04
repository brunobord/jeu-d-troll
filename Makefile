build: style.css markdown.css troll.md
	pandoc -t html -f markdown -s -c style.css -c markdown.css troll.md > index.html
