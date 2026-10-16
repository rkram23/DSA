#Factorial using Iterative method

def factorial_iterative(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    temp = 1
    for i in range(1, n+1):
        temp *= i
    return temp

#Factorial using Recursive method

def factorial_recursive(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

#Finding Fibonnaci Series using Iterative Method 

def fibo_iterative(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    fib_val = 0
    curr_val = 1
    last_val = 0

    if n == 0:
        fib_val = 0
    elif n == 1:
        fib_val = 1
    else:
        for i in range(2, n+1):
            fib_val = curr_val + last_val
            last_val = curr_val
            curr_val = fib_val
    return fib_val

#Finding Fibonnaci Series using Recursive Method 

def fibo_recursive(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)

#Finding GCD using Recursive Method
#Reference: https://www.geeksforgeeks.org/python/gcd-in-python/

def gcd_recursive(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError("gcd requires integer arguments")
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

DIGITS = "0123456789ABCDEF"

def convert_recursive(decimal, base):
    if type(decimal) != int or type(base) != int:
        raise TypeError("convert requires integer arguments")
    if base < 2 or base > 16:
        raise ValueError("base must be between 2 and 16")
    if decimal < 0:
        raise ValueError("decimal must be non-negative")
    if decimal == 0:
        return "0"

    def convert(n):
        if n < base:
            return DIGITS[n]
        return convert(n // base) + DIGITS[n % base]

    return convert(decimal)

#Towers of Hanoi using Recursive Method
#Reference: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

def moveDisk(src, dest):
    print(f"Moving Disk from Source {src} to Destination {dest}")

def towers_of_hanoi(n, src='A', dest='C', aux='B'):
    if type(n) != int:
        raise TypeError("towers_of_hanoi requires an integer number of disks")
    if n < 1:
        raise ValueError("number of disks must be at least 1")

    if n == 1:
        moveDisk(src, dest)
        return 1

    moves = towers_of_hanoi(n - 1, src, aux, dest)
    moveDisk(src, dest)
    moves += 1
    moves += towers_of_hanoi(n - 1, aux, dest, src)

    return moves