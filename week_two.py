import random

# FUNCTIONS set of instructions that take an input and produce output.
# They can be reused, always have a specific task to accomplish


# def calculate_tax(bill, tax_rate):
#     return round((bill * tax_rate) / 100.00, 2)
#
#
# print(f"Total Tax: {calculate_tax(175.00, 15)}")
#
# print(f"Total tax: {calculate_tax(164.33, 22)}")

# SCOPING local, enclosing, global and builtin LGBE

# LISTS insert() - specified point in an index, append() - at the end, extend() - as the name suggests
# list1 = [1, 2, 3, 4, 5]
# # list1.insert(len(list1), 6)
# # list1.append(6)
# list1.extend([6, 7, 8, 9])
#
# # POP removes an item at a specified index
# list1.pop(4)
# # DEL delete an item at a index
# del list1[2]
#
# for x in list1:
#     res = (x * x)
#     print(res)

# TUPLES count() - occurrences on an item, index() - gives u the index where the item is located
# can loop through a tuple as well __tuples are immutable all other list methods work as well

my_tuple = (1, "strings", 4.5, True)
# print(my_tuple.index(4.5))

# SETS dont allow duplicate values [add(), remove(), discard() same as remove,] no duplicates but unordered items
set_a = {1, 2, 3, 4, 5, 5}
set_b = {4, 5, 6, 7, 8}

# print(set_a.union(set_b)) or use the | symbol
print(set_a | set_b)  # union
print(set_a & set_b)  # intersection
print(set_a - set_b)  # difference
print(set_a ^ set_b)  # symmetrical_difference

# DICTIONARY - mutable, use key to access items [del to delete specifying the key u want to delete]

my_dict = {1: "Test", "Name": "Kenneth", "course": "CS"}

for key, value in my_dict.items():
    print(f"{key}: {value}")


# ARGS AND KWARGS - args u can pass n unnamed variables as function arguments.


# def sum_of(*args):
#     num = 0
#     for x in args:
#         num += x
#     return num
#
#
# print(sum_of(2, 3, 4, 5))

def sum_of(**kwargs):  # with kwargs u can pass in a number of keyword arguments
    num = 0
    for k, v in kwargs.items():
        num += v
    return round(num, 2)


print(sum_of(coffee=2.99, water=1.99, donut=4.99))


# EXCEPTIONS are known errors that should be handled
# SYNTAX error might be a typo

# Exception handling

def divide_by(a, b):
    return a / b


try:
    ans = divide_by(40, 4)
    print(ans)
except ZeroDivisionError as e:
    print(f"{e}, we cant divide by zero")
except Exception as e:
    print(f"{e}, something went wrong!")

# LIST COMPREHENSIONS
my_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(my_list)

# FILE HANDLING open() and close()
# OPEN FUNCTION open(<FILE NAME> <FILE LOCATION>, MODE)
# MODE specifies the action required whether its writing reading or create also includes the Output format
# whether u want it in text or binary.

# "r" - reads a file in text format
# "rb" - opens and reads a file in binary format
# "r+" - opens a file for reading and writing
# "w" - open for writing
# "a" - opens a file for editing or appending data.

# CLOSE FUNCTION
# close() doesnt take any arguments
# ANOTHER WAY TO OPEN OR CLOSE A FILE is __with open__ - which automatically closes a file
# opening the file (with open) automatically closes the file for you so no need to call the close function.
try:
    with open("text.txt", "r") as file:  # prints out a demo error
        data = file.read()
        print(data)
except FileNotFoundError as e:
    print("ERROR", e)

# CREATING FILES in python.
# To write multiple lines u can use the writelines() it accepts a list and a comma for each line
# To add new lines as specified by the word u need to add the \n
# To edit content always remember to use (a) mode which edits or appends to the file.
try:
    with open("newfile.txt", "w") as file:
        file.writelines(["\nKenneth Matovu", "\nFrontend Web Developer",
                         "\nKampala, Uganda", "\nStudent", "\nStudying is passion"])
except FileNotFoundError as e:
    print("ERROR", e)

# ALWAYS REMEMBER TO HANDLE EXCEPTIONS WHEN WORKING WITH FILES

# READING FILES read() readline() readlines()
# read(no.) - specified number as a list
# readline() - returns only the first line | readline(10) - returns a specified no. of chars on a single line.
# readlines() - Entire content of the file in a list which you iterate over and do some operations.

# DEMO program to choose for a name for my dog.
try:
    with open("test.txt", "r") as file:
        # data = file.readlines()  # returns a list by default you can iterate over it
        pet_names = file.read()
        pet_names_list = pet_names.split("\n")
        print(random.choice(pet_names_list))
except FileNotFoundError as e:
    print("ERROR", e)


# ALGORITHMS
# Palindrome Example
# str starts with same letter ends with same letter
# Recursion, divide and conquer, dynamic programming and greedy algorithms.

def is_palindrome(string):
    if string[0] == string[len(string) - 1]:
        print("Is a Palindrome")
        return "Is a Palindrome"
    else:
        print("Is not a Palindrome")
        return "Is not a Palindrome"


print(is_palindrome("rear"))

# CUP OF COFFEE - Algorithm exercise
# 1. Gas - Make teh fire
# 2. Coffee - Put milk in the sauce pan then put it on gas
# 3. Milk - Wait for a few minutes to when the milk is ready
# 4. Sugar - Put it in a cup with some sugar
# Then consider asking for inputs or these things then finally produce the coffee

# ALGORITHMIC COMPLEXITY
# Time and Space Complexity
# Horrible
# Bad
# Fair
# Good
# Excellent

# Constant time - takes same time and space O(C/1)
# Linear time - the bigger the range the bigger the running time O(log(n))
# Logarithmic time - running time of input against the number of operations. O(n)
# Quadratic Time - Linear operation of each time of linear operation **2 O(n^2)
# Cubic Time - O(n^3)
# Exponential Time - O(2^n)
# Factorial Time - O(n!)

# Binary search:
#   splitting the input int two to determine a pivot and whether the input is less or greater than.

# BIG O NOTATION
# Metric to measure program / snippet performance / Cost of an algorithm.
# Algorithmic Complexity - Is a measure of how long an algorithm will take to complete given teh size of input.
# commonly denoted by n or n(times)
# Time refers to how long an algorithm takes to complete.
# Space refers to the amount of memory needed to complete the algorithm.

# Useful links
# https://docs.pytest.org/en/7.1.x/
# https://stackabuse.com/test-driven-development-with-pytest/
