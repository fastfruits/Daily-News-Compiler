import json
import ui
import threading


def mainFunction():
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
    print(mainFunction())

background_thread = threading.Thread(target=mainFunction, daemon=True)
background_thread.start()

ui.createWindow()