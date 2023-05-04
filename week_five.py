# MODULES IN PYTHON
import sys
# from math import *
# from math import sqrt as s
from math import sqrt, log10

# You can always use keywords as import from, * and as

# List of the paths where the interpreter searches the modules from.
locations = sys.path
for l in locations:
    print(l)

root = sqrt(9)
print(root)
log_50 = round(log10(50), 3)
print(log_50)

country = "Uganda"


def change_country():
    ctry = "Germany"
    def cc():
        nonlocal ctry
        ctry = "East Africa"
        print(f"This is inside cc {ctry}")
    print(ctry)
    return cc()

print(country)
print(change_country())

# Scope is local by default in python so meaning a global variable wont be changed if the same var is declared within
# a function.

# json module converts dicts to json objects with the dumps method.
# When working with dictionaries always make sure to typecase correctly that is
# b'se data passed by default everything is a string

# RELOAD FUNCTION - reloads an imported module in python.
# Argument passed to it must be a module that has been successfully imported into a program.
# Reload function helps make dynamic changes within your code with the help of import statements.
# it is imported from the importlib package

# ---------------------- MODULE USE CASES ----------------------------------
# Modules are similar to files whereas Packages are like directories that contain different files.
# A library is a collection of packages.
# To install the packages that aren't part of standard library programmers use "pip".
# You can check for pip installation using python3 -m ensurepip --upgrade on MAC
# || py -m ensurepip --upgrade on windows
# To install packages use py -m pip install <package> on windows
# NB: Always look up the documentation of the packages to understand well their functionality.

# SUB PACKAGES - These are the directories inside the packages themselves
# We use the [dot notation] to access them
# for-example: <import matplotlib.pyplot as plt>

# --------------------- POPULAR PACKAGES ------------------------------------
# Each package is a book or magazine | A module is a file or document.
# PRIMARY USE CASES OF PYTHON
# - Data Science (numpy, sypy, nltk, pandas)
# - Machine Learning and AI (tensorflow, pytorch, keras)
# pytorch and keras are for more of deep learning, others include: scipy, scikit learn, Theano.
# - Web Frameworks (Django, Flask, cherry pie)
# - Application Development
# - Automation
# - Hardware Interfacing.

# Most Popular Builtin Packages
# - os, sys, csv, json, importlib, re, math, intertools.
# open CV and matplotlib are used for image processing and visualization.

# Get a project you want to develop and explore using on eof the above packages.

# ----DATA ANALYSIS PACKAGES----
# Numpy, SciPy, Matplotlib, SciKit Learn - Numerical Python
# Pandas - Python Data Analysis (cleaning anaylzing) using series and data frames as data structures.
# Matplotlib for data visualization.

# ------ML AND AI------ Pytorch - TensorFlow - Efficiency, flexibility, large support,
# User friendly debug and testing tools. Deep learning and neural networks, computer vision and image processing,
# natural language processing, data visualization Web scraping

# BIG DATA AND ANALYSIS WITH PYTHON

# Big data is the management of large datasets bot structured and unstructured.
# Today this data is stored in the form of data warehouses and data lakes. Both on serves and the cloud.
# Common xtics for use of big data are Volume, Variability and Velocity
# VOLUME is the size of the data in question and if large enough may require different handling to traditional data.
# VARIABILITY | VERACITY inconsistency that may be present in the data
# VELOCITY The speed of handling this data.
# -- The ability to handle a large amount of heterogeneous data with ease of acces and speedy processing.
# The next step is data analysis where latter it is its visualization or reports.

# Data Source -> Data Storage -> Filter | Transform Data -> Analysis and storage -> Report and visualization

# PYTHON WEB FRAMEWORKS

# High-level code, sockets, threading and protocols,
# Form processing, Routing requests, Connection and Authentication.
# Debugging and testing tools.
# -----------------------------------------------
# Full stack frameworks Django, WEb2py and pyramid
# Micro frameworks Flask, Bottle, cheery pie, Dash
# Asynchronous Growler, AIOHTTP, Sanic

# USEFUL LINKS
# https://www.netsolutions.com/insights/top-10-python-frameworks-for-web-development-in-2019/ - popular python packages
# Web Frameworks - https://www.netsolutions.com/insights/top-10-python-frameworks-for-web-development-in-2019/
# https://towardsdatascience.com/best-python-libraries-for-machine-learning-and-deep-learning-b0bd40c7e8c
# https://www.dataquest.io/blog/15-python-libraries-for-data-science/
