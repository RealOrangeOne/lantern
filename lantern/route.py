from sanic.response import html
from lantern.handle import execute_handle
from lantern.error import error_response
from lantern.request import serialize_request
import os


async def main_route(request, path=None):
    handle = os.path.join(os.path.dirname(__file__), 'test_handle.py')
    result = execute_handle(handle, serialize_request(request))
    if result.exit_code != 0:
        return error_response(result.error)

    return html(result.html, status=200)
