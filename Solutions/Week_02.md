---
layout      : post
categories  : solutions
title       : Week 2 - Solutions - Conditional Statements and Flow Control
comments    : true
---


## Q1

{% highlight python %}
"""
Solution to question 1 of week 2 lab sheet.

"""

# Relevant code to be typed directly in to interpreter:
print "Hello world"
{% endhighlight %}

## Q2

{% highlight python %}
"""
Solution to question 2 of week 2 lab sheet.
"""

print "Hello world"
{% endhighlight %}

## Q3

{% highlight python %}
"""
Solution to question 3 of week 2 lab sheet.
"""

## TICKABLE ##

num1 = 23
print type(num1)

num2 = 23.5
print type(num2)

str1 = "Hello world!"
print type(str1)

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q4

{% highlight python %}
"""
Solution to question 4 of week 2 lab sheet.
"""

num = 2  # Assigning the value 2 to the variable num
num = num + 3   # Adding 3 to num
print num  # Printing num


# This is the python 'shorthand' for doing the above:

num = 2  # Assing the value 2 to the variable num
num += 3  # Adding 3 to num
print num  # Printing num

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q5

{% highlight python %}
"""
Solution to question 5 of week 2 lab sheet.
"""

## TICKABLE ##

num = 5.2  # Assigning the value 5.2 to the variable num
num += 7   # Adding 7 to num
num *= 300   # Multiplying num by 300
num /= 4  # Dividing num by 3
num **= 3  # Raising num to the power of 3
print num  # Printing num

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q6

{% highlight python %}
"""
Solution to question 6 of week 2 lab sheet.
"""

## TICKABLE ##

str1 = "This is a string that I will learn to manipulate"  # Assign a string value to the variable str1
str2 = ", string manipulation is very useful."  # Assign a string value to the variable str2
string = str1 + str2  # Assign the concatenation of str1 and str2 to string (the syntax for this is particularly nice in python)
print string  # Print string
print len(string)  # Print the length of string (number of characters, including spaces)
print string[0]  # Obtaining the character in the first (index 0) position of string
print string[-1]  # The last character. Negative indices can be used to count from back.
print string[3:7]  # The string from index 3 to index (7 - 1).

index = str1.index("string")  # Use the index 'method' (don't worry too much about explaining what that is yet) to find index of 1st occurance of substring 'string' in str1
print index  # Print index
print str1[index:index + len("string")]  # print string

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q7

{% highlight python %}
"""
Solution to question 7 of week 2 lab sheet.
"""

f = 10.2  # Assigning a float to the variable f
print int(f)  # Modifying the float to an integet
print float(int(f))  # Modifying the integer to a float

s = str(f)  # Modifyng the float to a string and assigning it to s
print s  # Print sting
print type(s)  # Check the type of s

# Now some code to show how to generate strings:

numberofcats = 2
name = "Vince"
height = 1.7
notborn = "the UK"

# A way of using the above variable to create a string (encourage the students to change the values of some of the above variables to see effect on string below.

string = "My name is " + name + ", I am " + str(height) + " metres tall, have " + str(numberofcats) + " cats and was not born in " + notborn

# The better way:

string = "My name is %s, I am %.2f metres tall, have %i cats and was not born in %s" % (name, height, numberofcats, notborn)

# An explenation of the %s, %.2f and %i is in the lab sheet itself.

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q8

{% highlight python %}
"""
Solution to question 8 of week 2 lab sheet.
"""

boolean = True  # Assign the value True to the variable boolean
if boolean:  # Test boolean
        print "boolean is %s" % boolean  # Note the indentation

# Indentation is important in python

num = 11  # Assign the value 11 to num
print num % 2 == 0  # The % gives the reminder of a number when divided by another number. This prints the boolean variable corresponding to whether or not num is even.
if num % 2 == 0:  # Check boolean
    print "num is an even number"
else:
    print "num is an odd number"

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q9

{% highlight python %}
"""
Solution to question 9 of week 2 lab sheet.
"""

## TICKABLE ##

string = raw_input("Please input a string: ")  # Call for input from user
if len(string) > 10:
    print "that string has length strictly more than 10"
else:
    print "that string has length less than 9"

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q10

{% highlight python %}
"""
Solution to question 10 of week 2 lab sheet.
"""

print range(10)  # gives the list of integers from 0 to 9
print range(3, 10)  # gives the list of integers from 3 to 9
print range(0, 10, 2)  # gives the list of integers from 0 to 9 in steps of 2

# We can use the output of range (and any other list) to iterate using a for
# loop

for i in range(10):
    print i  # INDENTATION IS IMPORTANT!

for e in ["dog", "cat", 3, "I love mathematics"]:  # Can iterate over anything
    print e

s = 0
for i in range(1001):
    s += i  # Add all integers from 0 to 1000
print s

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q11

{% highlight python %}
"""
Solution to question 11 of week 2 lab sheet.
"""

## TICKABLE ##

s = 0
for i in range(1001):
    if i % 3 == 0:  # Note the double level of indentation (again this is important)
        s += i  # Add all integers if they are divisible by 3
print s

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q12

{% highlight python %}
"""
Solution to question 12 of week 2 lab sheet.
"""

k = 0
while k < 10:  # A while loop that checks a boolean prior to executing the indented statements
    print k
    k += 1  # Increment k

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q13

{% highlight python %}
"""
Solution to question 13 of week 2 lab sheet.
"""

## TICKABLE ##

n = 0
s = 0
while s < 20000:  # Run loop while s is smaller than 20000
    n += 1  # Increment n
    s += n ** 2  # Add n squared to s
    # print s, n #  This print statement would print out progress of the loop
print n

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening). It might be worth encouraging them to use a smaller value than 20000 and carry out operations by hand.
"""
{% endhighlight %}

## Q14

{% highlight python %}
"""
Solution to question 14 of week 2 lab sheet.
"""

K = 92  #This sets an initial value to take the square root of
X = K / 4.0  # This picks an initial value for the sequence, students might need a hand with this but try and get them to realise that they NEED a starting value (encourage them to work these things out by hand)
epsilon = .001  # This sets a level of precision but again students might not have realised they need one. I indicate that they need something in the video...
while abs(X**2 - K) > epsilon:
    X = (X + K / X) / 2
    print X

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q15

{% highlight python %}
"""
Solution to question 15 of week 2 lab sheet.
"""

import random  # Import the random library (an explanation of this was done in the video)

a = 0  # A lower bound on the integer to be picked
b = 1000  # A higher bound on the integer to be picked
value = random.randint(a, b)  # Use the random library to pick an integer
guess = input("Guess a number: ")  # Prompt the user to input a number, note that as the 'input' command is being used this will be read in a a python object. I.e. if a number is input then python knows this is a number.
while guess != value:  # Check that guess is not equal to value
    if guess > value:  # If the guess is too high prompt for a new value
        guess = input("Guess again, your previous guess was too high. ")
    else:  # Otherwise, ie if the guess was too low.
        guess = input("Guess again, your previous guess was too low. ")
print "Well done!"


"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}
