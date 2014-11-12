"""
Solution to question 3 of the classtest

Marking for this question will again be lenient with marks given for methodology and 'almost working' answers.
"""

def isperfect(n):
    """
    A function to check if a number is perfect or not.

    Arguments: n - an integer

    Output: boolean
    """
    return sum([k for k in range(1, n) if n % k == 0]) == n

# 20 marks for getting that function correct - but I expect very few answers will be that compact and also few will be correct (but marks still available)

print "There are %s perfect numbers less than 10000" % len([n for n in range(1, 10001) if isperfect(n)])

# 10 marks for the above: again I expect students won't use a list comprehension but might make use of a for loop (which is fine):

count = 0
for k in range(1, 10001):  # If they're off by one don't penalise too heavily
    if isperfect(k):
        print "%s is perfect" % k  # This outputs the perfect number to screen which was not asked
        count += 1

print "There are %s perfect numbers less than 10000" % count
