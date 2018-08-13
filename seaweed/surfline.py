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
    print("These spots matched your search:\n")
    for hit in data[0]["hits"]["hits"]:
        print(hit["_source"]["name"])

def getForecastDays(forecastType):
    # These are the types of forecasts offered based on the users preference
    forecastTypes = {
        "forecast": 7,
        "today": 1,
        "tomorrow": 2,
        "weekend": 3, # TODO - Figure out how to get the weekend forecast
    }

    return forecastTypes[forecastType]

def createForecast(spotId, forecastType):
    # This function takes care of composing the multiple forecast types
    days = getForecastDays(forecastType)
    waveForecast(spotId, days)

def waveForecast(spotId, days):
    # Set up parameters dictionary
    parameters = {
        "spotId": spotId,
        "days": days
    }

    response = requests.get("https://services.surfline.com/kbyg/spots/forecasts/wave", params=parameters)
    print(len(response.json()["data"]["wave"]))