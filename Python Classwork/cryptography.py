""" Day 3: Cryptography """

# Problem 1: Caesar Cipher

def caesar(message, shift):
    #build a dictionary



    #use the dictionary
    return()

print(caesar("ABC", 0))             # "ABC"
print(caesar("ABC", 1))             # "BCD"
print(caesar("ABC", 25))            # "ZAB"
print(caesar("ABC", 26))            # "ABC"

print(caesar("HELLO WORLD", 0))     # "HELLO WORLD"
print(caesar("HELLO WORLD", 1))     # "IFMMP XPSME"
print(caesar("HELLO WORLD", 2))     # "JGNNQ YQTNF"

print(caesar("HELLO WORLD", 24))    # "FCJJM UMPJB"
print(caesar("HELLO WORLD", 25))    # "GDKKN VNQKC"
print(caesar("HELLO WORLD", 26))    # "HELLO WORLD"

# Problem 2: Morse Code

letter_to_morse_dict = {"A": ".-",
                        "B": "-...", 
                        "C": "-.-.", 
                        "D": "-..", 
                        "E": ".", 
                        "F": "..-.", 
                        "G": "--.", 
                        "H": "....", 
                        "I": "..", 
                        "J": ".---", 
                        "K": "-.-", 
                        "L": ".-..", 
                        "M": "--", 
                        "N": "-.", 
                        "O": "---", 
                        "P": ".--.", 
                        "Q": "--.-", 
                        "R": ".-.", 
                        "S": "...", 
                        "T": "-", 
                        "U": "..-", 
                        "V": "...-", 
                        "W": ".--", 
                        "X": "-..-", 
                        "Y": "-.--", 
                        "Z": "--.."}

def morse(message):
    return()

print(morse("SOS"))                 # "... --- ..."
print(morse("HIS"))                 # ".... .. ..."
print(morse("TOME"))                # "- --- -- ."
print(morse("TO ME"))               # "- -- // -- ."


# Problem 3: Atbash

atbash_dict = {}

def atbash(message):
    return()

print(atbash("ABC"))                # "ZYX"
print(atbash("XYZ"))                # "ABC"

print(atbash("ALL"))                # "ZOO"
print(atbash("GLOW"))               # "TOLD"
print(atbash("HOLD"))               # "SLOW"
