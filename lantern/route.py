from sanic.response import html
from lantern.handle import execute_handle
from lantern.error import error_response
from lantern.request import serialize_request
import os


def build_main_route(args):
    handle = os.path.abspath(args.handler)
    if not os.path.isfile(handle) or not os.access(handle, os.X_OK):
        raise FileNotFoundError("Can't find handle at {}".format(handle))

    async def main_route(request, path=None):
        result = execute_handle(handle, serialize_request(request))
        if result.exit_code != 0:
            return error_response(result.error)

        return html(result.html, status=200)

    return main_route
