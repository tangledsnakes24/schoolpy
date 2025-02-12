""" Favorite Things """

math_dept_faves = {"mr. gold": ["math", "coding", "cats", "dogs"],
                   "mr. letarte": ["math", "cooking", "cats"],
                   "ms. moss": ["math", "set design", "cats"],
                   "mr. sherry": ["math", "camping", "singing"],
                   "mr. singer": ["coding", "movies", "yoga", "cats", "math"],
                   "mr. paul": ["math", "dogs", "physics"]}

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

# Problem 1: Who Loves

def who_loves(d, item):
    return()

print("Testing Problem 1: Who Loves")
print(who_loves(math_dept_faves, "cats"))           # ["mr. gold", "mr. letarte", "ms. moss", "mr. singer"]
print(who_loves(math_dept_faves, "coding"))         # ["mr. gold", "mr. sherry"]
print(who_loves(math_dept_faves, "set design"))     # ["ms. moss"]
print(who_loves(math_dept_faves, "hamsters"))       # []

print(who_loves(dog_faves, "naps"))         # ["lincoln", "peanut", "prince", "bella"]
print(who_loves(dog_faves, "rabbits"))      # ["peanut"]
print(who_loves(dog_faves, "walks"))        # ["peanut", "bella"]
print(who_loves(dog_faves, "baths"))        # []
print()

# Problem 2: Get All Faves

def get_all_faves(d):
    return()

print("Testing Problem 2: Get All Faves")
print(get_all_faves(dog_favs))          # ["tummy rubs", "naps", "walks", "rabbits", "growling"]
print(get_all_faves(cat_favs))          # ["scratching", "springs", "naps", "milk"]
print()

# Problem 3: Loved by All

def loved_by_all(d):
    return()

print("Testing Problem 3: Loved By All")
print(loved_by_all(math_dept_faves))            # ["math"]
print(loved_by_all(dog_favs))                   # ["naps", "walks"]
print(loved_by_all(cat_favs))                   # []
print()

# Problem 4: Most Adored

def most_adored(d):
    return()

print("Testing Problem 4: Most Adored")
print(most_adored(math_dept_faves))         # ["math"]
print(most_adored(cat_faves))               # ["naps", "springs"]
print(most_adored(dog_faves))               # ["naps", "walks"]
