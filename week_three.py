# FUNCTIONAL PROGRAMMING
# Traditional Functions
# Pure Functions - will always do the same thing and return same result regardless of the output.

# _____Diffs and Similarities of Pure and Traditional functions____
# Traditional can access global state pure cant
# Traditional can modify global_variables pure cant
# Both can access local state
# Traditional can change Args pure cant
# Pure functions output depends on inputs whereas Traditional doesn't
# ____________________________________________________________________

# In functional programming a function should never mutate the input data.
# Functions are considered standalone/independent.
# Functions passed as arguments and also return functions. == first class citizens.

# PURE FUNCTIONS
# Pure function doesn't change or have effect on a variable, data, set or list beyond its scope.
# Always know what the outcome will be.
# Ability to cache.

my_list = [1, 2, 3]


def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl


new_list = add_to_list(my_list, 4)
print(my_list)
print(new_list)


# RECURSION - A function that calls itself over and over again.
# They r like for loops but when creating recursive functions you must always consider the results unless it will
# / turn into a for loop and suck up all the memory.

# TOWER OF HANOI puzzle
# Base conditions serve primarily to complete the execution and doesnt run into an infinite loop.
# 2nd actual call to recursion function within itself.
# Driver Code that gives the actual call to function

"""
def hanoi(dsk, source, helper, destination):
    # Base condition
    if dsk == 1:
        print(f"Disk {dsk} moves from tower {source} to tower {destination}")
        return

    # Recursive calls in which the function calls itself
    hanoi(dsk - 1, source, destination, helper)
    print(f"Disk {dsk} moves from tower {source} to tower {destination}")
    hanoi(dsk - 1, helper, source, destination)


# Driver code

try:
    disks = int(input("Number of disks to be displaced: "))
    hanoi(disks, "A", "B", "C")
except Exception as e:
    print("ERROR:", e)
"""

def deliver_presents(houses):
    if len(houses) == 1:
        print(f"Delivering presents to {houses[0]}")

    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        #       Divide work btn two people
        deliver_presents(first_half)
        deliver_presents(second_half)


deliver_presents(["Drake's house", "Tevin's house", "Kelvin's house", "Ken's house", "Hildah's house"])


def sum_recursive(current_num, accumulated_sum):
    if current_num == 11:
        return accumulated_sum
    else:
        # print(current_num)
        return sum_recursive(current_num + 1, accumulated_sum + current_num)


print(sum_recursive(1, 0))


# REVERSING A STRING IN PYTHON str[:start:stop:step]
# slice function as well

def reverse_str(string):
    return string[::-1]


rvrsd = reverse_str("Kenneth")


# print(rvrsd)


def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]


print(string_reverse("Kenneth"))

# MAP AND FILTER - map function takes a function as an argument and then the iterable variable. // applies a function
# to the items in the list. filter creates a new list and returns the values which evaluated to true.
menu = ["matooke", "rice", "beans", "water"]


def find_water(dish):
    if dish[0] == "w":
        return dish


# map_dish = map(find_water, menu)
# print(map_dish)
# for d in map_dish:
#     print(d)

filter_dish = filter(find_water, menu)
print(filter_dish)
for val in filter_dish:
    print(val)

# COMPREHENSIONS
# List comprehensions [<expression> for x in <sequence> if <condition>]
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
added_3 = [num + 3 for num in data]
# print(f"New list with 3 added to each number {added_3}")

new_data = [x * 3 for x in data]
# print(f"Multiplied by three the list is {new_data}")

four_x = [x for x in new_data if x % 2 == 0]
# print(f"Divisible by four {four_x}")

nines = [x for x in range(100) if x % 9 == 0]
# print(f"Nines: {nines}")

nines_sub = [x - 1 for x in nines]
# print(f"Nines minus one {nines_sub}")

# Dict comprehensions
# [key: value for (key, value) in zip(list1, list2)]
# [key: value for key, value in list1]
# [key: value for in range(num)]

# Using two lists in this example
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

year = {k: v for (k, v) in zip(number, months)}
print(year)

# Using in range
using_range = {x: x * 2 for x in range(10)}
print(using_range)

# Using one input_list
num_dict = {x: x ** 2 for x in number}
print(num_dict)

# SET comprehensions use curly brackets
set_a = {x for x in range(10, 20) if x not in [12, 14, 17]}
print(f"This is the generated set with no 12, 14 and 17: {set_a}")

# Generator Comprehension using curved brackets
gen_obj = (x for x in number)
print(gen_obj)
print(type(gen_obj))
for item in gen_obj:
    print(item, sep=",", end=" ")

# List comprehensions have been a recent development they dont necessarily replace the map function
# Because still the map function is efficient when it comes to larger complex list larger lists.

a = [[96], [69]]
print("".join(list(map(str, a))))
