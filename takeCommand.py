from speak import speak
import speech_recognition as sr


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening..")
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        speak("Say that again please")
        return "None"
    return query


def takenumber():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening..")
        print("Listening..")
        audio = r.listen(source)
    try:
        print("Recognizing..")
        input1 = r.recognize_google(audio)
        return int(input1)
    except Exception as e:
        speak("Say the number again please")
        return 0


def takestring():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening..")
        print("Listening..")
        audio = r.listen(source)
    try:
        print("Recognizing..")
        input1 = r.recognize_google(audio)
        return str(input1)
    except Exception as e:
        speak("Say the number again please")
        return 0
