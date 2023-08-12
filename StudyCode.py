
print("Hello!")

years = 2022
age = int(input("Enter your age: "))
result = int(years) - age
print("You were born " + str(result) + " !")

course = input("What is the name of your course? ")
print(course.upper())

Days_Week = 'There are 7 days in a week'
print(Days_Week.replace('7', 'seven'))
print('week' in Days_Week)

print(5 + 2)
print(45 - 5)
print(60 % 3)
print(20 * 5)
print(100 / 2)
print(2 ** 4)

x = 4 == 2
print(x)

price = 50
print(20 < price < 100)
print(price < 30 or price < 35)

temperature = 40
result = int(input("Enter temperature: "))

if result > temperature:
    print("Its above 40 degrees today, so don't forget your water and a cap.")
elif result < temperature:
    print("Its below 40 degrees today, so don't forget your jersey. ")
else:
    print("Invalid value but Enjoy your day!!")

weight = float(input('Weight: '))
unit = input("Kg or Lbs: ")

if unit.upper() == 'K':
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print('Weight in Kg: ' + str(converted))

i = 1
while i <= 3:
    print(str(i) + ' Only chances available.')
    i += 1

days_Of_Week = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']
print(days_Of_Week[0:4])

days_Of_Week.append('Sun')
print(days_Of_Week)

days_Of_Week[2] = 'Feb'
print(days_Of_Week)

days_Of_Week.remove('Feb')
print(days_Of_Week)
print(3 in days_Of_Week)
print(len(days_Of_Week))

for day in days_Of_Week:
    print(days_Of_Week)

i = 0
while i < len(days_Of_Week):
    print(days_Of_Week[i])
    i = i + 1

numbers = range(4, 10)
for ran in numbers:
    print(ran)
for powers in numbers:
    print(pow(5, 3))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Operator: ")
if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print("Invalid math operator!")

days_Of_Week.extend(numbers)
print(days_Of_Week)


def greetings(name):
    print("Hello!" + name)


greetings('Diana')


def cube(numb):
    return numb * numb * numb


print(cube(9))


def max_number(numb1, numb2, numb3):
    if numb2 < numb1 > numb3:
        return numb1
    elif numb2 < numb3 > numb1:
        return numb3
    else:
        return numb2


print(max_number(5, 8, 9))


monthConversions = {
    'jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'Ma': 'May'
}
print(monthConversions['Apr'])
print(monthConversions.get('Feb'))

secret_word = 'Worship_God'
secret = " "
limit = 3
i = 0
out_of_guess = False

while secret != secret_word and not out_of_guess:
    if i < limit:
        secret = input('Enter a guess: ')
        i += 1
    else:
        out_of_guess = True
        print('Out of Guess, You Lose!')

try:
    no_numbers = int(input("Enter your favourite number: "))
    print(no_numbers)
except ValueError as err:
    print(err)
