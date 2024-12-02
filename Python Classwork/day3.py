print("----------------------------")
print("the sum of numbers 1 to 10 is:")
for number in range(1, 101):
    print(number)
print("---------------------------")
total = 0
for number in range(1, 101):
    total = total + number
print(total)
print("---------------------------")
product = 1
for number in range(1, 11):
    product = product * number
print(product)
print("----------------------------")

# sum of all odds between 1 and 100
mysum = 0
for number in range(1, 101):
    if (number % 2) == 1:
        mysum = number + mysum
print(mysum)
print("----------------------------")
def triangular(n):
    triangular_sum = 0
    for i in range(1, n + 1):
        triangular_sum = triangular_sum + i
    return(triangular_sum)
print(triangular(3)) #6
print(triangular(5)) #15
print(triangular(6)) #21
print("----------------------------")




