#dictionary is very simular to list
#uses { instead of ]
#data is "a": 1, "b":2
#letter is key, number is value
#keys can be anything, values can be anything (more or less) keys cant be complex data(list dictionary etc)

#allowed to have same value for different key, but not same key for diff value
days = {5: "wed",
        6: "thurs",
        7: "fri",
        7: "blue",
        5: "purple",
        }
#to index into dictionary, use print(name[key or value]
print(days[7])



""" Day 1: Dictionaries """


# Updating Dictionaries
print("updating dictionaries")
days[4] = "tuesday"
days[3] = "monday"
print(days)


# Getting Keys and Values
print("getting keys and values")
d1 = {"A": 1, "B": 2, "C": 3}
d1.keys()
d1.values()
days ={5: "tuesday",
       6: "wednsday",
       7: "thursday",
       }
print(list(days.keys()))
print(list(days.values()))
# Looping over Dictionaries





# Problem 0: Get Highest


def get_highest(d):
    return()

print("Testing Problem 0: Get Highest...")

animals_ranked = {"cats": 10, "dogs": 10, "spiders": 0, "zebras": 2}
print(get_highest(animals_ranked))     # ["cats", "dogs"]

days_ranked = {"monday": 1, "tuesday": 1, "wednesday": 2, "thursday": 2, "friday": 3}
print(get_highest(days_ranked))        # ["friday"]

print()





# Problem 1: Modes

def modes(l):
    return()

print("Testing Problem 1: Modes...")

print(modes("AAAAAA B C D E"))      # ["A"]
print(modes("A B C D EEEEEE"))      # ["E"]

print(modes("aaaa"))            # ["A"]
print(modes("aAAA"))            # ["A"]
print(modes("aaAA"))            # ["a", "A"]
print(modes("aaaA"))            # ["a"]
print(modes("aaaa"))            # ["a"]

print(modes("AABCC"))           # ["A", "C"]
print(modes("ABCDE"))           # ["A", "B", "C", "D", "E"]
print()

# Problem 2: Digits to Words

def digits_to_words(n):
    return("")


print("Testing Problem 2: Digits to Words")
print(digits_to_words(1))           # "one"
print(digits_to_words(23))          # "two three"
print(digits_to_words(456))         # "four five six"
print()

# Problem 3: Taller Than


           
def taller_than(d, bound):
    return()

heights = {"J": 180,
           "K": 190,
           "L": 170,
           "M": 200,
           "N": 210,
           "O": 160}

print("Testing Problem 3: Taller Than")
print(taller_than(heights, 150))        # ["J", "K", "L", "M", "N", "O"]
print(taller_than(heights, 200))        # ["N"]
print(taller_than(heights, 250))        # []
print()

