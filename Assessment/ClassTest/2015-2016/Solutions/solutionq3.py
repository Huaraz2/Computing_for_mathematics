"""
Solution to question 3 of the classtest

Marking for this question will again be lenient with marks given for methodology and 'almost working' answers.
"""

from math import sqrt, factorial

def f(n):
    return 9801.0 / sqrt(8) * (sum([(factorial((4*k))*(1103.0 + 26390 *
        k))/((factorial(k)) ** 4 * 396.0 ** (4 * k)) for k in range(n+1)])) ** (-1)

############################################################################
# Main difficulty here is getting factorial, extra marks if they go
# find it
# 20 marks
############################################################################

for n in range(10):
    print(f(n))
##########
# 10 marks
##########
