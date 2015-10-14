---
layout     : post
categories : 2015-2016
title      : "2015-2016: Handout 3 - Attitude, division, indices, functions, while loops."
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- Functions;
- Comments;
- Lists, appending variables to lists, using list comprehensions;
- Dictionaries.

## Class test

**The class test counts for 40% of your mark for this module (that is a lot!).**

It will be a 50 minute test taking place between 1500 and 1700 on November the 6th.

## Infinite Loops

Some of you (surprisingly not that many) wrote code something like this:

{% highlight python %}
k = 0
i = 0
while k < 10:
    print i
    i += 1
{% endhighlight %}

This creates an infinite loop. To stop an infinite loop press the `ctrl` key and
then the letter `c`.

The correct code for the above would be something like:

{% highlight python %}
k = 0
i = 0
while k < 10:
    print i
    i += 1
    k += 1  # Without this line the boolean test for the while loop is never False
{% endhighlight %}

## Difference between global and local variables

There is a difference between **global** and **local** variables.

Consider the following function which calculates the polynomial \(x^2+bx+1\) for
some constant \(b\).

{% highlight python %}
b = 20

def pol(x):
    """A function to return the required polynomial"""
    return x ** 2 + b * x +1

print pol(1)
print b
{% endhighlight %}

Here the variable `b` is a **global** variable, executing `f(1)` gives `22`.

Here we are going to define a **local** variable:

{% highlight python %}
b = 20

def pol(x):
    """A function to return the required polynomial"""
    b = 1  # Here b is local variable
    return x ** 2 + b * x +1

print pol(1)
print b
{% endhighlight %}

Here we see that `pol(1)` gives `3` but the global variable `b` still has value
`20`.

This later is better written as:

{% highlight python %}
b = 20

def pol(x, b=1):
    """A function to return the required polynomial"""
    return x ** 2 + b * x +1

print pol(1)
print b
{% endhighlight %}

There we see that `b` is has a default value in `pol`.

Here is a nice explanation of global and local variables:
[http://www.python-course.eu/global_vs_local_variables.php](http://www.python-course.eu/global_vs_local_variables.php).

## Dictionaries and lists

Lists in Python are used to hold 'things' in a specific order.

{% highlight python %}
countriesiamnotfrom = ['Scotland', 'France', 'Wales', 'Ireland']
{% endhighlight %}

I can access the first element of that list with `countriesiamnotfrom[0]`.

Dictionaries are **efficient** ways of **mapping** `keys` to `values`. For
example the following maps the above countries to how much of a chance I think
they have of making the semi final of the world cup:

{% highlight python %}
chances = {'Scotland':0, 'France':.3, 'Wales':.35, 'Ireland':.65}
{% endhighlight %}

This is not held in memory in any particular way but python is able to
efficiently obtain the `value` corresponding to a given `key`. For example I can
get my value for `Ireland`: `chances['Ireland']`. **The order in which I create
`chances` is irrelevant.**

{% highlight python %}
countriesiamnotfrom = ['Wales', 'Scotland', 'Ireland', 'France']
chances = {'Wales':.35, 'France':.3, 'Scotland':0, 'Ireland':.65}
{% endhighlight %}

Running `countriesiamnotfrom[0]` now gives a different result to before but
`chances['Ireland']` does not.

You can think of this as how you would keep alphabetical order of phones
numbers.

- Use lists when order is important;
- Use dictionaries when order is not important but being able to quickly go from
  `keys` to `values` is.

## What you should do next:

- **Get started on the third sheet!**
- **I DO NOT RECOMMEND YOU ONLY APPEAR AT THE SECOND LAB SESSION!**
- Start revising for the class test:
    - Look through past handouts
    - Go over solutions to labs sheets (tickables and non tickables)
    - Look at the past class test
- Come and see me (Fri 1500-1700) during office hours.
