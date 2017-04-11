import subprocess
import json
from collections import namedtuple


Result = namedtuple('Result', ['exit_code', 'html', 'error'])


def execute_handle(executable, request_data):
    input_data = json.dumps(request_data).encode('utf-8')
    cmd = subprocess.run(executable, input=input_data, stdout=subprocess.PIPE)
    return Result(
        cmd.returncode,
        cmd.stdout.decode('utf-8'),
        cmd.stderr.decode('utf-8')
    )


def get_http_status_code(exit_code):
    return 200 if exit_code == 0 else 500
