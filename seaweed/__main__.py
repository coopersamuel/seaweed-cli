'''
    This is the entry point for the CLI
'''

import argparse
from .surfline import search, spotSuggestion, createForecast

def main():
    args = parseArgs()
    getForecast(args.spot, args.timeframe)

    
def parseArgs():
    # Parse args passed to the cli
    parser = argparse.ArgumentParser(description="Get a surf forecast! Enter when and where you want to surf.")
    parser.add_argument('timeframe', help='when do you want to go surfing - today, tomorrow, weekend or forecast')
    parser.add_argument('spot', help='where do you want to surf')

    return parser.parse_args()

def getForecast(spot, forecastType):
    searchSpots = search(spot)
    hits = searchSpots[0]["hits"]["hits"]

    if len(hits) == 1:
        # Pull out the spot id for the single hit
        spotId = hits[0]["_id"]
        createForecast(spotId, forecastType)
    elif len(hits) > 1:
        # The user has received multiple spot suggestions, they'll need to narrow down the spot they want
        spotSuggestion(searchSpots)
    else:
        print("Couldn't find that spot")

if __name__ == '__main__':
    main()