# -*- coding: utf-8 -*-
"""
More about variables

Printing with f-strings
What if we want to have more flexibility and control over what we print out? So 
called f-strings are another way of formatting printouts in Python. The syntax 
can initially look a bit confusing, but in the end f-strings are often the 
simplest way of formatting text.

With f-strings the previous example would look like this:
    
   result = 10 * 25
   print(f"The result is {result}") 

A single f-string can contain multiple variables. For example this code:
    
    name = "Mark"
    age = 37
    city = "Palo Alto"
    print(f"Hi {name}, you are {age} years old. You live in {city}.")
    
prints out this:
    
    Hi Mark, you are 37 years old. You live in Palo Alto.
    
-------------------------------------------------------------------------------
1. Programming excercise: Extra space

Your friend is working on an app for jobseekers. She sends you this bit of code:
    
    name = "Tim Tester"
    age = 20
    skill1 = "python"
    level1 = "beginner"
    skill2 = "java"
    level2 = "veteran"
    skill3 = "programming"
    level3 = "semiprofessional"
    lower = 2000
    upper = 3000
    
    print("my name is ", name, " , I am ", age, "years old")
    print("my skills are")
    print("- ", skill1, " (", level1, ")")
    print("- ", skill2, " (", level2, ")")
    print("- ", skill3, " (", level3, " )")
    print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")
    
The program should print out exactly the following:
    
        my name is Tim Tester, I am 20 years old
        
        my skills are
         - python (beginner)
         - java (veteran)
         - programming (semiprofessional)
        
        I am looking for a job with a salary of 2000-3000 euros per month
"""

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("1. Programming excercise: Extra space")
print(f"my name is {name}, I am {age} years old\n \nmy skills are\n - {skill1} ({level1})\n - {skill2} ({level2})\n - {skill3} ({level3})\n \nI am looking for a job with a salary of {lower}-{upper} euros per month")
print("\n")


"""
2. Floating point numbers
Floating point number or float is a term you will come across often in 
programming. It refers to numbers with a decimal point. They can be used much 
in the same way as integer values.

This program calculates the mean of three floating point numbers:
    
    number1 = 2.5
    number2 = -1.25
    number3 = 3.62
    
mean = (number1 + number2 + number3) / 3
print(f"Mean: {mean}")

output:
    
    Mean: 1.6233333333333333
    
-------------------------------------------------------------------------------
2. Programming excercise: Arithmetics

This program already contains two integer variables, x and y:
    
    x = 27
    y = 15
    
Please complete the program so that it also prints out the following:
    
    27 + 15 = 42
    27 - 15 = 12
    27 * 15 = 405
    27 / 15 = 1.8
    
The program should work correctly even if the values of the variables are 
changed. That is, if the first two lines are replaced with this:
    
    x = 4
    y = 9
    
the program should print out the following:
    
    4 + 9 = 13
    4 - 9 = -5
    4 * 9 = 36
    4 / 9 = 0.4444444444444444
"""

print("2. Programming excercise: Arithmetics")

x = 27
y = 15

print(f"{x} + {y} = {x + y}\n{x} - {y} = {x - y}\n{x} * {y} = {x * y}\n{x} / {y} = {x / y}\n")
print("\n")

"""
-------------------------------------------------------------------------------
3. Programming excercise: Fix the code: Print a single line

Each print command usually prints out a line of its own, complete with a change 
of line at the end. However, if the print command is given an additional 
argument end = "", it will not print a line change.

For example:
    
    print("Hi ", end="")
    print("there!")
    
Output: 
    
    Hi there!
    
Please fix this program so that the entire calculation, complete with result, 
is printed out on a single line. Do not change the number of print commands 
used.

    print(5)
    print(" + ")
    print(8)
    print(" - ")
    print(4)
    print(" = ")
    print(5 + 8 - 4)
    

"""

print("3. Programming excercise: Fix the code: Print a single line")
print(f"5 + 8 - 4 = {5 + 8 - 4}")




















