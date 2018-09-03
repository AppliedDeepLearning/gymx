import argparse

from . import config
from .server import serve

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--address')
    parser.add_argument('--host', default=config.host)
    parser.add_argument('--port', default=config.port)
    args = parser.parse_args()
    serve(args.address or '{}:{}'.format(args.host, args.port))
