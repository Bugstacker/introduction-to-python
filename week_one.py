import time
# __VARIABLES__
# a, b, c = 1, 2, 3
# a = b = c = 3
# print(a, b, c)

# __DATATYPES__
# numeric -int, float, complex numbers(a = 10 + 10j) type()
# sequences str (), lists [], tuples ()
# dict {} key-value pair
# bool True/False
# set _unordered {} un-repeated

# __strings__
var_a = "Hello World" \
        " This world is really amazing taht is why am in it" \
        " Do you agree?"
var_b = " Ken is my name"


# __type casting__ converting one data type to another.
# implicit is automatic for compatible data types.
# explicit with provided functions str() int() float() ord() hex() oct() tuple() set() list() dict()


def floated_str(val):
    return float(input(val))


# coffee = floated_str("Enter the coffee price: ")
# jum = floated_str("Enter the jum price: ")
# bread = floated_str("Enter the bread price: ")

# total = coffee + jum + bread
# print(f"The total is ${total}")

# Logical operators and, or and not
# discount = 10
# total_bill = 100
# is_in_loyalty_program = False
# to_discount = 100 - total_bill
#
# if total_bill >= 100 and is_in_loyalty_program:
#     total_bill -= (float(total_bill) / 100 * discount)
#     print(f"The total bill is {total_bill} thanks for being a valuable customer")
# elif total_bill >= 100 and not is_in_loyalty_program:
#     discount /= 2
#     total_bill -= discount
#     print(f"The total bill is {total_bill} consider joining the loyalty program for more benefits")
# elif total_bill < 100 and is_in_loyalty_program:
#     print(f"Your bill is {total_bill} with no discount consider a purchase worth {to_discount} to enjoy a " \
#           "10% off discount")
# else:
#     print(f"Sorry no discount applied on the purchase consider purchasing goods worth {to_discount} to enjoy" \
#           " 5% off if your order is above $100 and 10% off if the it is the same case and your in our loyalty program.")


# MATCH statement
# http_status = 501
#
# match http_status:
#     case 200 | 201:
#         print("Success")
#     case 400:
#         print("Bad request")
#     case 404:
#         print("Not Found")
#     case 500 | 501:
#         print("Server Error")
#     case _:
#         print("Unknown status")
#
# # LOOP for and while
# me = ("Kenneth", "Meta frontend Dev", "Ugandan", "Loves tech" )
#
# # we use idx - index with the enumerate function to get access to the index of the element.
# for idx, item in enumerate(me):
#     print(idx, item.upper())
#
# desserts = ["Chocolate", "KFC", "Ice cream", "Yoghurt", "Smoothie"]

# __BREAK__
"""
for dessert in desserts:
    if dessert.lower() == "chocolate":
        print(f"Your favorite dessert {dessert} is here")
        # break stops the loop when condition is met.
        break
else:
    print(f"Not found this on the list")"""

# __CONTINUE__
"""
for dessert in desserts:
    if dessert.lower() == "chocolate":
        # continue lets skip over a section and continue with rest more like filter.
        continue
    print(f"Other favorite desserts of mine are {dessert}")"""

# __PASS__
"""
for dessert in desserts:
    if dessert.lower() == "ice cream":
        # helps run through the loop in its entirety and effectively ignore that the if condition has been satisfied.
        pass
    print(f"{dessert} is one of my favorite desserts")

num = 4
# while loop is based on the condition being true and exits when it becomes false.
while num > 0:
    print(num)
    num -= 1

# counting time taken for this loop to run using the time function
start_time = time.time()
# outer loop
for i in range(2):
    # inner loop
    for j in range(10):
        print(0, end=" ")
    print()

print(round(time.time() - start_time), 2)
"""

