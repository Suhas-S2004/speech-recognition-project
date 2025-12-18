# app.py

import os
import webbrowser
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Dictionary of known applications
dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "notepad": "notepad"
}

# For closing apps: map app name to process name
app_processes = {
    "paint": "mspaint.exe",
    "notepad": "notepad.exe",
    "chrome": "chrome.exe",
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "vlc": "vlc.exe",
    "vscode": "Code.exe",
    "command prompt": "cmd.exe"
}

def openappweb(query):
    speak("Launching, sir.")
    if ".com" in query or ".org" in query or ".co.in" in query:
        query = query.replace("open", "").replace("launch", "").replace("jarvis", "").replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        for app in dictapp:
            if app in query:
                os.system(f"start {dictapp[app]}")
                return
        speak("Sorry, I couldn't find that app.")

def closeappweb(query):
    for app in app_processes:
        if app in query:
            speak("Closing, sir.")
            os.system(f"taskkill /f /im {app_processes[app]}")
            return
    speak("Sorry, I don't know how to close that app.")

