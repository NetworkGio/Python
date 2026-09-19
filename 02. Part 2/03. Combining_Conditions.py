#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 20:41:35 2026

@author: junio]



1. Age Check


Please write a program which asks for the user's age. If the age is not plausible, 
that is, it is under 5 or something that can't be an actual human age, the program 
should print out a comment.

Have a look at the examples of expected behaviour below to figure out which comment 
is applicable in each case.

Sample output
What is your age? 13
Ok, you're 13 years old

Sample output
What is your age? 2
I suspect you can't write quite yet...

Sample output
What is your age? -4
That must be a mistake
"""

userAge = int(input("What is your age?"))
    
if (userAge >= 5):
    print(f"Ok, you're {userAge} years old")
elif (userAge >= 0 and userAge < 5):
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")
    
"""
2. Newphews


Please write a program which asks for the user's name. If the name is Huey, 
Dewey or Louie, the program should recognise the user as one of Donald Duck's 
nephews.

In a similar fashion, if the name is Morty or Ferdie, the program should recognise 
the user as one of Mickey Mouse's nephews.

Some examples:

Sample output
Please type in your name: Morty
I think you might be one of Mickey Mouse's nephews.

Sample output
Please type in your name: Huey
I think you might be one of Donald Duck's nephews.

Sample output
Please type in your name: Ken
You're not a nephew of any character I know of.
"""
    
userName = str(input("Please type in your name:"))

if (userName == "Huey" or userName == "Dewey" or userName == "Louie"):
    print("I think you might be one of Donald Duck's nephews.")
elif (userName == "Morty" or userName == "Ferdie"):
   print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")


"""
3. Grades and points

The table below outlines the grade boundaries on a certain university course. 
Please write a program which asks for the amount of points received and then 
prints out the grade attained according to the table.

        points	grade
        < 0	impossible!
        0-49	fail
        50-59	1
        60-69	2
        70-79	3
        80-89	4
        90-100	5
        > 100	impossible!
        
Some examples:

Sample output
How many points [0-100]: 37
Grade: fail

Sample output
How many points [0-100]: 76
Grade: 3

Sample output
How many points [0-100]: -3
Grade: impossible!
"""
# Write your solution here

userPoints = int(input("How many points [0-100]:"))

if (userPoints < 0 or userPoints > 100):
    print("Grade: impossible!")
elif (userPoints >= 0 and userPoints <= 49):
    print("Grade: fail")
elif (userPoints >= 50 and userPoints <= 59):
    print("Grade: 1")
elif (userPoints >= 60 and userPoints <= 69):
    print("Grade: 2")
elif (userPoints >= 70 and userPoints <= 79):
    print("Grade: 3")
elif (userPoints >= 80 and userPoints <= 89):
    print("Grade: 4")
elif (userPoints >= 90 and userPoints <= 100):
    print("Grade: 5")
    
"""
4. FizzBuzz

Please write a program which asks the user for an integer number. If the number 
is divisible by three, the program should print out Fizz. If the number is 
divisible by five, the program should print out Buzz. If the number is divisible 
by both three and five, the program should print out FizzBuzz.

Some examples of expected behaviour:

Sample output
Number: 9
Fizz

Sample output
Number: 7

Sample output
Number: 20
Buzz

Sample output
Number: 45
FizzBuzz

"""
userNumber = int(input("Number: "))

if (userNumber % 3 == 0 and userNumber % 5 == 0):
    print("FizzBuzz")
elif (userNumber % 3 == 0):
    print("Fizz")
elif (userNumber % 5 == 0):
    print("Buzz")
    
"""
5. Leap Year

Generally, any year that is divisible by four is a leap year. However, if the 
year is additionally divisible by 100, it is a leap year only if it also divisible 
by 400.

Please write a program which asks the user for a year, and then prints out 
whether that year is a leap year or not.

Some examples:

Sample output
Please type in a year: 2011
That year is not a leap year.

