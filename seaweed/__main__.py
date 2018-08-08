'''
    This is the entry point for the CLI
'''

import argparse
from .surfline import search, spotSuggestion

def main():
    # This will be the only state kept for the application
    state = {
        "spotId": '',
        "forecastType": ''
    }

    # Parse args passed to the cli
    parser = argparse.ArgumentParser(description="Get a forecast!")
    parser.add_argument('forecastType', help='when do you want to go surfing - today, tomorrow, weekend or forecast')
    parser.add_argument('spot', help='where do you want to surf')

    args = parser.parse_args()

    print(args.forecastType, args.spot)

if __name__ == '__main__':
    main()