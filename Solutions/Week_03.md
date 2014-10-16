---
layout      : post
categories  : solutions
title       : Week 3 - Solutions - Functions and Data Structures
comments    : true
---


## Q1

{% highlight python %}
"""
Solution to question 01 of week 3 lab sheet.
"""

def printhello():
    print "Hello"

printhello()  # Run the above function

def printhello(name):
    print "Hello, " + name  # This concatenates the name and string 'Hello', students might use another approach for this which is also fine.

printhello("Vince")  # Run the above function

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q2

{% highlight python %}
"""
Solution to question 2 of week 3 lab sheet.
"""


def mydiv(a, b):
    return a / b  # Uses the return function which gives a value to the function but DOES not print anything

print mydiv(6, 3)  # Use print to print

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q3

{% highlight python %}
"""
Solution to question 3 of week 3 lab sheet.
"""

## TICKABLE ##

def mydiv(a, b):
    if b == 0:
        return "Cannot divide by 0"  # Uses a return in the if statement which ends the function
    return a / b  # Uses the return function which gives a value to the function but DOES not print anything

print mydiv(6, 0)  # Use print to print
print mydiv(6, 3)  # Use print to print

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q4

{% highlight python %}
"""
Solution to question 4 of week 3 lab sheet.
"""

## TICKABLE ##

def mysum(K=10000, B=3):  # Define function with default values
    s = 0
    k = 0
    while k < K:
        if k % B == 0:  # Check if B divides k
            s += k
        k += 1
    return s

print mysum(50,13)
print mysum()

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q5

{% highlight python %}
"""
Solution to question 5 week 3 lab sheet.
"""

# The first part of the question just asks to create a function around the code in q14.


def mysqrt(K, epsilon=.001):
    X = K / 4.0
    while abs(X ** 2 - K) > epsilon:
        X = (X + K / X) / 2
    return X

for n in range(1, 10001):  # A loop to test a bunch of values
    approx = mysqrt(n)
    true = n ** .5
    print approx, true, approx - true  # Printing the 3 results

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}

## Q6

{% highlight python %}
"""
Solution to question 6 of week 3 lab sheet.
"""

def fibonacci(n):
    if n == 0 or n == 1:  # Students might struggle with this (realising that the function needs an 'initial' value)
        return 1
    a = 1  # Setting two values that will be used to hold information in fibonacci calculation
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b  # This is an important step and some students might have difficulties with it
        i += 1
    return a

for i in range(10):  # Visualise output of function
    print fibonacci(i)

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
{% endhighlight %}


## Q10

{% highlight python %}
"""
Solution to question 10 of week 3 lab sheet.

"""

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # This assigns the list of integers from 1 to 10 to the variable alist

blist = [30, 40, 50, 60] # We assign another list to the variable blist
clist = alist + blist # This concatenates both previous lists (NOTE THAT IT DOES NOT CARRY OUT VECTOR ADDITION)
print "Here is clist: %s" % clist # Viewing clist
print "Length: %s" % len(clist) # Viewing the length of clist
print "The first element of clist: %s" % clist[0] # Obtaining the FIRST element of clist
print "The last element of clist: %s" % clist[-1] # Negative indices can be used to index from the last element.
print "The 4th to the 12th elements of clist: %s" % clist[3:12] # Two numbers can be used to obtain a sub list.

index = clist.index(40) # The index method finds the index of a particular element in a list (here '40'). Students have seen this before in strings.
print "The index of 40 in clist: %s" % index
print "A sublist containing clist and 1 more element: %s" % clist[index:index + 2] # Viewing the elements in clist from the index to 2 + the index.
{% endhighlight %}

## Q11

{% highlight python %}
"""
Solution to question 11 of week 3 lab sheet.

"""

mylist = [] # Create an empty list
for i in range(11): # Iterate over the integers from 0 to 10.
    if i % 2 == 0: # Use an if statement to check that i is even
        mylist.append(i) # If i is even append i to our empty list
print mylist # print the list
{% endhighlight %}

## Q12

{% highlight python %}
"""
Solution to question 12 of week 3 lab sheet.
"""

mylist = [] # Create an empty list
k = 0 # Create a counter
i = 0 # Create a counter
while k < 1300: # Count the first 1300 element
    if i % 3 == 0: # Check if i is a multiple of 3
        k += 1 # If i is a multiple of 3 increase counter
        mylist.append(i) # If i is a multiple of 3 append to list
    i += 1 # Increment i
print mylist
print max(mylist) # Obtain the largest of elements in the list

# Some student might try and do this with a for loop.
{% endhighlight %}

## Q13

{% highlight python %}
"""
Solution to question 13 of week 3 lab sheet.
"""

squares = [e ** 2 for e in range(1, 11)] # Create a list of squares using list comprehensions (very handy short hand in python)
print squares

