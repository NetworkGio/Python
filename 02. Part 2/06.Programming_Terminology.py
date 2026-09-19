# -*- coding: utf-8 -*-
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
       
Please type in a number: 13
13 must be my lucky number!
Have a nice day!

Please type in a number: 101
The number was greater than one hundred
Now its value has decreased by one hundred
Its value is now 1
1 must be my lucky number!
Have a nice day!
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
    
    4
    8
    10
    0
    
Please write a program which asks the user for a word and then prints out the 
number of characters, if there was more than one typed in.

Examples of expected behaviour:  
    
    Please type in a word: hey
    There are 3 letters in the word hey
    Thank you!
    
    
    Please type in a word: banana
    There are 6 letters in the word banana
    Thank you!
    
    Please type in a word: b
    Thank you!
"""
word = str(input("Please type in a word:"))

if len(word) > 1:
    print(f"There are {len(word)} in the word {word}\nThank you!")
else:
    print("Thank you!")
    
"""
3. Typecasting

When programming in Python, often we need to change the data type of a value. 
For example, a floating point number can be converted into an integer with the 
function int:
    
    temperature = float(input("Please type in a temperature: "))

    print("The temperature is", temperature)
    
    print("...and rounded down it is", int(temperature))
    
Please type in a temperature: 5.15
The temperature is 5.15
...and rounded down it is 5

Notice the function always rounds down, and not according to the rounding rules 
in mathematics. This is an example of a floor function.

Please type in a temperature: 8.99
The temperature is 8.99
...and rounded down it is 8


Please write a program which asks the user for a floating point number and then 
prints out the integer part and the decimal part separately. Use the Python int 
function.

You can assume the number given by the user is always greater than zero.

An example of expected behaviour:
    
    Please type in a number: 1.34
    Integer part: 1
    Decimal part: 0.34
"""
number = float(input("Please type ion a number:"))
print(f"Integer part: {int(number)}\nDecimal part: {number - int(number)}")



































