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