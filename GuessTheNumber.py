import random
from speak import speak
from takeCommand import takenumber


def guess_the_number():
    speak("I am thinking of a number between 1 to 20")
    secretNumber = random.randint(1, 20)
    for guessesTaken in range(1, 7):
        speak('Take a guess')
        try :
            guess = int(takenumber())
            print(guess)
        except Exception as e:
            speak("Say again")

        if guess < secretNumber:
            speak("Your guess is too low")
        elif guess > secretNumber:
            speak("Your guess is too high")
        else:
            break

    if guess == secretNumber:
        speak("Good Job! You guessed my number in " + str(guessesTaken) + "guesses.")
        print("Good Job! You guessed my number in " + str(guessesTaken) + "guesses.")
    else:
        speak("Nope. The number I was thinking of was " + str(secretNumber))
        print("Nope. The number I was thinking of was " + str(secretNumber))
