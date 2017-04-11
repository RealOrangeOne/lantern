from sanic import Sanic
from lantern.route import main_route
import os

app = Sanic(__name__)


def main():
    workers = int(os.cpu_count()) or 1
    app.add_route(main_route, "/<path>")
    app.add_route(main_route, "/")
    app.run(host="0.0.0.0", port=8000, workers=workers)
