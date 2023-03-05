import datetime
import smtplib
import sys
import webbrowser
import os
import time
import pyttsx3
import pywhatkit
import requests
import wikipedia
import subprocess as sp
from speak import speak
from takeCommand import takecommand
from wishme import wishme
from GuessTheNumber import guess_the_number
from whatsappmsg import send_whatsapp_message


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('suvarnalaxmi@gmail.com', 'admin@123')
    server.sendmail('suvarnalaxmi25@gmail.com', to, content)
    server.close()

def play_on_youtube(video):
    pywhatkit.playonyt(video)

def search_on_google(query):
    pywhatkit.search(query)

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

# def search_on_stackoverflow():
#     pywhatkit.search(query)
yes="yes"
no="no"

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("what do you want to search on wikipedia?")
            search_query = takecommand().lower()
            speak("Searching wikipedia")
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia" + results)
            speak("For your convenience, I am printing it on the screen")
            print(results)
        elif 'youtube' in query:
            speak("What do you want to play on youtube?")
            video = takecommand().lower()
            play_on_youtube(video)
            # webbrowser.open("youtube.com")
        elif 'search on google' in query:
            speak("What do you want to search on google?")
            query = takecommand().lower()
            search_on_google(query)
            # webbrowser.open("google.com")
        elif 'send whatsapp message' in query:
            speak("Which number you want to send the message?")
            number=takecommand().lower()
            speak("The number is "+number)
            speak("What message do you want to send?")
            msg=takecommand().lower()
            send_whatsapp_message(number,msg)
        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\suvar\\Downloads\\New folder\\Jarvis\\Jarvis\\songs\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            tTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(tTime)
            print(tTime)
        elif 'open code' in query:
            codePath = 'C:\\Users\\lambt\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'email myself' in query:
            try:
                speak("What should I say")
                content = takecommand()
                to = "suvarnalaxmi25@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Unable to send this email. Please check your connection")
        elif 'open camera' in query:
            sp.run('start microsoft.windows.camera:', shell=True)
            time.sleep(5)
        elif 'open notepad' in query:
            notepadPath = 'C:\\Windows\\notepad.exe'
            os.startfile(notepadPath)
        elif 'open cmd' in query:
            os.system('start cmd')
        elif 'open calculator' in query:
            calculatorPath = 'C:\\Windows\\System32\\calc.exe'
            sp.Popen(calculatorPath)
        elif 'joke' in query:
            speak(f"hope you like this one")
            joke = get_random_joke()
            speak(joke)
            print(joke)
        elif 'guess the number' in query:
            guess_the_number()
        elif 'open microsoft word' in query:
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')
        elif 'open microsoft excel' in query:
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe')
        elif 'open microsoft powerpoint' in query:
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe')
        elif 'exit' in query:
            sys.exit()
        