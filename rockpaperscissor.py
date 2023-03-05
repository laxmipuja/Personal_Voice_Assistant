import random,sys
from takeCommand import takecommand
from speak import speak

speak("Let's start Rock Paper Scissor Game")

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties'%(wins , losses, ties))
    speak("Enter your move : (r)ock (p)paper (s)scissor")
    playerMove = takecommand().lower()
