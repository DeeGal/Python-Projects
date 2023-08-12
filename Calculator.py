
num1 = float(input("Enter the first number: "))
opp = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if opp == "+":
    print(num1 + num2)
elif opp == "-":
    print(num1 - num2)
elif opp == "/":
    print(num1 / num2)
elif opp == "*":
    print(num1 * num2)
else:
    print("Entered an invalid operator.")
