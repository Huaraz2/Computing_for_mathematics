---
layout      : post
categories  : solutions
title       : Week 4 - Solutions - Writing and Reading Files, Recursion and Algorithms
comments    : true
---


## Q1

{% highlight python %}
"""
Solution to question 1 of week 4 lab sheet.

"""

textfile = open('mytextfile.txt', 'w') # This opens the corresponding file in write mode. If the file does not exist it will create it.
for i in range(1, 11):
    textfile.write("%s\n" % i) # Write the string to the file including a '\n' which ensures a new line.
textfile.close() # Closes the file once all writing is complete.
{% endhighlight %}

## Q2

{% highlight python %}
"""
Solution to question 2 of week 4 lab sheet.

"""

textfile = open('mytextfile.txt', 'r') # Opens a file in read mode
string = textfile.read() # Reads the file, NOTE that this reads the file as a string, so the '\n' for new lines are also read.
print string # This prints the string to the screen, the IDLE interpreter however, knows how to display new lines (ie it reads the '\n').

data = string.split('\n') # This uses the split method which creates a list from a string, separating on a given string.
print data

data = [int(e) for e in data[:-1]] # Converting our sting to an integer.
print data
{% endhighlight %}

## Q3

{% highlight python %}
"""
Solution to question 3 of week 4 lab sheet.
"""


def isprime(n):
    """
    A function to return whether or not a number is prime.

    Arguments: n (an integer)

    Outputs: True or False
    """
    return min([n % e for e in range(2, n)]) != 0  # This checks that the remainder of all the numbers smaller than n is at least 1

print isprime(5)  # Returns true
print isprime(6)  # Returns false

# If students don't understand how the above works, invite them to not return
# the boolean but to return the list itself.

textfile = open('W03_D01.txt', 'r')  # Opens a file in read mode (students must use correct path)
string = textfile.read()  # Reads the file, NOTE that this reads the file as a string, so the '\n' for new lines are also read.
data = string.split('\n')  # Splits the file on the newline character
data = [int(e) for e in data[:-1]] # Removes last line and converts to integer

print len(data)

print len([e for e in data if isprime(e)])  # Uses function to check primes and also gives length
print len([e for e in set(data) if isprime(e)])  # Uses the set command to remove duplicates from data. Other approaches would make use of loops.
{% endhighlight %}

## Q4

{% highlight python %}
"""
Solution to question 4 of week 4 lab sheet.

This question asks students to work though the csv library. The solution here is a repeat of question 12 but using the csv library to import data.
"""
import csv  # This loads the csv library. It is good practice to load all libraries at beginning of script.


def isprime(n):
    """
    A function to return whether or not a number is prime.

    Arguments: n (an integer)

    Outputs: True or False
    """
    return min([n % e for e in range(2, n)]) != 0  # This checks that the remainder of all the numbers smaller than n is at least 1

textfile = open('W03_D01.txt', 'r')  # Opens a file in read mode (students must use correct path)
csvobject = csv.reader(textfile)  # Creates a csv reader object (in essence this replaces the split approach from previously)
data = [int(row[0]) for row in csvobject]  # Converts the csv reader object to data
textfile.close()

print len([e for e in data if isprime(e)])  # Uses function to check primes and also gives length
print len([e for e in set(data) if isprime(e)])  # Uses the set command to remove duplicates from data. Other approaches would make use of loops.
{% endhighlight %}

## Q5

{% highlight python %}
"""
Solution to question 5 of week 4 lab sheet.
"""

def iterX(n):
    """
    A function to give the sequence defined in q14 using an iterative approach

    Arguments: n, an integer

    Outputs: Xn where Xn is defined in q14
    """
    r = 1  # Setting a dummy variable
    for i in range(n - 1):  # Iterate over all integers less than n
        r *= 2  # Keep doubling r
    return r

print "Using iteration: f(3)=%s" % iterX(3)
print "Using iteration: f(40)=%s" % iterX(40)

def recX(n):
    """
    A function to give the sequence defined in q14 using a recursive approach

    Arguments: n, an integer

    Outputs: Xn where Xn is defined in q14
    """
    if n == 1:  # Identify the base case
        return 1
    return 2 * recX(n - 1)  # return 2*Xn-1 using the function itself

