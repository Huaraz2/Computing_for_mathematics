---
layout     : post
categories : handouts
title      : Handout 4 - Functions, dummy variables and building lists from other lists
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- Write data to a file using the write and read functions;
- Use the csv python module to read and write csv files;
- Program some basic algorithms using recurrence;
- Insertion and Bubble sort algorithms;
- Binary search.

## Some confusion about using functions on lists

Here is the solution to question 11 from Week 3:

{% highlight python %}
mylist = [] # Create an empty list
for i in range(11): # Iterate over the integers from 0 to 10.
    if i % 2 == 0: # Use an if statement to check that i is even
            mylist.append(i) # If i is even append i to our empty list
            print mylist # print the list
{% endhighlight %}

The above creates an empty list `mylist` and takes all elements from the list containing the integers from 0 to 10 (`range(11)`), and putting the ones that are even (`i % 2 == 0`) in to the empty list.

Let's try and do something similar.
We will find all elements less than 5 from a given list:

{% highlight python %}

def biggerthanfive(n):
    """
    A function that returns the boolean corresponding to whether or not a number is bigger than 5.

    Arguments: n (a number)

    Outputs: a boolean
    """
    return n > 5

givenlist = [313, 398, 228, 218, 9, 49, 180, 156, 165, 307, 323, 208, 72, 454, 35, 280, 258, 4, 242, 407, 124, 452, 469, 275, 290, 387, 251, 74, 278, 300, 279, 319, 468, 410, 97, 338, 498, 1, 473, 154, 317, 408, 463, 6, 61, 497, 202, 155, 470, 40, 31, 238, 126, 457, 358, 492, 135, 486, 8, 237, 296, 382, 447, 244, 445, 448, 235, 372, 286, 62, 178, 330, 415, 166, 405, 150, 107, 257, 78, 85, 461, 409, 352, 437, 41, 404, 91, 265, 357, 132, 252, 105, 499, 402, 362, 224, 69, 93, 263, 462]

mylist = []  # Create an empty list
for dummyvariable in givenlist:  # Iterate over the elements of the givenlist
    if biggerthanfive(dummyvariable):  # Use an if statement coupled with our previously defined function
        mylist.append(dummyvariable)  # If the dummyvariable is bigger than five then append to our empty list
print mylist  # print the list

{% endhighlight %}

You should hopefully be able to see that the two are very similar and in fact are similar to Q3 of week 4's lab sheet.

**Note** that we can do the above using list comprehensions as well:

{% highlight python %}
mylist = [k for k in givenlist]
{% endhighlight %}

The above just 'copies' every element from `givenlist` in to a new list called `mylist`.
That's not quite what we want.
We can use python syntax that is very similar to the mathematical convention:

$$
\{x\in S\;|\text{ some condition on x}\}
$$

{% highlight python %}
mylist = [k for k in givenlist if biggerthanfive(x)]
{% endhighlight %}

Of course, because our `biggerthanfive` function is very very simple we would probably just write:

{% highlight python %}
mylist = [k for k in givenlist if x > 5]
{% endhighlight %}

## Dummy variables

You can see in the above example that the dummy variable `i` and/or `dummyvariable` is used interchangeably.
This is similar to mathematical notation:


$$
\sum_{i=0}^ni = \sum_{k=0}^{n}k=\sum_{j=1}^{n+1}j-1
$$

So the following code snippets all do the same thing:

{% highlight python %}
# Using i as a dummy variable:
for i in range(10):
    print i

# Using j as a dummy variable:
for j in range(10):
    print j

# Using ninja as a dummy variable:
for ninja in range(10):
    print ninja
{% endhighlight %}

## Functions

A variety of students are still confused by functions (highlighted by difficulties with Q8 on week 4's session).
Take a look at the various handouts that I wrote last year to clarify this.

In general it is straightforward to modify code that does things for 1 or 2 specific values and make it a function.

The following finds all natural numbers less than 20 than are divisible by 2 and 5:

{% highlight python %}
numbers = range(1, 21)
mylist = []
for k in numbers:
    if k % 2 == 0 and k % 5 == 0:
        mylist.append(k)
print mylist
{% endhighlight %}

Here is a function that returns a list of all natural numbers than `K` that are divisible by `r` and `s`:

{% highlight python %}
def divisiblefunction(K, r, s):
    numbers = range(1, K + 1)
    mylist = []
    for k in numbers:
        if k % r == 0 and k % s == 0:
            mylist.append(k)
    return mylist
{% endhighlight %}

We can use that function to get the same result as above (but also other values if we wanted them):

{% highlight python %}
print divisiblefunction(20, 2, 5)
{% endhighlight %}

Compare this to the solution of question 8 and make sure you're comfortable with functions.

## Searching algorithms

We saw binary search this week which relies on constantly ‘dividing’ a list in to two smaller lists:

![]({{site.baseurl}}/Handouts/2013-2014/Images/binary.svg)

## What you should do next:

- **Get started on the fourth sheet!**
- **I DO NOT RECOMMEND YOU ONLY APPEAR TO THE SECOND LAB SESSION!**
- Start revising for the class test: **make your own notes by going through the previous sheets/handouts and solutions**
- Come and see Jason (Wed 1300-1500) and/or I (Thu 1300-1500) during office hours.
