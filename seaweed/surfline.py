import requests

def search(searchTerm):
    # Set up parameters dictionary
    parameters = {
        "q": searchTerm,
        "querySize": 10,
        "suggestionSize": 10
    }

    response = requests.get("https://services.surfline.com/search/site", params=parameters)
    data = response.json()
    # print(data[0]["suggest"])
    for entry in data[0]["suggest"]["spot-suggest"][0]["options"]:
        print(entry["text"])