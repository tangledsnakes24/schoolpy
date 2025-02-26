""" Problem 1: Letter Frequency
Write a function that takes in a string and returns a dictionary that counts
the number of times each letter appears in the string, ignoring spaces.
"""

def letter_frequency(s):

    #for letter in s:
    #make a counter, loop over string, for each instance of the letter, counter += 1
    return()

print(freq("HELLO"))            # {"H": 1, "E": 1, "L": 2, "O": 1}
print(freq("WORLD"))            # {"W": 1, "O": 1, "R": 1, "L": 1, "D": 1}
print(freq("HELLO WORLD"))      # {"H": 1, "E": 1, "L": 3, "O": 2, "W": 1, "R": 1, "D": 1}


""" Problem 2: Bigram Frequency
A Bigram is a pair of consecutive letters in a word(e.g. BI, IG, GR, etc. in BIGRAM).

Write a function that takes in a string and returns a dictionary that counts
the number of times each bigram (pair of letters) appears in the string.

Again, ignore spaces, but do not consider bigrams that span spaces.
For example, OS is not a bigram in "NO SPACES."
"""

def bigram_frequency(s):
    return()

print(bigram_frequency("HELLO"))            # {"HE": 1, "EL": 1, "LL": 1, "LO": 1}
print(bigram_frequency("BANANA"))           # {"BA": 1, "AN": 2, "NA": 2}
print(bigram_frequency("AN ANGRY BANANA"))  # {"AN": 4, "NG": 1, "GR": 1, "RY": 1, "BA": 1, "NA": 2}
