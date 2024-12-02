""" Hello World! """



""" Basic Data Types """

integer = 3
string = "THIS IS A STRING"

""" Math """

x = 3
y = 4

x_plus_y = x+y
x_minus_y = x-7
x_times_y = x*y
x_over_y = x/y

x_to_the_y = x**y
#mod is the remainder when I devide
x_mod = x%y

#to find even and odd numbers, just use (number)mod 2
""" Functions with Integers """
print("double-and-add-one")
def double_and_add_one(x):
    
    return(2*x+1) #here is the output
#tests
print(double_and_add_one(0))   
print(double_and_add_one(1))  
print(double_and_add_one(2)) 
print(double_and_add_one(3))

def add_one_and_double(x):
    
    return((x+1)*2) #output goes here
print("add-one-and-double")
# TESTS GO HERE
print(add_one_and_double(0))
print(add_one_and_double(1))
print(add_one_and_double(2))
print(add_one_and_double(3))


print("add-one-and-double-5-times")
def add_one_and_double_5_times(x):
    x = add_one_and_double(x)
    x = add_one_and_double(x)
    x = add_one_and_double(x)
    x = add_one_and_double(x)
    x = add_one_and_double(x)
    return(x)
print(add_one_and_double_5_times(0))
print("running mystery function/square-and-sub-one")
def square_and_sub_1(x):
    x = x*x
    x = x - 1
    return(x)
print(square_and_sub_1(1))
print(square_and_sub_1(2))
print(square_and_sub_1(3))
print(square_and_sub_1(4))