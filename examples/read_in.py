#!/usr/bin/env python3

import sys
import json

print("<h1>Hello!</h1>")

request = json.loads(sys.stdin.read())


print("<p>You're looking at {}.</p>".format(request['url']))
