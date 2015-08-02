#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import CommonMark
import jinja2
from codecs import open
from jinja2 import Environment, FileSystemLoader

pages = (
    {'input': 'jeu-troll.md', 'output': 'index.html'},
    {'input': 're-troll.md', 'output': 're-troll.html', 'subtitle': "re-troll"},
    {'input': ['jeu-troll.md', 're-troll.md'], 'output': 'print.html', 'template': 'print.html'},
)

if __name__ == '__main__':
    default_template = 'base.html'

    for page in pages:
        template_name = page.get('template', default_template)
        output_file = page.get('output')
        input_files = page.get('input')
        subtitle = page.get('subtitle', None)

        print("{} + {} = {}".format(input_files, template_name, output_file))

        parser = CommonMark.DocParser()
        renderer = CommonMark.HTMLRenderer()
        if isinstance(input_files, (str, unicode)):
            input_files = [input_files]

        contents = []
        for input_file in input_files:
            with open(input_file, encoding='utf8') as fd:
                contents.append(fd.read())

        content = '\n----\n'.join(contents)
        ast = parser.parse(content)
        html = renderer.render(ast)

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(template_name)
        output = template.render(content=html, subtitle=subtitle)

        with open(output_file, 'w', encoding='utf8') as fd:
            fd.write(output)
