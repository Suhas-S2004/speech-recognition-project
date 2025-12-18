from deep_translator import GoogleTranslator
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os
import time
from playsound import playsound

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

gtts_supported_langs = {
    'english': 'en',
    'hindi': 'hi',
    'telugu': 'te',
    'tamil': 'ta',
    'french': 'fr',
    'german': 'de',
    'spanish': 'es',
    'kannada': 'kn',
    'bengali': 'bn',
    'japanese': 'ja',
    'chinese': 'zh-CN',
    'arabic': 'ar'
}


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print(" Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" You Said: {query}\n")
    except Exception:
        print(" Say that again please...")
        return "None"
    return query


def translategl(query):
    speak("Sure sir. Please say the language you want to translate to.")
    print(" Example: Hindi, Telugu, Tamil, etc.")

    target_lang_name = takeCommand().lower()

    if target_lang_name not in gtts_supported_langs:
        speak("Sorry, this language is not supported for speech.")
        return

    target_lang_code = gtts_supported_langs[target_lang_name]

    try:
        translated_text = GoogleTranslator(source='auto', target=target_lang_code).translate(query)
        print(f" Translated: {translated_text}")
        speak(f"The translation in {target_lang_name} is: {translated_text}")

        tts = gTTS(text=translated_text, lang=target_lang_code, slow=False)
        tts.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(1)
        os.remove("voice.mp3")

    except Exception as e:
        print(" Error during translation:", e)
        speak("Sorry, something went wrong while translating.")
