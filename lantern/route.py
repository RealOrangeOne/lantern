from sanic.response import json


async def main_route(request, path=None):
    return json({"hello": "world"})
