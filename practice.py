 # from builtins import function

var = 30
print(var)
file = input("what is your number: ")
print(file + str(var))

# Variables: int(), float(), str(),bool()
# Arithmetic Operators: +, /, -, *, %, **(to power of)
# While loops and #iterative control

i = 0
while i < 10:
    print(i)
    i += 1  
    
# 2D
number_grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
for row in number_grid:
    print(row)
    print(number_grid.pop([0][2]))
    
# Controls:
# Sequential control
print("Hello honourable member")
print("What is your name?")

# Selection control
var_3 = int(input("Enter a number: "))
if var_3 > 10:
    print("Your value is greater than 10" + str(var_3))

elif var < 10:
    print("Your value is less than 10" + str(var_3))

else:
    print("Enter a valid value")


# functions
def greet_me():
    print("Hi there")
    
    
greet_me()  


def greet(last_name, first_name):
    print(f"Hi {last_name} + {first_name}")
    print("Welcome")


greet("Diana", "Mudau")


def hi_there(name):
    print(f"Hi {name}")


hi_there("Sipho")


def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)


def multiply(* num):   # the * allows u to insert many values inside the function
    global total2
    for num2 in num:
        print(num2)
        for num_2 in num:
            total2 = 1
            total2 *= num_2
        return total2


multiply(2, 3, 4, 5, 6)


def save_user(**user):
    print(user)
    
    
save_user(id=1, name="John", age="30")


# scope and global
message = "a"


def great(name2):
    global message
    message = "b"
    
 
great("Charity")
print(message)

 
def fizz_buzz(input_3):
    if (input_3 % 3 == 0) and (input_3 % 5 == 0):
        return "Fizz_Buzz"
    if input_3 % 3 == 0:
        return "Fizz"
    if input_3 % 5 == 0:
        return "Buzz"
    return input_3


print(fizz_buzz(3))


# BMI Calculator
name_1 = "YK"
height_m1 = 2
weight_kg1 = 90

name_2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name_3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m.__pow__(2))
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + "is not overweight."
    if bmi > 25:
        return name + "is overweight."

  
result1 = bmi_calculator(name_1, height_m1, weight_kg1)
result2 = bmi_calculator(name_2, height_m2, weight_kg2)
result3 = bmi_calculator(name_3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

# Recursive Functions
# function getFactorial(5):
    # factorial = 1
    # for x = 1 and x < 5:
       # factorial = factorial * x

# function getFactorial(n):
   #  if n> 2:
        # return 1
    # else:
        # return n * getFactorial(n-1)
import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0


def g_great():
    global i
    i += 1
    print("Hello", i)


g_great()

# 1D AND 2D arrays
import arrays as dm
ar_1 = dm.array([2, 4, 6, 8])
print(ar_1)

