import datetime
from email import message
import webbrowser
from numpy import tile
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from Dictapp import openappweb, closeappweb
from Jarvis_Final.GreetMe import thank_you



for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if a==pw:
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif i==2 and a!=pw:
        exit()

    elif a!=pw:
        print("Try Again")



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query




if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()


            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    from GreetMe import sleep_mode
                    sleep_mode()  # Now it speaks!
                    break


                #################### JARVIS: THe Trilogy 2.0 #####################

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")



                elif "translate" in query:
                    from Translator import translategl

                    query = query.replace("translate", "")
                    translategl(query)




                elif "cricket" in query or "match" in query or "score" in query:
                    from game import get_cricket_score_and_upcoming

                    get_cricket_score_and_upcoming()



                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")                       
                     




                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")



                
                

                ############################################################
                elif "hello" in query:
                    speak("Hello sir")



                elif "how are you" in query:
                    from GreetMe import how_are_you
                    how_are_you()

                elif "thank you" in query:
                    from GreetMe import thank_you

                    thank_you()
                

                
                elif "volume up" in query:
                    from keyboard import volumeup

                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown

                    volumedown()

                elif "open" in query or "launch" in query:
                    openappweb(query)

                elif "close" in query:
                    closeappweb(query)



                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)


                elif "calculate" in query:
                    from Calculatenumbers import  Calc
                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)


                elif " whatsapp" in query:
                    from Whatsapp import send_whatsapp

                    send_whatsapp()


                elif "weather" in query:
                    from weather import get_weather, speak

                    city = query.replace("weather in", "").strip()  # Extract city name from query
                    weather_report = get_weather(city)
                    speak(weather_report)
                    print(weather_report)  # For debugging



                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    from GreetMe import finally_sleep
                    finally_sleep()
                    exit()


                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break







                




                


 