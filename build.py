import sys
import CommonMark
import jinja2
from codecs import open
from jinja2 import Environment, FileSystemLoader

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) >= 2:
        output_file = sys.argv[1]
    else:
        output_file = 'index.html'
    parser = CommonMark.DocParser()
    renderer = CommonMark.HTMLRenderer()
    with open('jeu-troll.md', encoding='utf8') as fd:
        content = fd.read()
    ast = parser.parse(content)
    html = renderer.render(ast)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('base.html')
    output = template.render(content=html)

    with open(output_file, 'w', encoding='utf8') as fd:
        fd.write(output)
