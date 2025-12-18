import pyttsx3
import speech_recognition as sr
import random

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

# Speak the given text
def speak(text):
    print(f" Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# Normalize possible speech errors
def normalize_choice(query):
    query = query.lower()
    if "rock" in query or "rack" in query or "lock" in query:
        return "rock"
    elif "paper" in query or "piper" in query or "pay per" in query:
        return "paper"
    elif "scissors" in query or "scissor" in query or "sister" in query:
        return "scissors"
    else:
        return None

# Take voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, phrase_time_limit=4)

    try:
        print(" Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" You Said: {query}\n")
        return query
    except Exception:
        print(" Say that again please...")
        return "None"

# Game logic
def game_play():
    speak("Let's play Rock Paper Scissors!")
    print(" Game Started!")

    i = 0
    me_score = 0
    com_score = 0
    options = ("rock", "paper", "scissors")

    while i < 5:
        speak(f"Round {i+1}. Say rock, paper, or scissors.")
        com_choice = random.choice(options)
        raw_query = takeCommand()

        user_choice = normalize_choice(raw_query)

        if user_choice is None:
            speak("Sorry, I couldn't understand. Please say rock, paper, or scissors.")
            continue

        speak(f"I chose {com_choice}.")

        if user_choice == com_choice:
            speak("It's a draw.")
        elif (user_choice == "rock" and com_choice == "scissors") or \
             (user_choice == "paper" and com_choice == "rock") or \
             (user_choice == "scissors" and com_choice == "paper"):
            me_score += 1
            speak("You win this round.")
        else:
            com_score += 1
            speak("I win this round.")

        print(f" Round {i+1} Score: YOU: {me_score}, JARVIS: {com_score}")
        i += 1

    print(f"\n Final Score: YOU: {me_score} | JARVIS: {com_score}")
    if me_score > com_score:
        speak("Congratulations! You won the game.")
    elif me_score < com_score:
        speak("I won the game. Better luck next time!")
    else:
        speak("It's a tie game!")










####################################CRICKET SCORE###########################################
# cricket.py
import requests
from bs4 import BeautifulSoup
import pyttsx3

# Text-to-speech engine
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_cricket_score_and_upcoming():
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    # First, find any live matches
    live_cards = soup.find_all("div", class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    for card in live_cards:
        status_div = card.find("div", class_="cb-text-live") or card.find("div", class_="cb-text-complete")
        if status_div:
            title = card.find("a").text.strip()
            status = status_div.text.strip()
            result = f"{title}. Status: {status}"
            print(" Live Match:", result)
            speak("Here is the live cricket update.")
            speak(result)
            return

    # No live matches found, look for upcoming
    upcoming_section = soup.find("div", class_="cb-ltst-wgt-hdr", string=lambda x: x and "upcoming" in x.lower())
    if upcoming_section:
        next_card = upcoming_section.find_next_sibling("div", class_="cb-col cb-col-100 cb-tms-itm")
        if next_card:
            title = next_card.find("a").text.strip()
            status = next_card.find("div", class_="text-gray").text.strip()
            result = f"Upcoming match: {title}. {status}"
            print(" Upcoming:", result)
            speak(result)
            return

    # If neither live nor upcoming
    speak("There are no current or upcoming matches listed at the moment.")





            