print "Using recursion: f(3)=%s" % recX(3)
print "Using recursion: f(40)=%s" % recX(40)
{% endhighlight %}

## Q6

{% highlight python %}
"""
Solution to question 6 of week 4 lab sheet.
"""

def iterfactorial(n):
    """
    A function to give n!, using iteration.

    Arguments: n, an integer

    Outputs: n!
    """
    r = 1  # Setting a dummy variable
    for i in range(1, n + 1):  # Iterate over all integers less than or equal to n
        r *= i  # Keep multiplying r by i
    return r

print "Using iteration: 3!=%s" % iterfactorial(3)
print "Using iteration: 40!=%s" % iterfactorial(40)

def recfactorial(n):
    """
    A function to give the function defined in q14 using a recursive approach

    Arguments: n, an integer

    Outputs: f(n) where f is defined in q14
    """
    if n == 1:  # Identify the base case
        return 1
    return n * recfactorial(n - 1)  # return n*(n-1)! using the function itself

print "Using iteration: 3!=%s" % recfactorial(3)
print "Using iteration: 40!=%s" % recfactorial(40)
{% endhighlight %}

## Q07

{% highlight python %}
"""
Solution to question 7 of week 4 lab sheet.
"""

def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:  # Check the base case
        return 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11):  # Printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i))
{% endhighlight %}

## Q08

{% highlight python %}
"""
Solution to question 8 of week 4 lab sheet.

"""

import random  # This imports the random libraru

jumbledlist = random.sample(range(1, 31), 20)  # Creates a random list of 20 elements from the integers 1 to 30
print "Here is a jumbled list: %s" % jumbledlist


def jumbledlist(maximumnumber, sizeoflist):
    """
    A function that returns a random shuffled list of integers

    Arguments:
        maximumnumber: the largest integer that can be sampled
        sizeoflist: the size of the list

    Outputs: A random list
    """
    return random.sample(range(1, maximumnumber + 1), sizeoflist)

print "Here is another jumbled list: %s" % jumbledlist(10, 5)
{% endhighlight %}


## Q09

{% highlight python %}

"""
Solution to question 9 of week 4 lab sheet.
"""

import random  # This imports the random library


def jumbledlist(maximumnumber, sizeoflist):
    """
    A function that returns a random shuffled list of integers

    Arguments:
        maximumnumber: the largest integer that can be sampled
        sizeoflist: the size of the list

    Outputs: A random list
    """
    return random.sample(range(1, maximumnumber + 1), sizeoflist)

l = jumbledlist(30, 20)  # Creates a jumbled list
print "A random list: %s" % l  # Print the list before sorting it
l.sort()
print "The above list (sorted): %s" % l  # Print the list after sorting it


# Here is the insertion sort algorithm:

def insertionsort(data):
    """
    A function to carry out the insertion sort algorithm.

    Arguments: A list

    Output: A sorted list
    """
    firstUnsorted = 0  # Initiate a marker to keep progress of algorithm
    while firstUnsorted < len(data) - 1:  # A while statement to keep sorting until algorithm is complete
        indexOfSmallest = firstUnsorted  # indexOfSmallest keeps track of location of smallest unsorted element
        index = firstUnsorted + 1  # We look for smallest element in unsorted elements
        while index <= len(data) - 1:  # A while statement to keep looking for smallest unsorted element
            if data[index] < data[indexOfSmallest]:  # Check if element is smaller than current smallest
                indexOfSmallest = index
            index += 1  # Search next element
        data[firstUnsorted], data[indexOfSmallest] = data[indexOfSmallest], data[firstUnsorted]  # Using synchronised assignment to swap two element
        firstUnsorted += 1

l = jumbledlist(30, 20)  # Creates a jumbled list
print "A random list: %s" % l  # Print the list before sorting it
insertionsort(l)
print "The above list (sorted): %s" % l  # Print the list after sorting it
{% endhighlight %}

## Q10

{% highlight python %}
"""
Solution to question 10 of week 4 lab sheet.
"""

import random  # This imports the random library


def jumbledlist(maximumnumber, sizeoflist):
    """
    A function that returns a random shuffled list of integers

    Arguments:
        maximumnumber: the largest integer that can be sampled
        sizeoflist: the size of the list

    Outputs: A random list
    """
    return random.sample(range(1, maximumnumber + 1), sizeoflist)

