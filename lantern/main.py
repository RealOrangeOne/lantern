from sanic import Sanic
from sanic_useragent import SanicUserAgent
from lantern.route import main_route
import os

app = Sanic(__name__)
SanicUserAgent.init_app(app)


def main():
    workers = os.cpu_count() or 1
    app.add_route(main_route, "/<path>")
    app.add_route(main_route, "/")
    app.run(host="0.0.0.0", port=8000, workers=workers)
