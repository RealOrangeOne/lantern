from sanic import Sanic
from lantern.route import main_route


app = Sanic()


def main():
    app.add_route(main_route, "/<path>")
    app.add_route(main_route, "/")
    app.run(host="0.0.0.0", port="8000")
