import requests

def search(searchTerm):
    # Set up parameters dictionary
    parameters = {
        "q": searchTerm,
        "querySize": 10,
        "suggestionSize": 10
    }

    response = requests.get("https://services.surfline.com/search/site", params=parameters)
    return response.json()

def spotSuggestion(data):
    # Print out the spot suggestions received from the surfline API
    for entry in data[0]["suggest"]["spot-suggest"][0]["options"]:
        print(entry["text"])

def getForecastDays(forecastType):
    # These are the types of forecasts offered based on the users preference
    forecastTypes = {
        "forecast": 7,
        "today": 1,
        "tomorrow": 2,
        "weekend": 3, # TODO - Figure out how to get the weekend forecast
    }

    return forecastTypes.forecastType

def waveForecast(spotId, days):
    # Set up parameters dictionary
    parameters = {
        "spotId": spotId,
        "days": days
    }

    response = requests.get("https://services.surfline.com/kbyg/spots/forecasts/wave", params=parameters)
    return response.json()