# -*- coding: utf-8 -*-
"""
Getting started

1. Computer programs consist of commands, each command instructing the computer to take some action. 
A computer executes these commands one by one. Among other things, commands can be used to perform 
calculations, compare things in the computer's memory, cause changes in how the program functions, 
relay messages or ask for information from the program's user.

Let's begin programming by getting familiar with the print command, which prints text. In this context, 
printing essentially means that the program will show some text on the screen.

The following program will print the line "Hi there!":
"""
print("--------- Getting Started ---------")
print("Hi there!")
print("\n")

## Programming exercise: Please write a program which prints out an emoticon: :-) ##
print("1. Programming Excercise: Please write a program which prints out an emoticon")
print("\n")
print(":-)")
print("\n")
"""
2. A program of multiple commands
Multiple commands written in succession will be executed in order from first to last. 
For example this program:
    
    print("Welcome to Introduction to Programming!")
    print("First we will practice using the print command.")
    print("This program prints three lines of text on the screen.")

prints the following lines on the screen:
    
    Welcome to Introduction to Programming!
    First we will practice using the print command.
    This program prints three lines of text on the screen.

Programming Excercise: Fix the code: Seven Brothers

"Seitsemän veljestä" is one of the first novels ever written in Finnish. It is the story of seven orphaned 
brothers learning to make their way in the world (read more on Wikipedia).

This program is supposed to print out the names of the brothers in alphabetical order, but it's not working 
quite right yet. Please fix the program so that the names are printed in the correct order.

        print("Simeoni")
        print("Juhani")
        print("Eero")
        print("Lauri")
        print("Aapo")
        print("Tuomas")
        print("Timo")
"""
print("2. Programming Excercise: Fix the code: Seven Brothers")
print("\n")

print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

print("\n")

"""
3. Please write a program which prints out the following lines exactly as 
they are written here, punctuation and all:
    
    Row, row, row your boat,
    Gently down the stream.
    Merrily, merrily, merrily, merrily,
    Life is but a dream.
    
"""
print("3. Programming Excercise: Row, row, row your boat")
print("\n")

print("Row, row, row your boat,")
print("Gently down the stream.")
print("Merrily, merrily, merrily, merrily,")
print("Life is but a dream.")
print("\n")

"""
4. Arithmetic operations

You can also put arithmetic operations inside a print command. Running it will 
then print out the result of the operation. For example, the following program

    print(2 + 5)
    print(3 * 3)
    print(2 + 2 * 10) 
    
prints out these lines:
    7
    9
    22

Notice the lack of quotation marks around the arithmetic operations above. 
Quotation marks are used to signify strings. In the context of programming, 
strings are sequences of characters. They can consist of letters, numbers and any other types 
of characters, such as punctuation. Strings aren't just words as we commonly understand them, 
but instead a single string can be as long as multiple complete sentences. Strings are usually 
printed out exactly as they are written. Thus, the following two commands produce two quite 
different results:
    
    print(2 + 2 * 10)
    print("2 + 2 * 10")

This program prints out:
    
    22
    2 + 2 * 10

With the second line of code, Python does not calculate the result of the operation, but instead 
prints out the operation itself, as a string. So, strings are printed out just as they are written, 
without any reference to their contents.

Commenting
Any line beginning with the pound sign #, also known as a hash or a number sign, is a comment. 
This means that any text on that line following the # symbol will not in any way affect how the 
program functions. Python will simply ignore it.

Comments are used for explaining how a program works, to both the programmer themselves, and others 
reading the program code. In this program a comment explains the calculation performed in the code: 
    
    print("Hours in a year:")
    # there are 365 days in a year and 24 hours in each day
    print(365*24)
    
When the program is run, the comment will not be visible to the user:
    
    Hours in a year:
    8760

Short comments can also be added to the end of a line:
    
    print("Hours in a year:")
    print(365*24) # 365 days, 24 hours in each day
    
Programming excercise: Minutes in a year: 

Please write a program which prints out the number of minutes in a year. Use Python code to 
perform the calculation, as in the previous code example.

"""
print("4. Programming Excercise: Minutes in a year")
print("\n")
print(60 * 24 * 365)
print("\n")

"""
5. Print some code

Thus far, you have probably used double quotation marks " to print out strings. In addition to 
the double quotation marks, Python also accepts single quotation marks '.

This comes in handy if you ever want to print out the actual quotation marks themselves:
    
    print('"Come right back!", shouted the police officer.')
    output: "Come right back!", shouted the police officer.
    
Please write a program which prints out the following:
    
    print("Hello there!")
"""
print("5. Programming Excercise: Hello there!")
print("\n")
print('print("Hello there!")')