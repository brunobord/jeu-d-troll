#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import CommonMark
import jinja2
from codecs import open
from jinja2 import Environment, FileSystemLoader

pages = (
    {'input': 'jeu-troll.md', 'output': 'index.html'},
    {'input': 'jeu-troll.md', 'output': 'print.html', 'template': 'print.html'},
    {'input': 're-troll.md', 'output': 're-troll.html'},
)

if __name__ == '__main__':
    default_template = 'base.html'

    for page in pages:
        template_name = page.get('template', default_template)
        output_file = page.get('output')
        input_file = page.get('input')

        print("{} + {} = {}".format(input_file, template_name, output_file))

        parser = CommonMark.DocParser()
        renderer = CommonMark.HTMLRenderer()
        with open(input_file, encoding='utf8') as fd:
            content = fd.read()
        ast = parser.parse(content)
        html = renderer.render(ast)

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(template_name)
        output = template.render(content=html)

        with open(output_file, 'w', encoding='utf8') as fd:
            fd.write(output)
