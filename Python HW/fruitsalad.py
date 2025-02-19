""" Day 1 Homework: Fruit Salads """

salad1 = {"apple": 20,
          "banana": 30}

salad2 = {"cherry": 100}

salad3 = {"apple": 1,
          "banana": 1,
          "cherry": 1,
          "dates": 1}

salad4 = {"cherry": 30,
          "elderberry": 20}


salad5 = {"cherry": 30,
          "bannana": 199,
          "apple": 2
          }

salad6 = {"kale": 10,
          "lettuce": 350,
          "tobacco": 50
          }
# Problem 1: Total Cost

def total_cost(prices, recipe):
    cost = 0
    for ingredient in recipe:
        price = prices[ingredient]
        quantity = recipe[ingredient]
        cost += price * quantity
    return(cost)

prices = {"apple": 3,
          "banana": 2,
          "cherry": 4,
          "dates": 5,
          "elderberry": 6}
print("running total cost")
print(total_cost(prices, salad1))       # 120 (20 * 3 + 30 * 2)
print(total_cost(prices, salad2))       # 400 (100 * 4)
print(total_cost(prices, salad3))       # 14 (3 + 2 + 4 + 5)
print(total_cost(prices, salad4))       # 240 (30 * 4 + 20 * 6)

# Problem 2: Makeable

pantry = {"apple": 40,
          "banana": 50,
          "cherry": 20,
          "dates": 70,
          "elderberry": 0}

def makeable(pantry, recipe):
    for ingredient in recipe:
        if ingredient in pantry:
            if pantry[ingredient] < recipe[ingredient]:
                #print("not enough " + ingredient)
                return(False)
        else:
            #print(ingredient + "not even in pantry!")
            return(False)
            

    
    return(True)

print(makeable(pantry, salad1))       # True
print(makeable(pantry, salad2))       # False (not enough cherries)
print(makeable(pantry, salad3))       # True
print(makeable(pantry, salad4))       # False (not enough cherries or elderberries)
print(makeable(pantry, salad5))       #false
print(makeable(pantry, salad6))       #false  
# Problem 3: Batches

def batches(pantry, recipe):
    l = []
    for ingredient in recipe:

        if ingredient in pantry:
            b = int(pantry[ingredient] / recipe[ingredient])
            l = l + [b]

        else:
            l += [0]
    return(min(l))

print(batches(pantry, salad1))       # 1 (enough apples for 2, but not enough bananas)
print(batches(pantry, salad2))       # 0 (not enough cherries)
print(batches(pantry, salad3))       # 20 (limited by cherries)
print(batches(pantry, salad4))       # 0 (not enough cherries or elderberries)
