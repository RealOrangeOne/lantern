from sanic import Sanic
from sanic.response import json, text
from sanic.exceptions import NotFound

app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})


@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Page not found at {}".format(request.url), status=404)


def main():
    app.run(host="0.0.0.0", port="8000")
