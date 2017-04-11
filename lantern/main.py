from sanic import Sanic
from sanic_useragent import SanicUserAgent
from lantern.args import parse_args
from lantern.route import build_main_route
import os

app = Sanic(__name__)
SanicUserAgent.init_app(app)


def main():
    args = parse_args()
    workers = os.cpu_count() or 1
    main_route = build_main_route(args)
    app.add_route(main_route, "/<path>")
    app.add_route(main_route, "/")
    app.run(host="0.0.0.0", port=args.port, workers=workers)
