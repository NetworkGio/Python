#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Please write a program which asks the user for an integer number. The program 
should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

Please type in a number: 2020

Please type in a number: 1984
Orwell

1. Write your solution here

"""
print("Excercise 1: Orwell")
print("\n")
number = int(input("Please type in a number:"))

if number == 1984:
    print("Orwell")


"""
2. Please write a program which asks the user for an integer number. If the 
number is less than zero, the program should print out the number multiplied 
by -1. Otherwise the program prints out the number as is. Please have a look 
at the examples of expected behaviour below.

Please type in a number: -7
The absolute value of this number is 7

Please type in a number: 1
The absolute value of this number is 1

Please type in a number: -99
The absolute value of this number is 99
"""
print("Excercise 2: Absolute Value")
print("\n")
# Write your solution here
number = int(input("Please type in a number:"))

if number < 0:
    print(f"The absolute value of this number is {number * -1}")
else:
   print(f"The absolute value of this number is {number}")
   
"""
3. Please write a program which asks for the user's name. If the name is anything 
but "Jerry", the program then asks for the number of portions and prints out 
the total cost. The price of a single portion is 5.90.

Two examples of the program's execution:

Sample output
    Please tell me your name: Kramer
    How many portions of soup? 2
    The total cost is 11.8
    Next please!

Sample output
    Please tell me your name: Jerry
    Next please!
"""
print("Excercise 3: How many Portions of Soup")
print("\n")
# Write your solution here
name = str(input("Please tell me your name:"))

if name == "Jerry":
    print("Next please!")
else: 
    portion = int(input("How many portions of soup?"))
    print(f"The total cost is {5.90 * portion}")
    print("Next please!")


"""
4. Please write a program which asks the user for an integer number. The program 
should then print out the magnitude of the number according to the following 
examples.

Sample output
    Please type in a number: 950
    This number is smaller than 1000
    Thank you!

Sample output
    Please type in a number: 59
    This number is smaller than 1000
    This number is smaller than 100
    Thank you!

Sample output
    Please type in a number: 2
    This number is smaller than 1000
    This number is smaller than 100
    This number is smaller than 10
    Thank you!

Sample output
    Please type in a number: 1123
    Thank you!
"""
print("Excercise 4: Magnitude")
print("\n")
# Write your solution here
number = int(input("Please type in a number:"))

if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")

print("Thank you!")

"""
5. Please write a program which asks the user for two numbers and an operation. 
If the operation is add, multiply or subtract, the program should calculate 
and print out the result of the operation with the given numbers. If the user 
types in anything else, the program should print out nothing.

Some examples of expected behaviour:

Sample output
    Number 1: 10
    Number 2: 17
    Operation: add

        10 + 17 = 27

Sample output
    Number 1: 4
    Number 2: 6
    Operation: multiply

        4 * 6 = 24

Sample output
    Number 1: 4
    Number 2: 6
    Operation: subtract

        4 - 6 = -2
"""
print("Excercise 5: Calculator")
print("\n")

# Write your solution here
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
operation = str(input("Operation:"))

if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}")
elif operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")
elif operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")
    
"""
6. Please write a program which asks the user for a temperature in degrees 
Fahrenheit, and then prints out the same in degrees Celsius. If the converted 
temperature falls below zero degrees Celsius, the program should also print 
out "Brr! It's cold in here!".

The formula for converting degrees Fahrenheit to degrees Celsius can be found 
easily by any search engine of your choice.

Two examples of expected behaviour:

Sample output
    Please type in a temperature (F): 101
    101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

Please type in a temperature (F): 21
    21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
    Brr! It's cold in here!
"""
print("Excercise 6: Temperature")
print("\n")
# Write your solution here
user_temp = int(input("Please type in a temperature (F):"))
temperature = (user_temp - 32) * 5 / 9

if temperature >= 0.0:
    print(f"{user_temp} degrees Fahrenheit equals {temperature} degrees Celsius")
else:
    print(f"{user_temp} degrees Fahrenheit equals {temperature} degrees Celsius\nBrr! It's cold in here!")

"""
7. Please write a program which asks for the hourly wage, hours worked, and 
the day of the week. The program should then print out the daily wages, which 
equal hourly wage multiplied by hours worked, except on Sundays when the hourly 
wage is doubled.

