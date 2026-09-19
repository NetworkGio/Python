#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 19:48:04 2026

@author: junio

1. Age of maturity

Please write a program which asks the user for their age. The program should 
then print out a message based on whether the user is of age or not, using 18 
as the age of maturity.

Some examples of expected behaviour:

Sample output
How old are you? 12
You are not of age!

Sample output
How old are you? 32
You are of age!
"""

age = int(input("How old are you?"))

if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")


"""
2. Greater than or equal to

Please write a program which asks for two integer numbers. The program should 
then print out whichever is greater. If the numbers are equal, the program 
should print a different message.

Some examples of expected behaviour:

Sample output
Please type in the first number: 5
Please type in another number: 3
The greater number was: 5

Sample output
Please type in the first number: 5
Please type in another number: 8
The greater number was: 8

Sample output
Please type in the first number: 5
Please type in another number: 5
The numbers are equal!
"""

userNumber1 = int(input("Please type in the first number:"))
userNumber2 = int(input("Please type in the first number:"))

if userNumber1 > userNumber2:
    print(f"The greater number was: {userNumber1}")
elif userNumber2 > userNumber1:
     print(f"The greater number was: {userNumber2}")
elif userNumber1 == userNumber2:
    print("The numbers are equal")

"""
3. The elder

Please write a program which asks for the names and ages of two persons. The 
program should then print out the name of the elder.

Some examples of expected behaviour:

Sample output
Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada

Sample output
Person 1:
Name: Bill
Age: 1
Person 2:
Name: Jean
Age: 1
Bill and Jean are the same age
"""

userName1 = input("Name:")
userAge1 = int(input("Age:"))

userName2 = input("Name:")
userAge2 = int(input("Age:"))

if userAge1 > userAge2:
    print(f"The elder is {userName1}")
elif userAge2 > userAge1:
    print(f"The elder is {userName2}")
else:
    print(f"{userName1} and {userName2} are the same age")
    
"""
4. Alphabetically last

Python comparison operators can also be used on strings. String a is smaller 
than string b if it comes alphabetically before b. Notice however that the 
comparison is only reliable if

the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
only the standard English alphabet of a to z, or A to Z, is used.
Please write a program which asks the user for two words. The program should 
then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Some examples of expected behaviour:

Sample output
Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last.

Sample output
Please type in the 1st word: zorro
Please type in the 2nd word: batman
zorro comes alphabetically last.

Sample output
Please type in the 1st word: python
Please type in the 2nd word: python
You gave the same word twice.
"""

userWord1 = input("Please type in the 1st word:")
userWord2 = input("Please type in the 2nd word:")

if userWord1 > userWord2:
    print(f"{userWord1} comes alphabetically last.")
elif userWord2 > userWord1:
    print(f"{userWord2} comes alphabetically last.")
else:
    print("You gave the same word twice.")




