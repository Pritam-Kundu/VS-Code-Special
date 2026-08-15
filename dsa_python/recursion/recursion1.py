# WAP to print first N natural numbers

def printN(n):
    if n>0:
        printN(n-1)
        print(n,end="  ") 
     
# printN(10)



# WAP to print first N natural numbers in reverse order

def print_rev(n):
    if n>0:
        print(n,end="  ")
        print_rev(n-1)
        
# print_rev(10)        



# WAP to print first N(if input given is 10 then in output there must be 10 odd natural numbers) odd natural numbers 

def print_odd(n):
    if n>0:
        print_odd(n-1)
        print(2*n-1,end="  ")
            
# print_odd(10)



# WAP to print first N(if input given is 10 then in output there must be 10 odd natural numbers) even natural numbers

def print_even(n):
    if n>0:
        print_even(n-1)
        print(2*n,end="  ")
        
# print_even(10)



# WAP to print first N odd natural numbers in reverse order

def printOddRev(n):
    if n>0:
        print(2*n-1,end="  ")
        printOddRev(n-1)
        
# printOddRev(10)



# WAP to print first N even natural numbers in reverse order

def printEvenRev(n):
    if n>0:
        print(2*n,end="  ")
        printEvenRev(n-1)
        
printEvenRev(10)