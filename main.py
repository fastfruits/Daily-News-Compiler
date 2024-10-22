import requests
import json
import ui
from datetime import date

print(str(date.today()))

def getToken(file_path, variable):
    with open(file_path, 'r') as file:
        config = json.load(file)
        return config.get(variable)

def my_custom_function():
    url = "https://api.worldnewsapi.com/search-news?text=earth+quake&language=en&earliest-publish-date=" + str(date.today()) + ""
    api_key = getToken('config.json', 'newsToken')

    headers = {
        'x-api-key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    print(my_custom_function())

ui.createWindow()