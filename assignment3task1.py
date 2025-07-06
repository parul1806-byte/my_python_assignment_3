# factorial of a number with recursion
n = int(input("enter a number:"))
def factorial(n):
    if (n==0 or n==1):
        return(1)
    else:
        fact = n * factorial(n-1)
        return(fact)
print("factorial of ", n, "is :",factorial(n))

