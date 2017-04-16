# lantern
[![CircleCI](https://img.shields.io/circleci/project/github/RealOrangeOne/lantern.svg?style=flat-square)](https://circleci.com/gh/RealOrangeOne/lantern)

Write a web server in _almost_ any language.

## Usage
    $ lantern --help
    usage: lantern [-h] [--port PORT] handler

    positional arguments:
    handler      Executable to run

    optional arguments:
    -h, --help   show this help message and exit
    --port PORT  Port to listen on

`handler` should be your executable program. It should be executable without any additional arguments (eg `./handler.py`).

## How it works
When a request is sent to lantern, the handler program is called, and request data passed through `stdin`. Anything passed to `stdout` will be returned to the client. This data must be standard text / HTML.

You can't really write it in a language that doesn't support reading from `stdin` / writing to `stdout`, but almost all languages support this.

### Request Data
Request data is fetched from sanic, and serialized to JSON. THe exact keys serialized can be found in `lantern/request.py`, and descriptions can be found in the [sanic docs](http://sanic.readthedocs.io/en/latest/sanic/request_data.html).

Additionally, there's also the [useragent](https://github.com/lixxu/sanic-useragent) plugin installed, which adds useragent data to the request at `useragent`.

## Why
I build this simply for testing, I wanted to have a play around with [sanic](https://github.com/channelcat/sanic/), and needed something to help me do [this project]().

## _"Can I use this in production?"_
Technically yes, there's nothing stopping you, But please, __Please__ don't!

Whilst thanks to [sanic](https://github.com/channelcat/sanic/) it's super fast, it's not designed to be secure, scalable, or even particularly stable.

If you want to use a language in production, use a web framework in that language, eg [Django](https://www.djangoproject.com/) or [Hyper](https://hyper.rs/).

## Examples
See the `examples/` directory for some basic examples. eg:

    $ lantern examples/simple.sh
