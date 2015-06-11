import sys
import CommonMark
import jinja2
from codecs import open
from jinja2 import Environment, FileSystemLoader

if __name__ == '__main__':
    output_file = 'index.html'
    template_name = 'base.html'

    if len(sys.argv) >= 2:
        output_file = sys.argv[1]
    if len(sys.argv) >= 3:
        template_name = sys.argv[2]

    print output_file, template_name

    parser = CommonMark.DocParser()
    renderer = CommonMark.HTMLRenderer()
    with open('jeu-troll.md', encoding='utf8') as fd:
        content = fd.read()
    ast = parser.parse(content)
    html = renderer.render(ast)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    output = template.render(content=html)

    with open(output_file, 'w', encoding='utf8') as fd:
        fd.write(output)
