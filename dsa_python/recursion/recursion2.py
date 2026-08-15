# Write a recursive program to calculate sum of first N natural numbers

def sumN(n):
    if n == 0:
        return 0
    return sumN(n-1) + n
        
# print(sumN(5))



# Write a recursive program to calculate sum of first N odd natural numbers

def sumOdd(n):
    if n == 0:
        return 0
    return sumOdd(n-1) + (2*n-1)

# print(sumOdd(5))



# Write a recursive program to calculate sum of first N even natural numbers

def sumEven(n):
    if n==0:
        return 0
    return sumEven(n-1) + 2*n

# print(sumEven(0))



# Write a recursive program to calculate factorial of a number

def fact(n):
    if n==0:
        return 1
    return fact(n-1) * n

# print(fact(5))



# Write a recursive program to calculate sum of squares of first N natural numbers

def sumSquare(n):
    if n==1:
        return 1
    return sumSquare(n-1) + (n**2)

print(sumSquare(5))