import ui
import threading
from worldnews import NewsManager
from gpt import GPTManager
from elevenlabsVoice import VoiceManager
from audio import AudioManager
import queue

generateQ = ui.generate_q
voice = ui.voice
FIRST_SYSTEM_MESSAGE = "Summarize every prompt given to you so they are no more than 1500 words long but make sure to get all the important details."


def mainFunction():
    while generate == False:
        if not generateQ.empty():
            ui.generate = generateQ.get()
    GPTManager.chat_history.append(FIRST_SYSTEM_MESSAGE)

    VOICE = voice

    NewsManager.mainFunction()
    print("running")

    wnResult = open("txtReturn.txt", "r")

    gptResult = GPTManager.chat(wnResult)

    with open("txtReturn.txt", "w") as file:
        file.write(str(gptResult))

    elevenlabsResult = VoiceManager.tta(gptResult, VOICE, False)

    AudioManager.playAudio(elevenlabsResult, True, True, True)


if __name__ == "__main__":
    print(mainFunction())

background_thread = threading.Thread(target=mainFunction, daemon=True)
background_thread.start()

ui.createWindow()