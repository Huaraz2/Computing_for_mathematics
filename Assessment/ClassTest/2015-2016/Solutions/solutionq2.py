"""
Solution to question 2 of class test

Marking for this question will be lenient with marks given for methodology and 'almost working' answers.

This question was a tiny modification of known code for the fibonacci
sequence
There were multiple acceptable answers to the iterative approach:
"""

### This is the approach that was closest to the notes and requires the tiniest
### modification to code students have seen before.  The other approaches
### are at the end of this sheet.

def iterX(n):
    """
    Return the N'th term of the requested sequence using iteration
    """
    if n == 0 or n == 1:  # Base case
        return 1
    a = 1
    b = 1
    i = 0
    while i < n:
        a, b = b, a + 2 * b  # This is a tiny modification to the code for the Fibonacci sequence
        i += 1
    return a

###########################
# 10 Marks for the function
###########################


def recX(N):
    """
    Return the N'th term of the requested sequence using recursion
    """
    if N in [0, 1]:
        return 1
    return 2 * recX(N - 1) + recX(N - 2)

###########################
# 10 Marks for the function
###########################

for n in range(0, 11):
    print(recX(n), iterX(n), recX(n) == round(iterX(n), 0))

#################################
# 10 Marks for anything like this
#################################


#########################################################################
######## Here are some of the OTHER approaches for the iterative function

from math import sqrt  # Students might choose to use a different approach to calculating the square root


def iterX(N):
    """
    Return the N'th term of the requested sequence using iteration
    """
    term_1 = 1
    term_2 = 1
    for i in range(N):
        term_1 *= (1 - sqrt(2))
        term_2 *= (1 + sqrt(2))
    return (term_1 + term_2) / 2.0

### The following is also technically iterative:

def iterX(N):
    """
    Return the N'th term of the requested sequence using iteration
    """
    return ((1 + sqrt(2)) ** n + (1 - sqrt(2)) ** n) / 2.0
