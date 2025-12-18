from pynput.keyboard import Key,Controller

from time import sleep

import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

keyboard = Controller()

def volumeup():
    speak("Turning volume up,sir")
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    speak("Turning volume down,sir")
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

