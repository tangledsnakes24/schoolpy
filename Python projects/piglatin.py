""" Project: Pig Latin """


""" Problem 1: pig_latin

Given an integer word s, pig-latin-ify it! That is,
    if s starts with a consonant cluster, move it to the end and add -ay.
    if s starts with a vowel (aeiouy), just add -ay to the end.
If the original word started with a capital letter, the output should too.
.upper or .lower to change case of letter
"""

def pig_latin(s):
    nonvowelstr = ''
    vowelstr = ''
    latinified = ''
    
    for index in range (len(s)):
        char = s[index]
        if char not in "aeiouyAEIOUY":
            nonvowelstr += char
        else:
            break
        
#find a way to make the capital and lowercase letters work. maybe look at the index of the letter and if it == 1 then .upper it and if not then .lowwer it
    latinified = s[index:len(s)] + nonvowelstr + 'ay'

    
    
        


    return(latinified)

print(pig_latin("hello"))           # "ellohay"
print(pig_latin("world"))           # "orldway"
print(pig_latin("String"))          # "Ingstray"
print(pig_latin("Alphabet"))        # "Alphabetay"
print(pig_latin("yay"))             # "yayay"
print("________________________")
""" Problem 2: pig_latin_sentence

Given a sentence, pig-latin-ify it. That is, pig-latin-ify each word, then put them back into a sentence.
You can assume that there will be no punctuation, and that there will be exactly one space between words.
However, you must maintain the original case (upper vs. lower) of each word in the sentence.

"""

def pig_latin_sentence(s):
    words = s.split(" ")
    piglatin = []
    finalpig = ''
    for word in words:
        pig_latin(word)
        piglatin += [pig_latin(word)]

    for element in piglatin:
        
        str(element)
        finalpig += str(element) + " "
        
        finalpig = finalpig[0:len(s) - 1]

        #find a way to make capital and lowercase letters work
    


    


    
    return(finalpig)

print(pig_latin_sentence("hello world"))                                # "ellohay orldway"
print(pig_latin_sentence("python is fun"))                              # "ythonpay isay unfay"
print(pig_latin_sentence("Hello World"))                                # "Ellohay Orldway"
print(pig_latin_sentence("Very strange"))                               # "Eryvay angestray"
print("___________________________")
""" Problem 3: de_pig_latin

Given a string s, return a list of all possible strings that pig-latin-ify to s.
Again, maintain the proper case. Your list may have the candidate strings in any order.

"""






def de_pig_latin(s):
   
    
    
    
    
    s = s[0:len(s) - 2]
    delatinified = [s]
    while s[len(s) - 1] not in "AEIOUYaeiouy":
        notlastletter = s[0:len(s) - 1]
        lastletter = s[len(s) - 1]
        s = lastletter + notlastletter
        delatinified += [s]
        
        
        
       
    
       
        
        #remove ay (done)
       #loop backwards through word, remove last letter and add it to front, add that word to a list, rinse and repeat until the last letter is a vowel
   
       




   
    return(delatinified)

print(de_pig_latin("ellohay"))           # ["hello", "elloh"]
print(de_pig_latin("orldway"))           # ["orldw", "world", "dworl", "ldwor", "rldwo"]
print(de_pig_latin("Ingstray"))          # ["Ingstray", "Ringst", "Trings", "String", "Gstrin", "Ngstri"]
print(de_pig_latin("Alphabetay"))        # ["Alphabet", "Talphabe"]
print(de_pig_latin("yayay"))             # ["yay"]
print("______________")
""" Problem 4: de_pig_latin_sentence

Give a pig-latin-ified sentence, de-pig-latin-ify it. You may choose ANY candidate sentence to return.
Again, assume there is no punctuation, and that spacing is consistent.

"""

def de_pig_latin_sentence(s):
    words = s.split(" ")
    english = []
    finaleng = ''
    for word in words:
        de_pig_latin(word)
        english += [de_pig_latin(word)[0]]

    for element in english:
        
        str(element)
        finaleng += str(element) + " "
        finaleng = finaleng[0:len(s) - 1]
    return(finaleng)

print(de_pig_latin_sentence("ellohay orldway"))                         # "hello world" or "elloh dworl" or...
print(de_pig_latin_sentence("odingcay isay unfay"))                     # "coding is fun" or "ngcodi si nfu" or...
print("_________________")

""" Problem 5: de_pig_latin_sentence_count and de_pig_latin_sentence_list [BONUS!]

Give a pig-latin-ified sentence, count how many possible sentences it can de-pig-latin-ify to.
Also, return a list (in any order) with all possible sentences it can de-pig-latin-ify to.


"""
def de_pig_latin_sentence_count(s):

    return()
print(de_pig_latin_sentence_count("ellohay orldway"))                           # 10
print(de_pig_latin_sentence_count("odingcay isay unfay"))                       # 24


def de_pig_latin_sentence_list(s):
    return()
print(de_pig_latin_sentence_list("youay anday iay"))                            # ["you and i", "you dan i", "you nda i"]
print(de_pig_latin_sentence_list("ehay umpsjay"))                               # ["he umpsj", "eh umpsj", 
                                                                                # "he jumps", "eh jumps", 
                                                                                # "he sjump", "eh sjump", 
                                                                                # "he psjum", "eh psjum", 
                                                                                # "he mpsju", "eh mpsju"]
