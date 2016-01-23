---
layout     : post
categories : 2015-2016
title      : "2015-2016: Handout 4 - Reading, functions, understanding
algorithms"
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

## Read, revise and document

This is a direct quote from one of the students tutors (who I ask every week to
give me feedback about the labs):

> 1) "Not reading the questions is the most frequent reason for
> unfinished/incorrect code. I will often ask someone to open a tickable and
> there will be a line or two of code copied straight from the first blue box on
> the lab sheet."

> 2) Some students don't seem to be aware that the work is progressive. They will
> be required to do something in a tickable that they have done before, but will
> often ask me how to do it before referring to their previous work.

> 3) Finally, I'm not sure how important you consider this compared to other
> issues but for some students the convention of commenting has never really been
> picked up. I'll be trying to look through a function with no comments at all and
> it can be very difficult to work out what the code is even trying to do as a
> result.

## Functions

Some functions return a value, other just do something to something (most do
both).

Here is an example of a function that adds 2 to all elements of a list:

{% highlight python %}
def add2tolist(data):
    n = len(data)
    for i in range(n):
        data[i] += 2
{% endhighlight %}

This does not **return** anything but it does change the given list:

{% highlight python %}
l = [1, 2, 3, 4]
print(l)
print add2tolist(l)  # This prints None as nothing is returned
print(l)
{% endhighlight %}

Similarly, a function can return something and leave other values unchanged
(remember what we spoke about last week with global and local variables):

{% highlight python %}
def givelistwith2added(data):
    newlist = [el + 2 for el in data]
    return newlist  # This function has a return
{% endhighlight %}

{% highlight python %}
l = [1, 2, 3, 4]
print(l)
print(givelistwith2added(l))  # Now returns a list
print(l)  # Is the same list
{% endhighlight %}

## Understanding algorithms

A lot of students came to see me this week saying "I do not understand the
code". For example for
[Q9](http://vknight.org/Computing_for_mathematics/Solutions/Week_04/#q09). With
these students I then walked through each line of the code: there was nothing
new and they agreed that it was straightforward code. It is not I recommend
reading over **previous lab sheets**.

**The first thing you should do when seeing a new algorithm/theorem/problem is
try and approach it by hand.**

## What you should do next:

- **Get started on the fourth sheet!**
- **I DO NOT RECOMMEND YOU ONLY APPEAR TO THE SECOND LAB SESSION!**
- Start revising for the class test: **make your own notes by going through the previous sheets/handouts and solutions**
- Come and me (Fri 1500-1700) during office hours.
