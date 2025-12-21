Recursive Function: Base case and Recursive case


def count(n):
    if n == 0 :
        return
    print(n)
    count(n-1)   # recursive case
count(5)


"""

Factorial:
1! = 1
4! = 4 * 3* 2 * 1 = 24 
5! = 5 * 4 * 3 * 2 * 1 = 120
6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 = 120

"""


def factorial(n):
    if n == 1 :
        return 1
    else:
        fact = n * factorial(n-1)
        return fact
result = factorial(5)

print("Factorial is :", result)

