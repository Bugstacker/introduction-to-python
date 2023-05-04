# OOP
# Paradigm is a style of programming.
# Inheritance, Polymorphism(A single function can act differently on the obj it has been called)
# Encapsulation(Bind methods / unwanted modifications) / Abstraction(Hide implementation details to make code more safer)

# Name mangling is the use of two leading underscores and one trailing underscore.
# In inheritance Method Resolution Order determines the flow of execution.

# CLASSES
# Attributes - Variables
# Behaviors - Methods
# pass - placeholder when nothing needs to be executed

from abc import ABC, abstractmethod

"""
class MyClass:
    a = 5
    print("Hello")

    def hello(self):
        print("Hello World")
        return


myc = MyClass()
print(myc.a)
print(myc.hello())
"""

# Define a class
# Create an instance of it
# Initialize the instance

"""
class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(f"The {self.dish} has {self.items} and takes {self.time} min to prepare")


pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pasta.items)

print(pizza.contents())

"""

"""
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(f"{self.index}")
        print(f"{philosopher} wrote the book: {book}")

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

"""

"""
class PaySlips:
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return f"{self.name} is paid {self.amount}"
        else:
            return f"{self.name} is not paid yet"

roger = PaySlips("Roger", "no", 100)
drake = PaySlips("Drake", "no", 120)

# print(roger.pay())
print(roger.status())
print(drake.status())

roger.pay()

print("After payment")
print(roger.status())
print(drake.status())

"""

# PARENT CLASSES VS CHILD CLASSES - Inheritance
# Parent class - Super/Base class
# Child Class - Sub/Derived Class
# You can add new props to the child class and as well modify the default props without affecting any other class.

"""
class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return f"May I take a leave for {days} days"

adrian = Supervisors("Adrian", "A", "apple")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.name)
print(emily.name)

"""

# MULTIPLE AND SINGLE INHERITANCE
"""
class A:
    a = 1

class B:
    b = 2

class C(A, B):
    pass

c = C()
print(c.a, c.b)

# There two methods when it comes to relationship btn two classes and objects
# Namely - issubclass() // isinstance()
print("-----------------")
print("issubclass demo")
print(issubclass(C, A))
print(issubclass(A, C))
print(issubclass(C, B))

print("-----------------")
print("isinstance demo")
print(isinstance(c, C))

"""

print("-----------------")
# SUPER FUNCTION
# Is a method that can be called in the derived class and gives access to the methods and variables of the parent
# or sibling classes.
# SIBLING CLASSES are classes that share the same parent.
# Super fn helps to drive the flow of execution. From where I can draw the values of my desired functions and variables.

"""
class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)

"""

# ABSTRACT CLASSES AND METHODS
# Interoperability, Consistency and Avoid Code duplication

"""
class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass


class Donation(Employee):
    def donate(self):
        try:
            a = float(input("How much would you like to donate ? "))
            return a
        except BaseException as e:
            print("ERROR Not a number", e)


john = Donation()
mary = Donation()
john.donate()
mary.donate()
"""

# Simple inheritance, multi inheritance, multi level inheritance, Hierachical inheritance, hybrid inheritance
# Method Resolution Order // MRO
# Determines the order in which a given method or attribute passed is searched.
# C3 linearization algorithm.
# Adheres to motonicity. - Follows inheritance graph - Visits super class after local classes.


