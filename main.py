import time 
# import playsound

morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

message = input("Type your message here: ")
morse_message = " ".join(morse_code_dict[c] for c in message.upper())

def play_morse_code(message):
    for c in morse_message:
        if c == ".":
            playsound("short_beep.wav")
            time.sleep(0.3)
        elif c == "-":
            playsound("long_beep.wav")
            time.sleep(0.3)
        elif c == "/" or c == " ":
            time.sleep(0.5)
        else:
            print("Invalid character detected.")

play_morse_code(message)