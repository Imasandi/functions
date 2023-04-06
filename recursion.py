    """ Recursion """
# defined function can call itself
# common mathematical and programming consept
# function called itself
# can loop through data
"""
Write a program and recurrence relation to find the Fibonacci series of n where n>2 . 
Mathematical Equation:  

n if n == 0, n == 1;      
fib(n) = fib(n-1) + fib(n-2) otherwise;
Recurrence Relation: 

T(n) = T(n-1) + T(n-2) + O(1)
Recursive program: 

Input: n = 5 
Output:
Fibonacci series of 5 numbers is : 0 1 1 2 3
"""


def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


# Driver Code

# Initialize variable n.
n = 5
print("Fibonacci series of 5 numbers is :", end=" ")

# for loop to print the fibonacci series.
for i in range(0, n):
    print(fib(i), end=" ")

"""
Problem 2: Write a program and recurrence relation to find the Factorial of n where n>2 . 
Mathematical Equation: 

1 if n == 0 or n == 1;      
f(n) = n*f(n-1) if n> 1;
Recurrence Relation: 

T(n) = 1 for n = 0
T(n) = 1 + T(n-1) for n > 0
Recursive Program: 
Input: n = 5 
Output: 
factorial of 5 is: 120
 
"""
def f(n):
    if n == 0:
        return 0

    if n == 0 or n == 1:
        return 1
    else :
        return n * f(n - 1)
n = 5

print("factorial of 5 is:" ,f(n))




