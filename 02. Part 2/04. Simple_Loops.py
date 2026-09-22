#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt
"""
Created on Sat Sep 19 13:18:51 2026

@author: junio

1. Shall we continue?

Let's create a program along the lines of the example above. This program should 
print out the message "hi" and then ask "Shall we continue?" until the user inputs 
"no". Then the program should print out "okay then" and finish. Please have a look 
at the example below.

Sample output
hi
Shall we continue? yes
hi
Shall we continue? oui
hi
Shall we continue? jawohl
hi
Shall we continue? no
okay then
"""

while True:
    
    print("hi")
    
    programContinue = input("Shall we continue?")
    
    if programContinue == "no":
        break
    

"""
2. Input Validation

Please write a program which asks the user for integer numbers.

If the number is below zero, the program should print out the message "Invalid number".

If the number is above zero, the program should print out the square root of 
the number using the Python sqrt function.

In either case, the program should then ask for another number.

If the user inputs the number zero, the program should stop asking for numbers
and exit the loop.

Below you'll find a reminder of how the sqrt function is used. Remember to 
import it in the beginning of the program.

# sqrt function will not work without this line in the beginning of the program
from math import sqrt

print(sqrt(9))
Sample output
3.0

An example of expected behaviour of your program:

Sample output
Please type in a number: 16
4.0
Please type in a number: 4
2.0
Please type in a number: -3
Invalid number
Please type in a number: 1
1.0
Please type in a number: 0
Exiting...


"""



while True:
    
    userInt = int(input("Please type in a number: "))
    
    if userInt < 0:
        print("Invalid number")
    elif userInt > 0:
        print(f"{sqrt(userInt)}")
    else:
        print("Exiting...")
        break
    
"""
3. Fix the code: Countdown

This program should print out a countdown. The code is as follows:

number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number > 0:
    break

print("Now!")
This should print out

Sample output
Countdown!
5
4
3
2
1
Now!

However, the program doesn't quite work. Please fix it.
"""

number = 5

print("Countdown!")

while True:
    
  print(number)
  
  number = number - 1
  
  if number == 0:
      
    break

print("Now!")

"""
4. Repeat Password

Please write a program which asks the user for a password. The program should 
then ask the user to type in the password again. If the user types in something 
else than the first password, the program should keep on asking until the user 
types the first password again correctly.

Have a look at the expected behaviour below:

Sample output
Password: sekred
Repeat password: secret
They do not match!
Repeat password: cantremember
They do not match!
Repeat password: sekred
User account created!

"""

# Write your solution here
userPassword1 = input("Password:")

while True:
    
    userPassword2 = input("Repeat password:")
    
    if userPassword1 == userPassword2:
        print("User account created!")
        break
    else:
        print("They do not match!")
        
"""
5. PIN and number of attempts

Please write a program which keeps asking the user for a PIN code until they 
type in the correct one, which is 4321. The program should then print out the 
number of times the user tried different codes.

Sample output
PIN: 3245
Wrong
PIN: 1234
Wrong
PIN: 0000
Wrong
PIN: 4321
Correct! It took you 4 attempts

If the user gets it right on the first try, the program should print out something a bit different:

Sample output
PIN: 4321
Correct! It only took you one single attempt!
"""
# Write your solution here
attempts = 0

while True:
    
    userPin = int(input("PIN:"))
    
    attempts += 1
    
    if userPin == 4321:
        break
    else:
        print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
    

"""
6. The next leap year

Please write a program which asks the user for a year, and prints out the next 
leap year.

Sample output
Year: 2023
The next leap year after 2023 is 2024

If the user inputs a year which is a leap year (such as 2024), the program should 
print out the following leap year:

Sample output
Year: 2024
The next leap year after 2024 is 2028
"""
userYear = int(input("Year:"))
futureYear = userYear + 1

while True:
     
    if (futureYear % 400 == 0 or (futureYear % 4 == 0 and futureYear % 100 != 0)):
        print(f"The next leap year after {userYear} is {futureYear}")
        break;

    futureYear += 1
    

"""
7. Story

Part 1
Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

Sample output
Please type in a word: Once
Please type in a word: upon
Please type in a word: a
Please type in a word: time
Please type in a word: there
Please type in a word: was
Please type in a word: a
Please type in a word: girl
Please type in a word: end
Once upon a time there was a girl

Part 2
Change the program so that the loop ends also if the user types in the same word twice in a row.

Sample output
Please type in a word: It
Please type in a word: was
Please type in a word: a
Please type in a word: dark
Please type in a word: and
Please type in a word: stormy
Please type in a word: night
Please type in a word: night
It was a dark and stormy night

"""
wordStack = ""
previous = ""

while True:
    userWord = input("Please type in a word:")
    
    if (userWord == "end" or userWord == previous):
        print(f"{wordStack}")
        break
    
    wordStack += userWord + " "
    previous = userWord


"""
8. Working with numbers

Pre-task
Please write a program which asks the user for integer numbers. The program 
should keep asking for numbers until the user types in zero.

Sample output
Please type in integer numbers. Type in 0 to finish.
Number: 5
Number: 22
Number: 9
Number: -2
Number: 0

Part 1: Count
After reading in the numbers the program should print out how many numbers were 
typed in. The zero at the end should not be included in the count.

You will need a new variable here to keep track of the numbers typed in.

Sample output
... the program asks for numbers
Numbers typed in 4

Part 2: Sum
The program should also print out the sum of all the numbers typed in. The zero 
at the end should not be included in the calculation.

The program should now print out the following:

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34

Part 3: Mean
The program should also print out the mean of the numbers. The zero at the end 
should not be included in the calculation. You may assume the user will always 
type in at least one valid non-zero number.

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5

Part 4: Positives and negatives
The program should also print out statistics on how many of the numbers were 
positive and how many were negative. The zero at the end should not be included 
in the calculation.

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5
Positive numbers 3
Negative numbers 1

"""

print("Please type in integer numbers. Type in 0 to finish.")
i = 0
sum = 0
positive = 0
negative = 0

while True:
    
    userNumber = int(input("Number:"))

    if(userNumber > 0):
        positive += 1
    
    if(userNumber < 0):
        negative += 1
    
    if (userNumber == 0):
        print(f"Numbers typed in {i}\nThe sum of the numbers is {sum}")
        print(f"The mean of the numbers is {sum/i}")
        print(f"Positive numbers {positive}")
        print(f"Negative numbers {negative}")
        break

    sum += userNumber
    i += 1
















