import json
import ui
import threading


def mainFunction():
    print("running")


if __name__ == "__main__":
    print(mainFunction())

background_thread = threading.Thread(target=mainFunction, daemon=True)
background_thread.start()

ui.createWindow()