Sample output
Please type in a year: 2020
That year is a leap year.

Sample output
Please type in a year: 1800
That year is not a leap year.
"""

userYear = int(input("Please type in a year:"))
    
if (userYear % 400 == 0):
    print("That year is a leap year")
elif (userYear % 100 == 0):
    print("That year is not a leap year")
elif (userYear % 4 == 0):
    print("That year is a leap year")
else:
    print("That is not a leap year")
    
    
"""
6. Alphabetically in the middle


Please write a program which asks the user for three letters. The program 
should then print out whichever of the three letters would be in the middle 
if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

Sample output
1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output
1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B


"""
    
userLetter1 = input("1st letter:")
userLetter2 = input("2nd letter:")
userLetter3 = input("3rd letter:")

if ((userLetter1 < userLetter2 and userLetter1 > userLetter3) or (userLetter1 > userLetter2 and userLetter1 < userLetter3)):
    print(f"The letter in the middle is {userLetter1}")
elif ((userLetter2 < userLetter1 and userLetter2 > userLetter3) or (userLetter2 > userLetter1 and userLetter2 < userLetter3)):
    print(f"The letter in the middle is {userLetter2}")
elif ((userLetter3 < userLetter1 and userLetter3 > userLetter2) or (userLetter3 > userLetter1 and userLetter3 < userLetter2)):
    print(f"The letter in the middle is {userLetter3}")
    

"""
7. Gift tax calculator

Some say paying taxes makes Finns happy, so let's see if the secret of happiness 
lies in one of the taxes set out in Finnish tax code.

According to the Finnish Tax Administration, a gift is a transfer of property 
to another person against no compensation or payment. If the total value of the 
gifts you receive from the same donor in the course of 3 years is €5,000 or more, 
you must pay gift tax.

When the gift is received from a close relative or a family member, the amount 
of tax to be paid is determined by the following table, which is also available 
on this website:

Value of gift	Tax at the lower limit	Tax rate for the exceeding part (%)
5 000 — 25 000	100	8
25 000 — 55 000	1 700	10
55 000 — 200 000	4 700	12
200 000 — 1 000 000	22 100	15
1 000 000 —	142 100	17
So, for a gift of 6 000 euros the recipient pays a tax of 180 euros 
(100 + (6 000 - 5 000) * 0.08). Similarly, for a gift of 75 000 euros the 
recipient pays a tax of 7 100 euros (4 700 + (75 000 - 55 000) * 0.12).

Please write a program which calculates the correct amount of tax for a gift 
from a close relative. Have a look at the examples below to see what is expected. 
Notice the lack of thousands separators in the input values - you may assume there 
will be no spaces or other thousands separators in the numbers in the input, as 
we haven't yet covered dealing with these.

Sample output
Value of gift: 3500
No tax!

Sample output
Value of gift: 5000
Amount of tax: 100.0 euros

Sample output
Value of gift: 27500
Amount of tax: 1950.0 euros

"""
    
valueOfGift = float(input("Value of digt: "))
tax = 0


if (valueOfGift >= 5000 and valueOfGift < 25000):
   tax = 100 + (valueOfGift - 5000) * 0.08
   print(f"Amount of tax: {tax} euros")
elif (valueOfGift >= 25000 and valueOfGift < 55000):
    tax = 1700 + (valueOfGift - 25000) * 0.10
    print(f"Amount of tax: {tax} euros")
elif (valueOfGift >= 55000 and valueOfGift < 200000):
    tax = 4700 + (valueOfGift - 55000) * 0.12
    print(f"Amount of tax: {tax} euros")
elif (valueOfGift >= 200000 and valueOfGift < 1000000):
    tax = 22100 + (valueOfGift - 200000) * 0.15
    print(f"Amount of tax: {tax} euros")
elif (valueOfGift >= 1000000):
    tax = 142100 + (valueOfGift - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")
else:
    print("No tax!")
    


   












    