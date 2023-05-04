# software testing is a process of evaluating and verifying the various software applications
# and products in terms of performance, correctness, and completeness.

# Least tests written to find the largest number of defects.
# Poor design, Functionality, Scalability, Security, AB testing, Compatibility, Assurance, Experience.
# The tests should follow Re-usability, Traceability and Efficiency
# TESTING LIFE CYCLE - Planning -> Preparation -> Execution -> Reporting
# This can be writing compiling correcting and then reporting.

# X-TICS OF A GOOD TEST
# Coverage, Re-usability, UX, Reduce cost, increase satisfaction.
# - Test cycles, passing percentage, deadlines and time intervals

# Types of Testing
# White box tests
# Black box tests
# Functional tests are based on business requirements.
# Non-functional tests
# Maintenance tests
# Unit/Component testing, integration testing, system testing, acceptance testing

# Unit tests are written while writing code
# Integration tests are whether the apps are communication correctly.
# system test - tests all the software. | shipping of software.
# Acceptance testing - deployment | Bug free - scenarios to find bugs

# Testing early and test frequently.
# Agile Model - release different versions of the model and testing is done every after a few weeks.

# TEST AUTOMATION PACKAGES
# There must be a bridge btn programming code and test cases.
# Unittest , PyTest, Robot, Selenium (Web apps)
# STEPS - prepare test env, run test scripts and then analyze the results
# PyTest expects a bool after evaluating the assert statement
import addition
from week_two import is_palindrome, divide_by


def test_is_palindrome():
    assert is_palindrome("string") == "Is not a Palindrome"


def test_add():
    assert addition.add(4, 5) == 9


def test_sub():
    assert addition.sub(4, 5) == -1


def test_divide():
    assert divide_by(6, 3) == 2

# py -m pytest <tests file> | py -m pytest <tests file>::<test fn> to run the tests in teh terminal
# Always add a suffix test_ to the file where the tests are being written.

# TDD STEPS - Test Driven Development
# 1. Write a test for a feature that fails
# 2. Write code in accordance with the tests
# 3. Run the tests expecting them to fail
# 4. evaluate error and refactor the code as needed.
# 5. Rerun the process.

# Fail the test and rewrite code until u dont have to.

# Test Driven Development Steps.
# Write test case with some functionality in mind
# Write code to test after tests
# Refactor if code fails

