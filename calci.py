import operator
import string
import speech_recognition as s_r
from speak import speak

# print("Your speech_recognition version is: "+s_r.version)
r = s_r.Recognizer()
my_mic_device = s_r.Microphone(device_index=1)
with my_mic_device as source:
    print("Say what you want to calculate, example: 3 plus 3")
    speak("Say what you want to calculate, example: 3 plus 3")
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    speak("Listening")
    audio = r.listen(source)
my_string = r.recognize_google(audio)
print(my_string)


def get_operator_fn(op):
    return {
        "+": operator.add,
        "-": operator.sub,
        "X": operator.mul,
        "/": operator.truediv,
        "Mod": operator.mod,
        "mod": operator.mod,
        "exponent": operator.pow,
    }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


ans = eval_binary_expr(*(my_string.split()))
speak("the answer is ")
speak(ans)
print("The answer is ", (eval_binary_expr(*(my_string.split()))))
