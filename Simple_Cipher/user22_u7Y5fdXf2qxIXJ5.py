# Simple Cipher Text Generator
# Rohan Roy - 2nd Nov 2013

import simplegui
import random

# Global Variables
CIPHER = {}
LETTER = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ1234567890!@#$%&" "'
message = ""

# Helper Function
def init():
    letter_list = list(LETTER)
    random.shuffle(letter_list)
    for ch in LETTER:
        CIPHER[ch] = letter_list.pop()
        
# Encoding Fuction        
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message , " encodes to ",emsg
    
# Decoding Function   
def decode():
    dmsg = ""
    for ch in message:
        for key,value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message , " decodes to ", dmsg
# Input Message Function    
def newmsg(msg):
    global message
    message = msg
    label1=label2.set_text(msg)
    
# Frames for the program   
frame = simplegui.create_frame("SimpleCipher",2,300,300)
frame.add_input("Message:", newmsg,200)
label1 = frame.add_label("Input Message:")
label2 = frame.add_label("",200)
frame.add_button("Encode",encode)
frame.add_button("Decode",decode)

# Initialization of the program
init()

# Starting of the frame
frame.start()
