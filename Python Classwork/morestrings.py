
def shrink(s):
    new_s = ""
    for index in range(len(s)):
        if index == 0 or s[index] != s[index - 1]:
            new_s += s[index]
            
    return(new_s)

print(shrink("AAAABBCCCCCCD"))    #"ABCD"
print(shrink("ABCD"))

print(shrink("hello"))          # "helo"
print(shrink("yayyy"))          # "yay"
print(shrink("ooooo"))          # "o"

print(shrink("shrink"))         # "shrink"
print(shrink("banana"))         # "banana"

print(shrink(""))               # ""
print(shrink("a"))              # "a"
print(shrink("aa"))             # "a"


def destroy(s):
    new_s = ""
    for index in range(len(s)):
        

        if index == 0:
            substr = s[0 : 2]


        elif index == len(s) - 1:
            substr = s[index - 1 : len(s)]

        else:
            substr = s[index - 1: index + 2]

        if "!" not in substr:
            new_s += s[index]
        
    
    return(new_s)

print(destroy("k!ablam"))       # "blam"
print(destroy("st!rings"))      # "sings"
print(destroy("destroy"))       # "destroy"

print(destroy("boom!"))         # "boo"
print(destroy("!fwoosh"))       # "woosh"
print(destroy("!tnt!"))         # "n"

print(destroy("!"))             # ""
print(destroy("!!"))            # ""
print(destroy("!a!"))           # ""
