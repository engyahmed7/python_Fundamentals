# !/usr/bin/env python3

import math

# 1- Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

def reverse_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(last_name + " " + first_name)
    
    
reverse_name()

# 2- Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

def calc_value():
    n = int(input("Enter a number: "))
    result = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
    print(result)
    
    
calc_value()

# 3- Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example


def print_documents():
    print("""
    a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example
    """)
    
print_documents()

# 4- Write a Python program to get the volume of a sphere with radius 6.

def sphere_volume():
    r = 6
    volume = (4/3) * math.pi * pow(r, 3)
    print(volume)
    
    
sphere_volume()


# 5- Write a Python program that will accept the base and height of a triangle and compute
# the area.

def area_of_triangle():
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(area)

area_of_triangle();

# 6- Write a Python program to construct the following pattern, using a nested for loop.


def pattern():
    for i in range(5):
        for j in range(i):
            print("*", end="")
        print()
    for i in range(5, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
        
pattern()
    
    
# 7- Write a Python program that accepts a word from the user and reverse it.

def reverse_word():
    word = input("Enter a word: ")
    print(word[::-1])

reverse_word()

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

def print_numbers():
    for i in range(7):
        if i == 3 or i == 6:
            continue
        print(i)
        
print_numbers()


# 9-Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

def fibonacci():
    a, b = 0, 1
    while b < 50:
        print(b)
        a, b = b, a + b
fibonacci()

# 10 - write a python program that accepts a string and calculate the number of digits and letters.

def count_digits_letters():
    str_input = input("Enter a string: ")
    digits = 0
    letters = 0
    for i in str_input:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            letters += 1
    print("Letters: ", letters)
    print("Digits: ", digits)
    
    
count_digits_letters()
    
    
