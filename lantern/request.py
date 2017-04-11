from sanic.exceptions import InvalidUsage


SERIALIZE_ATTRS = [
    'args',
    'form',
    'url',
    'ip',
    'query_string'
]


def serialize_request(request):
    serialized = {key: getattr(request, key) for key in SERIALIZE_ATTRS}
    try:
        serialized['json'] = request.json
    except InvalidUsage:  # if there's no body, we cant add it
        pass
    serialized['user_agent'] = request['user_agent'].to_dict()
    return serialized
