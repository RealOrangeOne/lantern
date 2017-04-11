import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("handler", help="Executable to run", type=str)
    parser.add_argument("--port", help="Port to listen on", type=int, default=8000)
    parser.add_help = True
    return parser.parse_args()
