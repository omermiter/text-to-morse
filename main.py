morse_code_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


# function to encode plain English text to morse code

def to_morse(text):
    letter_list = [letter for letter in text]
    morse_translation_list = [morse_code_dict[item] for item in letter_list]
    morse_translation = ""
    for morse in morse_translation_list:
        morse_translation += morse
        morse_translation += " "
    return morse_translation


# function to decode morse code into plain English
def from_morse(text):
    key_list = list(morse_code_dict.keys())
    values_list = list(morse_code_dict.values())
    translation_list = [key_list[values_list.index(code)] for code in text]
    translation = ""
    for letter in translation_list:
        translation += letter

    return translation

active = True

while active:
    route_choice = input("Would you like to encode or decode?\n")
    if route_choice.lower() == "encode":
        active = False
        text = input("You have chosen to encode, please enter the text:\n")
        print(to_morse(text.replace(" ", "")))
    elif route_choice.lower() == "decode":
        active = False
        text = input("You have chosen to decode, please enter the text:\n")
        print(from_morse(text.split(" ")))
    else:
        print("You have entered an invalid input, you may only submit encode or decode")
