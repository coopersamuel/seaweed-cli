'''
    This is the entry point for the CLI
'''

import sys
from .surfline import search

def main():
    # Parse args passed to the cli
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
        search(arg)

if __name__ == '__main__':
    main()