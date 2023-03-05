from email import message
from speak import speak
from takeCommand import takecommand
import pywhatkit

def send_whatsapp_message(number,msg):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}",msg)



