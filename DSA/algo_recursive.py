# recursive algorithms - function that calls itself
# factorial: n! = n * (n-1) * (n-2) * ... * 1 eg 5 is 5 × 4 × 3 × 2 × 1 = 120.  
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))