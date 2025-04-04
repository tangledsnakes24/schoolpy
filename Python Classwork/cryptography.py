""" Day 3: Cryptography """

# Problem 1: Caesar Cipher
def number_to_letter(num):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = (num - 1) % 26
    return(all_letters[index])
print(number_to_letter(1))
print(number_to_letter(2))
print(number_to_letter(3))
print(number_to_letter(4))


print(number_to_letter(27))
print(number_to_letter(28))
print(number_to_letter(29))
print(number_to_letter(30))
def letter_to_number(letter):
    
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for num in range(1, 27):
        current_letter = number_to_letter(num)
        if current_letter == letter:
            return(num)
        
    return()
print(letter_to_number("A"))
print(letter_to_number("B"))
print(letter_to_number("C"))
print(letter_to_number("D"))
print(letter_to_number("E"))

def caesar(message, shift):
    new_s = ""
    for letter in message:
        if letter == " ":
            new_s += " "
        else:
            num = letter_to_number(letter)
            num = num + shift
            new_letter = number_to_letter(num)
            new_s += new_letter
        
    return(new_s)

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
    new_message = ""
    for letter in message:
        if letter == " ":
            new_message += "// "
        else:
            morse_letter = letter_to_morse_dict[letter]
            new_message += morse_letter + " "
    return(new_message[:-1])

print(morse("SOS"))                 # "... --- ..."
print(morse("HIS"))                 # ".... .. ..."
print(morse("TOME"))                # "- --- -- ."
print(morse("TO ME"))               # "- --- // -- ."


# Problem 3: Atbash

atbash_dict = {}

def atbash(message):
    return()

print(atbash("ABC"))                # "ZYX"
print(atbash("XYZ"))                # "ABC"

print(atbash("ALL"))                # "ZOO"
print(atbash("GLOW"))               # "TOLD"
print(atbash("HOLD"))               # "SLOW"
