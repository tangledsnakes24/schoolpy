# Day 3: Fav Things Quiz

math_dept_faves = {"gold": ["math", "coding", "cats", "dogs"],
                   "letarte": ["math", "cooking", "cats"],
                   "moss": ["math", "set design", "cats"],
                   "sherry": ["math", "camping", "singing"],
                   "singer": ["coding", "movies", "yoga", "cats", "math"],
                   "paul": ["math", "dogs", "physics"]}

cat_faves = {"astrid": ["scratching", "springs", "naps"],
             "gizmo": ["milk", "naps"],
             "yvie": ["naps", "springs"],
             "chester": ["naps", "springs", "scratching"],
             "matzoh": ["naps"],
             "grumpy": []}
             
dog_faves = {"lincoln": ["tummy rubs", "naps", "walks"],
             "peanut": ["walks", "naps", "rabbits"],
             "prince": ["tummy rubs", "naps", "growling", "walks"],
             "bella": ["naps", "walks", "tummy rubs"]}

""" Problem 1: Common Interests
Write a function to determine two people's common interests.

That is, given two people, return a list of all the likes they have in common.

[Note: The returned list may be in any order.] 
"""

def common_interests(d, person1, person2):
    return()

print(common_interests(math_dept_faves, "gold", "letarte"))     # ["math", "cats"]

print(common_interests(cat_faves, "yvie", "matzoh"))    # ["naps"]
print(common_interests(cat_faves, "astrid", "chester")) # ["scratching", "springs", "naps"]
print(common_interests(cat_faves, "astrid", "grumpy"))  # []

print(common_interests(dog_faves, "lincoln", "bella"))  # ["tummy rubs", "naps", "walks"]
print(common_interests(dog_faves, "bella", "lincoln"))  # ["tummy rubs", "naps", "walks"]



""" Problem 2: Most Similar
Write a function that determines which people are "most similar" to a given person.

To figure out how similar two people are, simply count their common interests.
The "most similar" people are those with the most common interests.

[Note: It is possible that someone has no common interests with anyone, in which case
       they are most similar to everybody! See "Grumpy" for an example.]
       
[Note: The returned list may be in any order.] 
"""

def most_similar(d, person):
    return()

print(most_similar(math_dept_faves, "letarte")) # ["gold", "moss", "singer"]
print(most_similar(math_dept_faves, "paul"))    # ["gold"]

print(most_similar(cat_faves, "astrid"))    # ["chester"]
print(most_similar(cat_faves, "gizmo"))     # ["astrid", "yvie", "chester", "matzoh"]
print(most_similar(cat_faves, "yvie"))      # ["astrid", "chester"]
print(most_similar(cat_faves, "grumpy"))    # ["astrid", "gizmo", "yvie", "chester", "matzoh"]
