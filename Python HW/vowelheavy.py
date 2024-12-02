""" Problem 1: Vowel Heavy
We say that a string is "vowel heavy" if at least 40% of its letters (excluding spaces) are vowels (a, e, i, o, u, or y).

Write a function is_vowel_heavy(s) that determines if a string is "vowel heavy."
"""

def is_vowel_heavy(s):
    counter = 0
    for character in s:
        if character in "aeiouyAEIOUY":
            counter += 1
    if counter/len(s) >= 0.4:
        return(True)
    else:
        return(False)
 

print(is_vowel_heavy("adieu"))     # True
print(is_vowel_heavy("pants"))     # False
print(is_vowel_heavy("legs"))     # false
print(is_vowel_heavy("rope"))     # true
print(is_vowel_heavy("play"))     # true




""" Problem 2: Count Long Vowels
Write a function count_long_vowels(s) that counts how many double vowels are in a string s.

You may assume that there will never be triple vowels. 
"""
#I tried this, but it kept just returning 0
def count_long_vowels(s):
    vowellist = ["aa", "ee", "ii", "OO", "uu", "yy", "AA", "EE", "II", "OO", "UU", "YY"]
    counter = 0
    for character in s:
        if character in vowellist:
            counter += 2
    return(counter)

print(count_long_vowels("aardvarks are cool"))          # 2

#I also tried this, but im not sure it works very well, if at all, it just kept giving me whatever I told it to add to count at the bottom, and it only worked for the last test case, soooo....
def count_long_vowels(s, substring, sub, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10):
    count = 0
    small_len = len(substring)
    big_len = len(s)
    if big_len == small_len:
        if s == substring:
            return(1)
        else:
            return(0)
    if small_len > big_len:
        return(0)
    for index in range(len(s) - small_len + 1):
        if s[index : index + small_len] == substring:
            count += 1
    return(count)

print(count_long_vowels("banana", "aa", "ee", "ii", "oo", "uu", "yy", "AA", "EE", "II", "OO", "UU", "YY"))              # 0
print(count_long_vowels("banana", "aa", "ee", "ii", "oo", "uu", "yy", "AA", "EE", "II", "OO", "UU", "YY"))             # 0
print(count_long_vowels("banana", "aa", "ee", "ii", "oo", "uu", "yy", "AA", "EE", "II", "OO", "UU", "YY"))            # 0
print(count_long_vowels("banana ban", "aa", "ee", "ii", "oo", "uu", "yy", "AA", "EE", "II", "OO", "UU", "YY"))        # 0
print(count_long_vowels("banana ban", "aa", "ee", "ii", "oo", "uu", "yy", "AA", "EE", "II", "OO", "UU", "YY"))         # 0
print(count_long_vowels("cool pools rule", "aa", "ee", "ii", "oo", "uu", "yy", "AA", "EE", "II", "OO", "UU", "YY"))  #2
print(count_long_vowels("aardvarks are cool", "aa", "ee", "ii", "oo", "uu", "yy", "AA", "EE", "II", "OO", "UU", "YY"))      
