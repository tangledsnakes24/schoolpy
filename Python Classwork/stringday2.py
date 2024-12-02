#string manipulation
s1 = "hello world"
#what we cant do:
#s[0] = "Y"
#print(s)

#what we can do:
new_s = ""
new_s = "Y" + s1[1:]
#what we cant do:
s = "i like dogs"
#s[7] = "B"
#print(s)

#What we can do:
new_s = s[:7] + "B" + s[8:]
print(new_s)


#upper and lower
s2 = "i like dogs"
s2 = s2.upper()
print(s2)
s3 = "I LIKE SCREAMING"
s3 = s3.lower()
print(s3)
""" Problem 1: Capitalize Vowels """

def cap_vowels(s):
    new_s = ""
    for index in range(len(s)):
        if s[index] in "aeiouy":
            cap = s[index].upper()
            new_s += cap
        else:
            new_s += s[index]
            
    return(new_s)

print(cap_vowels("abcdefg"))        # "AbcdEfg"
print(cap_vowels("AbcdEfg"))        # "AbcdEfg"
print(cap_vowels("aBCDeFG"))        # "ABCDEFG"


""" Problem 2: De-Double """

def de_double(s):
    new_s = ""
    for index in range(len(s)):
        if index == len(s) - 1:
            new_s = new_s + s[index]
        elif s[index] != s[index + 1]:
            new_s = new_s + s[index]

        
    
    return(new_s)

print(de_double("reed"))                # "red"
print(de_double("loop"))                # "lop"
print(de_double("tapped"))              # "taped"
print(de_double("pants"))               # "pants"
print(de_double("string"))              # "string"
print(de_double(""))                    #""
print(de_double("o"))                   #o

""" Problem 3: Split """
#s.split(char) is built in to do the same thing
def split(s, splitter):
    s = s + splitter
    l = []
    word = ""
    for character in s:
        if character == splitter:
            if word != "":
                l += [word]
            word = ""

        else:
            word += character
            

            
    
    return(l)

print(split("A.B.C.D", "."))                # ["A", "B", "C", "D"]
print(split("A.B.C.", "."))                 # ["A", "B", "C"]
print(split(".A.B.C", "."))                 # ["A", "B", "C"]

print(split("Hello World", " "))            # ["Hello", "World"]
print(split("Coding is Fun", "i"))          # ["Cod", "ng ", "s Fun"]
print(split("split", "z"))                  # ["split"]