l = jumbledlist(30, 20)  # Creates a jumbled list
print "A random list: %s" % l  # Print the list before sorting it
l.sort()
print "The above list (sorted): %s" % l  # Print the list after sorting it

# Here is the bubble sort algorithm:


def bubblesort(data):
    firstUnsorted = 0  # Initiate a marker to keep progress of algorithm
    swap = True  # A boolean marker

    # The algorithm
    while firstUnsorted < (len(data) - 1) and swap:  # A while loop to keep sorting until algorithm is complete
        swap = False  # Set swap to False till swap two items
        index = len(data) - 1  # Look for element at end of data set
        while index > firstUnsorted:
            if data[index] < data[index - 1]:  # Check if elements should be swapped
                # Swapping two elements 'bubbling up'
                data[index], data[index - 1] = data[index - 1], data[index]
                swap = True
            index -= 1
        firstUnsorted += 1

l = jumbledlist(30, 20)  # Creates a jumbled list
print "A random list: %s" % l  # Print the list before sorting it
bubblesort(l)
print "The above list (sorted): %s" % l  # Print the list after sorting it
{% endhighlight %}

## Q11

{% highlight python %}
"""
Solution to question 11 of week 4 lab sheet.
"""

import time  # This import the time library

print "Current computer time is: %s" % time.time()  # This prints the current time to screen.


def timing(string):
    """
    A function to time the running of a string of python code

    Arguments: A string of python code

    Outputs: The time it took to run
    """
    starttime = time.time()
    eval(string)
    return time.time() - starttime


def testfunction():
    """
    A function that takes some time.

    Arguments: NA

    Output: NA
    """
    k = 0
    while k < 10 ** 6:  # Count to 10 ** 6
        k += 1


print "testfunction took %s seconds to run" % timing("testfunction()")


def timing(string):
    """
    A function to return the average time for the running of a string of python code over a set of runs.

    Arguments: A string of python code

    Outputs: The mean time to run over 10 repetitions
    """
    runtime = []
    for i in range(10):
        starttime = time.time()
        eval(string)
        runtime.append(time.time() - starttime)  # Append run time to list
    return sum(runtime) / len(runtime)  # Compute mean of list

print "testfunction took %s seconds to run over 10 runs" % timing("testfunction()")
{% endhighlight %}

## Q12

{% highlight python %}
"""
Solution to question 12 of week 4 lab sheet.

Invite students to search through the file by hand (open in any editor). The answer to 'if there were 2 searchers' is that students could divide the list in two and come up with answer sooner.
"""

f = open("W04_D01.txt", 'r')  # Open a file in read mode
data = f.read()  # Read the data as a string (if students want to use csv library: Great!)
f.close()  # Close the file

data = data.split("\n")  # Split on new lines
print data.index("4558\r")  # Print index, note the \r which is the symbol for carriage return. Students might have a hard time finding this so tell them to print the data to screen.
{% endhighlight %}

## Q13

{% highlight python %}
"""
Solution to question 13 of week 4 lab sheet.
"""


def sequentialsearch(data, item):
    """
    A function to return that sorts a list and returns index of item in sorted list.

    Arguments:
        data: a list
        item: an item to find in list

    Outputs: the index of item in the sorted list
    """
    data.sort()  # Students are welcome to use their own searching algorithm
    length = len(data)  # Set length to be size of data
    index = 0  # Set location of algorithm to 0
    found = False  # Create a boolean that is false until item is found
    while index < length and not found:  # Go through whole list until item is found or go past item that is larger then search target
        if data[index] == item:
            found = True
        elif data[index] > item:
            index = length
        else:
            index += 1
    if found:
        return index
    else:
        return False

# Load data:

f = open("W04_D01.txt", 'r')  # Open file in read mode
data = f.read()  # Read data
f.close()  # Close file
data = data.split('\n')  # Split on new lines
data = [int(e) for e in data[:-1]]  # Convert to integer

targets = [19,
           592,
           9507,
           4221]

for t in targets:
    index = sequentialsearch(data, t)
    if index:
        print 'target: %s is in position %s of sorted list.' % (t, index)
    else:
        print 'target: %s is not in list' % t
{% endhighlight %}

## Q14

