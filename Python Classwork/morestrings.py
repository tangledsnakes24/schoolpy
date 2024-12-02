
def shrink(s):
    new_s = ""
    for index in range(len(s)):
        if s[index] != s[index - 1]:
            new_s += s[index]
            
    return()

print(shrink("AAAABBCCCCCCD")    #"ABCD"
print(shrink("ABCD")

print(shrink("hello"))          # "helo"
print(shrink("yayyy"))          # "yay"
print(shrink("ooooo"))          # "o"

print(shrink("shrink"))         # "shrink"
print(shrink("banana"))         # "banana"

print(shrink(""))               # ""
print(shrink("a"))              # "a"
print(shrink("aa"))             # "a"


def destroy(s):
    return()

print(destroy("k!ablam"))       # "blam"
print(destroy("st!rings"))      # "sings"
print(destroy("destroy"))       # "destroy"

print(destroy("boom!"))         # "boo"
print(destroy("!fwoosh"))       # "woosh"
print(destroy("!tnt!"))         # "n"

print(destroy("!"))             # ""
print(destroy("!!"))            # ""
print(destroy("!a!"))           # ""
