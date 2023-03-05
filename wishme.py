import datetime

from speak import speak


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Suvarnalaxmi!")
        print("Good Morning Suvarnalaxmi!")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon Suvarnalaxmi!")
        print("Good Afternoon Suvarnalaxmi!")
    else:
        speak("Good Evening Suvarnalaxmi!")
        print("Good Evening Suvarnalaxmi!")
    speak("I am Sophia. Please tell me how may I help you?")
    print("I am Sophia. Please tell me how may I help you?")