{% highlight python %}
"""
Solution to question 14 of week 4 lab sheet.

"""


def binarysearch(data, item):
    """
    A function to carry out the binary search algorithm

    Arguments:
        data: a list
        item: an item to be searched for in the list

    Outputs: the index of item in the sorted list
    """
    data.sort()  # Sort the data set
    first = 0  # Index of first element in data set
    last = len(data) - 1  # Index of last element in data set
    found = False  # a boolean variable that is false until algorithm finds item
    while first <= last and not found:  # Carry on algorithm until 'bookends' do not meet or until item is found
        middle = int((first + last) / 2)  # Index of middle of the data set
        if item == data[middle]:  # Check if middle item is target
            found = True
        elif item < data[middle]:  # Two if statements to decide which half of data set to consider
            last = middle - 1
        else:
            first = middle + 1
    if data[middle] == item:
        return middle
    return False

data = range(345010)
print binarysearch(data, 64890)  # Student can play with algorithm in any way they see fit.
{% endhighlight %}

## Q15

{% highlight python %}
"""
Solution to question 15 of week 4 lab sheet.
"""
import random  # Importing random library for investigation later on
import time


def timing(string):
    """
    A function to return the average time for the running of a string of python code over a set of runs.

    Arguments: A string of python code

    Outputs: The mean time to run over 10 repetitions
    """
    runtime = []
    for i in range(10):
        starttime = time.time()
        eval(string)
        runtime.append(time.time() - starttime)  # Append run time to list
    return sum(runtime) / len(runtime)  # Compute mean of list


def sequentialsearch(data, item):
    """
    A function to return that sorts a list and returns index of item in sorted list.

    Arguments:
        data: a list
        item: an item to find in list

    Outputs: the index of item in the sorted list
    """
    data.sort()  # Students are welcome to use their own searching algorithm
    length = len(data)  # Set length to be size of data
    index = 0  # Set location of algorithm to 0
    found = False  # Create a boolean that is false until item is found
    while index < length and not found:  # Go through whole list until item is found or go past item that is larger then search target
        if data[index] == item:
            found = True
        elif data[index] > item:
            index = length
        else:
            index += 1
    if found:
        return index
    else:
        return False


def binarysearch(data, item):
    """
    A function to carry out the binary search algorithm

    Arguments:
        data: a list
        item: an item to be searched for in the list

    Outputs: the index of item in the sorted list
    """
    data.sort()  # Sort the data set
    first = 0  # Index of first element in data set
    last = len(data) - 1  # Index of last element in data set
    found = False  # a boolean variable that is false until algorithm finds item
    while first <= last and not found:  # Carry on algorithm until 'bookends' do not meet or until item is found
        middle = int((first + last) / 2)  # Index of middle of the data set
        if item == data[middle]:  # Check if middle item is target
            found = True
        elif item < data[middle]:  # Two if statements to decide which half of data set to consider
            last = middle - 1
        else:
            first = middle + 1
    if data[middle] == item:
        return middle
    return False

timedata = []
for i in range(1, 1001):
    target = random.randint(0, i)
    data = range(i)
    timedata.append([timing("sequentialsearch(%s, %s)" % (data, target)), timing("binarysearch(%s, %s)" % (data, target))])

print "Mean difference in timings: %s" % (sum([e[1] - e[0] for e in timedata]) / len(timedata))  # Small negative mean value indicates that binary search seems faster.
{% endhighlight %}

## Q16

{% highlight python %}
"""
Solution to question 16 of week 4 lab sheet.

"""

#!/usr/bin/env python
"""
Script for recursive binary search in a sorted array
"""


def binary_search(data, item, first=0, last=False):
    """
    A function to carry out binary search implemented in a binary way
    """
    data.sort()  # sort the data
    if not last:  # Need to check if last is default
        last = len(data) - 1
    if first > last:  # One base case (item not in list)
        return False
    middle = int((first + last) / 2)
    if item == data[middle]:  # Other base case (item is found)
        return middle
    if item < data[middle]:  # If item is before middle, carry out algorithm on first half of data
        return binary_search(data, item, first, middle)
    else:  # If item is after middle, carry out algorithm on second half of data
        return binary_search(data, item, middle, last)

data = range(10000)
print binary_search(data, 750)
{% endhighlight %}
