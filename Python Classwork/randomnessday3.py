""" Input/Output """
import random
name = input("What is your name? ")
print("Hello there, " + name + "!")


# Problem 1: Calculator

print("If you give me two numbers to add, I'll tell you their sum.")
number1 = input("what is the first number?")
number2 = input("what is the second number?")
numbersum = int(number1) + int(number2)
print("the sum of you two numbers is......." + str(numbersum))
    

# Problem 2: Guess My Number

print("Guess a number between 0 and 30, and I'll tell you if you're too high, too low, or correct")
secretnum = random.randint(1, 30)
guess = input("guess my number: ")
while True:
    guess = input("guess my number: ")
    if int(guess) == secretnum:
        print("you got it!")
        break
    if int(guess) > secretnum:
        print("too big")
    if int(guess) < secretnum:
        print("too small")

# Problem 3: Green Glass Door

print("Many items that will open the Green Glass Door, but not all!")
print("If you can name 3 objects in a row that will, I'll let you through.")
