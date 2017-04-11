from sanic.response import html
from lantern.handle import execute_handle, get_http_status_code
import os


async def main_route(request, path=None):
    handle = os.path.join(os.path.dirname(__file__), 'test_handle.py')
    result = execute_handle(handle, {})
    return html(result.html, status=get_http_status_code(result.exit_code))
