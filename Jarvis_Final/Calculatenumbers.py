import pyttsx3


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



# Evaluate the math expression
def Calc(query):
    print(f" Input: {query}")

    # Replace spoken words with operators
    Term = query.lower()
    Term = Term.replace("jarvis", "")
    Term = Term.replace("what is", "")
    Term = Term.replace("calculate", "")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("multiplied by", "*")
    Term = Term.replace("times", "*")
    Term = Term.replace("into", "*")
    Term = Term.replace("divide", "/")
    Term = Term.replace("divided by", "/")
    Term = Term.replace("by", "/")
    Term = Term.replace(" ", "")

    print(f" Evaluating: {Term}")

    if not any(op in Term for op in "+-*/") :
        speak("Please include an operator .")
        return

    try:
        result = eval(Term)
        print(f" Result: {result}")
        speak(f"The answer is {result}")
    except Exception as e:
        print(f" Error: {e}")
        speak("Sorry, I could not calculate that.")
