#helperfunction
def even_helper(n):
    if (n % 2 == 1):
        return(0)
    else:
        return(n)

print(even_helper(3))
print(even_helper(2))
print("++++++++")

def add_evens(x, y, z):
    x = even_helper(x)
    y = even_helper(y)
    z = even_helper(z)
    return(x + y + z)

print(add_evens(1, 3, 4))
print(add_evens(5, 6, 2))
print(add_evens(1, 2, 3))

def triangular(n):
    counter = 0
    for number in range(1, n+1):
        counter += number
    return(counter)
print(triangular(5))
print(triangular(6))
print("------")
def alternating_sum(x):
    counter1 = 0
    for number1 in range(1, x+1):
        if (number1 % 2 == 0):
            counter1 -= number1
        else:
            counter1 += number1
    return(counter1)
print(alternating_sum(5))
print(alternating_sum(9))
print(alternating_sum(12))
print(alternating_sum(4))
print("---------")




def wiredsums2(n, pos_count2):
    counter3 = 0
    for number in range(1, n + 1):
            if (n % (pos_count2 + 1) == 0):
                counter3 -= number
            else:
                counter3 += number
    return(number)


print(wiredsums2(6, 2))
print(wiredsums2(7, 2))
print(wiredsums2(4, 8))
print(wiredsums2(15, 5))

print("----------")
def morewierdsums(n):
    counter4 = 0
    for number in range(1, n+1):
        if(number % 4) == 1 or (number % 4) == 2:
            counter4 = counter4 + number
        if(number % 4) == 3 or (number % 4) == 0:
            counter4 = counter4 - number
    return(counter4)
print(morewierdsums(2))
print(morewierdsums(5))
print(morewierdsums(8))
print(morewierdsums(3))
print("----------------")
