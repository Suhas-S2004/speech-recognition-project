import pywhatkit
import datetime
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
    try:
        print(" Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f" You said: {query}")
    except:
        speak("Sorry, I didn't catch that.")
        return "None"
    return query.lower()

def send_whatsapp():
    speak("Please type the number including country code.")
    phone_number = input("Enter phone number (with country code, no + sign): ")
    phone_number = "+{}".format(phone_number.strip())

    speak("What message do you want to send?")
    message = takeCommand()

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # Scheduled 2 minutes ahead

    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        speak("Message scheduled successfully.")
    except Exception as e:
        print("Error:", e)
        speak("Failed to send the message.")
