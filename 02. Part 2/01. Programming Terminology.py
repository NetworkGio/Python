#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 20:42:23 2026

@author: junio
"""

"""
1. Fix the syntax

The following program contains several syntactic errors. Please fix the program
so that the syntax is in order and the program works as specified by the examples 
below.

  number = input("Please type in a number: ")
  if number>100
    print("The number was greater than one hundred")
    number - 100
    print("Now its value has decreased by one hundred)
     print("Its value is now"+ number)
 print(number + " must be my lucky number!")
 print("Have a nice day!)
       
Sample Output: 
    Please type in a number: 13
    13 must be my lucky number!
    Have a nice day!

Sample Output:
    Please type in a number: 101
    The number was greater than one hundred
    Now its value has decreased by one hundred
    Its value is now 1
    1 must be my lucky number!
    Have a nice day!
"""

"""
# Fix the program
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number = number - 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")

print(f"{number} must be my lucky number!")
print("Have a nice day!")
"""

"""
2. Number of characters

The function len can be used to find out the length of a string, among other 
things. The function returns the number of characters in a string.

Some examples of how this works:
    
    word = "abcd"
    print(len(word))
    
    print(len("hi there"))
    
    word2 = "howdydoody"
    length = len(word2)
    print(length)
    
    empty_string = ""
    length = len(empty_string)
    print(length)

Please write a program which asks the user for a word and then prints out the 
number of characters, if there was more than one typed in.
"""

# Write your solution here
userWord = input("Please type in a word:")
wordLen = len(userWord)

if wordLen > 1:
    print(f"There are {wordLen} letters in the word {userWord}")

print("Thank you!")

"""
Please write a program which asks the user for a floating point number and then 
prints out the integer part and the decimal part separately. Use the Python int 
function.

You can assume the number given by the user is always greater than zero.

An example of expected behaviour:
    
    Please type in a number: 1.34
    Integer part: 1
    Decimal part: 0.34
"""

# Write your solution here
userNumber = float(input("Please type in a number:"))

print(f"Integer part: {int(userNumber)}\nDecimal part: {userNumber % 1}")