Sample output
    Hourly wage: 8.5
    Hours worked: 3
    Day of the week: Monday
    Daily wages: 25.5 euros

Sample output
    Hourly wage: 12.5
    Hours worked: 10
    Day of the week: Sunday
    Daily wages: 250.0 euros
"""
print("Excercise 7: Daily Wages")
print("\n")
# Write your solution here
hourly_wage = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
day_of_the_week = str(input("Day of the week:"))
daily_wages = hourly_wage * hours_worked

if day_of_the_week != "Sunday":
    print(f"Daily wages: {daily_wages} euros")
else:
    daily_wages *= 2
    print(f"Daily wages: {daily_wages} euros")
    
"""
8. Loyalty Bonus: This program calculates the end of year bonus a customer 
receives on their loyalty card. The bonus is calculated with the following 
formula:

If there are less than a hundred points on the card, the bonus is 10 %
In any other case the bonus is 15 %
The program should work like this:

 Sample output:
        How many points are on your card? 55
        Your bonus is 10 %
        You now have 60.5 points

But there is a problem with the program, so with some inputs it doesn't work 
quite right:

Sample output:
    How many points are on your card? 95
    Your bonus is 10 %
    Your bonus is 15 %
    You now have 120.175 points
"""
print("Excercise 8: Loyalty Bonus")
print("\n")
# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
else:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

"""
9. What to wear tomorrow


Please write a program which asks for tomorrow's weather forecast and then 
suggests weather-appropriate clothing.

The suggestion should change if the temperature (measured in degrees Celsius) 
is over 20, 10 or 5 degrees, and also if there is rain on the radar.

Some examples of expected behaviour:

Sample output
    What is the weather forecast for tomorrow?
    Temperature: 21
    Will it rain (yes/no): no
    Wear jeans and a T-shirt

Sample output
    What is the weather forecast for tomorrow?
    Temperature: 11
    Will it rain (yes/no): no
    Wear jeans and a T-shirt
    I recommend a jumper as well

Sample output
    What is the weather forecast for tomorrow?
    Temperature: 7
    Will it rain (yes/no): no
    Wear jeans and a T-shirt
    I recommend a jumper as well
    Take a jacket with you

Sample output
    What is the weather forecast for tomorrow?
    Temperature: 3
    Will it rain (yes/no): yes
    Wear jeans and a T-shirt
    I recommend a jumper as well
    Take a jacket with you
    Make it a warm coat, actually
    I think gloves are in order
    Don't forget your umbrella!
"""
print("Excercise 9: What to wear tomorrow")
print("\n")
# Write your solution here
print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature:"))
is_raining = str(input("Will it rain (yes/no):"))

print("Wear jeans and a T-shirt")

if temperature <= 20:
    print("I recommend a jumper as well")

if temperature <= 10:
    print("Take a jacket with you")


if temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if is_raining == "yes":
    print("Don't forget your umbrella!")
    
"""
10. Solving a quadratic equation


In the Python math module there is the function sqrt, which calculates the 
square root of a number. You can use it like so:

from math import sqrt

print(sqrt(9))
This should print out

Sample output
    3.0

We will return to the concept of a module and the import statement later. 
For now, it is sufficient to understand that the line from math import sqrt 
allows us to use the sqrt function in our program.

Please write a program for solving a quadratic equation of the form ax²+bx+c. 
The program asks for values a, b and c. It should then use the quadratic 
formula to solve the equation. The quadratic formula expressed with the Python
 sqrt function is as follows:

x = (-b ± sqrt(b²-4ac))/(2a).

You can assume the equation will always have two real roots, so the above f
ormula will always work.

An example of expected behaviour:

Sample output
    Value of a: 1
    Value of b: 2
    Value of c: -8
    
    The roots are 2.0 and -4.0
"""
print("Excercise 10: Solving a quadratic equation")
print("\n")

# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))

# Positive part of the equation
x1 = (-b + sqrt((b ** 2) - (4 * a * c)) ) / (2 * a)
# Negative part of the equation
x2 = (-b - sqrt((b ** 2) - (4 * a * c)) ) / (2 * a)

print(f"The roots are {x1} and {x2}")










































