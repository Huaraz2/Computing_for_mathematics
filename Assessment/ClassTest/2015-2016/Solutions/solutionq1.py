"""
Solution to question 1 of class test

Marking for this exercise will be strict as the students were told multiple times during lectures that all they would need to do for question 1 of the class test is to copy a file from the solutions.
"""

def mysqrt(K, epsilon=.001):
    """
    A function to compute the square root of the input K for a given level of precision.
    """
    X = K / 4.0
    while abs(X ** 2 - K) > epsilon:
        X = (X + K / X) / 2
    return X

###########################################
# 20 marks for pasting the correct function
###########################################


for n in range(1, 10001):  # A loop to test a bunch of values
    approx = mysqrt(n)
    true = n ** .5
    print approx, true, approx - true  # Printing the 3 results

###########################################
# 10 marks for pasting the correct solution
###########################################
