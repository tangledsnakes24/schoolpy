""" Strings! """

s1 = "Hello World!"
s2 = "HELLO WORLD!"
s3 = "hello world"

# Indexing, Length, and Substrings
first_letter = s1[0] #same as list, returns H
middle_letter = s1[6] # W
otherletter = s1[5] # returns *space*
l1 = len(s1) # prints the length of s1
print(l1)

#substring is a string that is pulled out of a larger string format is *stringname*[startindex:endindex]
substring = s1[0:5]
print(substring)
# Looping over Strings
for character in s1:
    print(character)
index = 0
while index > len(s1):
    print(s1[index])
    index += 1
for index in range(len(s1)):
    print(s1[index])


# String Concatenation
str1 = "hi"
str2 = "person"
print(str1 + " " + str2 + "!")



# Upper and Lower




""" Problem 1: Count Vowels """

def count_vowels(s):
    counter = 0
    for character in s:
        if character in "aeiouyAEIOUY":
            counter += 1
    return(counter)

print("Testing Count Vowels")
print(count_vowels("Hello!"))           # 2
print(count_vowels("Goodbye!"))         # 4
print(count_vowels("Adieu!"))           # 4
print()



""" Problem 2: Remove Vowels """

def remove_vowels(s):
    new_s = ""
    for character in s:
        if not (character in "aeiouyAEIOUY"):
            new_s += character
            
        
            
    return(new_s)

print("Testing Remove Vowels")
print(remove_vowels("strings!"))                     # "strngs!"
print(remove_vowels("loops"))                        # "lps"
print(remove_vowels("you"))                          # ""
print(remove_vowels("a e i o u and sometimes y"))    # "     nd smtms "
print()

""" Problem 3: Palindrome """
def reverse(s):
    new_s = ""
    index = len(s) - 1
    while index >= 0:
        new_s = new_s + s[index]
        index = index - 1
    return(new_s)
print("Testing is Palindrome")
print(reverse("kayak"))                   # True
print(reverse("racecar"))                 # True
print(reverse("hello"))                   # False
print(reverse("too hot to hoot"))         # False
print(reverse("toohottohoot"))            # True
print()
    
def is_palindrome(s):
    if reverse(s) == (s):
        return(True)
    else:
        return(False)
    

print("Testing is Palindrome")
print(is_palindrome("kayak"))                   # True
print(is_palindrome("racecar"))                 # True
print(is_palindrome("hello"))                   # False
print(is_palindrome("too hot to hoot"))         # False
print(is_palindrome("toohottohoot"))            # True
print()



""" Problem 4: Every Other Letter """

def every_other_letter(s):
    new_s = ""
    for index in range(len(s)):
        if index % 2 == 1:
            new_s = new_s + s[index]
    return(new_s)

print("Testing Every Other Letter")
print(every_other_letter("schooled"))           # "cold"
print(every_other_letter("friends"))            # "red"
print(every_other_letter("hi!"))                # "i"
print(every_other_letter(""))                   # ""
print()

""" Problem 5: Count Substrings """

def count_substrings(s, substring):
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

print(count_substrings("banana", "a"))              # 3
print(count_substrings("banana", "na"))             # 2
print(count_substrings("banana", "ana"))            # 2
print(count_substrings("banana ban", "ban"))        # 2
print(count_substrings("banana ban", "ab"))         # 0