squares = [e ** 2 for e in range(1, 11) if e % 2 == 1] # We can include a conditional statement in a list comprehension
print squares
{% endhighlight %}

## Q14

{% highlight python %}
"""
Solution to question 14 of week 3 lab sheet.
"""

def f(n): # Defining function from question. Ensure students use convention as specified in first lab sheet.
    """
    Defining function from question 5 of week 3 lab sheet.

    Arguments: n, an integer.

    Output: The output of the function is an integer according to the following formulae:
        if n odd: n^3
        if n divisible by 4: n^2 + 1
        otherwise: n - 1
    """
    if n % 2 == 1: # if statement to catch case and end function with return
        return n ** 3
    if n % 4 == 0:
        return n ** 2 + 1
    return n - 1 # A final return that catches all non matching cases

l = [f(n) for n in range(1,101)] # It is straightforward to create the list with this list comprehension
print l
{% endhighlight %}

## Q15

{% highlight python %}
"""
Solution to question 15 of week 3 lab sheet.

"""

alist = [1,74,2,100,-123]
print max(alist) # Note that some of these functions might be useful to students in previous exercises.
print min(alist)
print len(alist)
{% endhighlight %}

## Q16

{% highlight python %}
"""
Solution to question 16 of week 3 lab sheet.
"""

# This question aims to introduce students to dictionaries.

badphonebook = [["Vince", 3],
                ["Zoe", 2],
                ["Julien", 6],
                ["Thomas", 10],
                ["Mike", 1],
                ["Matt", 4]] # A bad phone book (list of lists). Note that the list is written over multiple lines (so that it is easier to read)

def searchpb(target):
    """
    A function to read through all elements in the above phonebook.

    Arguments: A string that will be searched for

    Output: The number corresponding to the string if it is in the phonebook.
    """
    for e in badphonebook: # Iterate through all elements in the phonebook.
        print "Checking %s" % e # Printing a statement for each element in the phonebook
        if e[0] == target: # If statement to check if the element is the target element
            return e[1]
    return "%s not in phonebook" % target # A statement to point out that the target is not in the phonebook


print searchpb("Mike") # Trying out some values
print searchpb("Ben")


goodphonebook = {"Vince": 3,
                    "Zoe": 2,
                    "Julien": 6,
                    "Thomas": 10,
                    "Mike": 1,
                    "Matt": 4} # A phonebook written as a dictionary

print goodphonebook.get("Thomas") # Using the get method to obtain the value corresponding to 'Thomas'
print goodphonebook.get("Brayden") # Using the get method to obtain the value corresponding to 'Brayden' (as it is not in the dictionary this will return 0)
print goodphonebook.get("Brayden", 'Not in book') # Setting a value to be return in case the value is not in the dictionary
print goodphonebook.get("Thomas", 'Not in book')


print goodphonebook['Vince'] # Checking the value of 'Vince'
goodphonebook['Vince'] = 8 # Changing the value of 'Vince'
print goodphonebook['Vince'] # Checking the new value of 'Vince'

print goodphonebook['Brayden'] # Note that 'Brayden' is not in the dictionary so this returns an error
goodphonebook['Brayden'] = 12
print goodphonebook['Brayden']
{% endhighlight %}

## Q17

{% highlight python %}
badphonebook = [["Vince", 3],
                ["Zoe", 2],
                ["Julien", 6],
                ["Thomas", 10],
                ["Mike", 1],
                ["Matt", 4]]

pb = {} # Creating an empty dictionary
for e in badphonebook: # Iterating over the lists in the bad phonebook
        pb[e[0]] = e[1] # Defining the value of the key corresponding to the name in the bar phonebook

print pb
{% endhighlight %}


## Q18

{% highlight python %}
"""
Solution to question 18 of week 3 lab sheet.

"""

goodphonebook = {"Vince": 3,
                    "Zoe": 2,
                    "Julien": 6,
                    "Thomas": 10,
                    "Mike": 1,
                    "Matt": 4}

for e in goodphonebook: # When iterating over a dictionary we iterate over the keys (but these are not necessarily in order).
    print goodphonebook[e]
{% endhighlight %}

## Challenge

{% highlight python %}
"""
This was an extra challenge given out in the week 2 lecture:

Write a function that returns a list with the indices of all occurrences of a substring in a given string.

Example of how it should work:

>>> string = 'Here is a sentence with the letter e appearing on multiple occasions.'
>>> print index_finder(string)
[1, 3, 11, 14, 17, 26, 29, 32, 35, 40, 57]
"""
def index_finder(string, substring):
    """
    Function that returns indices of all occurrences of a substring in a given string.

    Arguments:
        - string: a string that we want to search
        - substring: a string that we want to find

    Outputs:
        - A list of all indices
    """
    listofindices = []
    indx = 0
    while indx < len(string):
        if string[indx: indx + len(substring)] == substring:
            listofindices.append(indx)
        indx += 1
    return listofindices
{% endhighlight %}
