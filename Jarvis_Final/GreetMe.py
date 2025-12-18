import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning ,sir ,Please tell me, How can I help you ?")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir ,Please tell me, How can I help you ?")

    else:
        speak("Good Evening ,sir ,Please tell me, How can I help you ?")




def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def sleep_mode():
    speak("Ok sir , You can call me anytime")


############################Greeting to others################################



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def how_are_you():
    speak("Perfect sir")

def thank_you():
    speak("you are welcome sir")

def finally_sleep():
    speak("Going to sleep,sir")






