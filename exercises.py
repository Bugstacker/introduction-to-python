def add(n):
    if n == 1:
        return 0
    return n + add(n - 1)


a = add(5)
print(a)

numbers = [15, 30, 47, 82, 95]


def lesser(numbers):
    return numbers < 50


small = list(filter(lesser, numbers))
print(small)


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


five_factorial = factorial(5)
print(five_factorial)

uganda = "Pearl of africa"
