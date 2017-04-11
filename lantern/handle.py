import subprocess
import json
from collections import namedtuple


Result = namedtuple('Result', ['exit_code', 'html', 'error'])


def execute_handle(executable, request_data):
    input_data = json.dumps(request_data).encode('utf-8')
    try:
        cmd = subprocess.run(executable, input=input_data, stdout=subprocess.PIPE)
    except Exception as e:
        return Result(1, None, str(e))
    return Result(
        cmd.returncode,
        cmd.stdout.decode('utf-8'),
        cmd.stderr.decode('utf-8') if cmd.stderr is not None else None
    )
