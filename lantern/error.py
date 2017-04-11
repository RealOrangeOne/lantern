from jinja2 import Template
from sanic.response import html
import os


TEMPLATE = os.path.join(os.path.dirname(__file__), 'templates', 'error.html')


def error_response(error_str):
    with open(TEMPLATE) as f:
        template = Template(f.read())
    return html(template.render(error=error_str), status=500)
