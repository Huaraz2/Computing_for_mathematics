---
layout     : post
categories : handouts
title      : Handout 3 - Attitude, division, indices, functions, while loops.
comments   : false
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

It will be a 50 minute test taking place between 1400 and 1500 on November the 7th.

## Books in the library

There is a huge amount of help on the internet, if you would also like to use books there are a bunch of them in the library:

![]({{site.baseurl}}/assets/Images/library_books.jpg)

## Attitude

You **must** get to the lab having completed your tickables to gain the most from them.
**I recommend coming to at least the first lab session as this gives you time to address what needs addressing to get your ticks**.
One student only came to the second lab and with 5 minutes to go asked me to look at their tickables.
I then checked their understanding of what they had written and ended up giving them no ticks.

Here are some quotes from an email from one of the undergraduate tutors:

> [...] Not just for this module but all of their first year modules. I only say this from experience, as unfortunately I failed 4 of my 5 January exams, and had I not turned it around in the second semester, and also spent 7 weeks in the summer in Cardiff revising for resits, I would never have made it into second year. The resits are completely unavoidable, as I have no doubt whatsoever in saying that I believe every single first year at the moment is capable of getting a 2:1 or a 1st if they put the necessary work in.

> [...]  I now understand the privilege of attending such a fantastic Russell Group university, and it would be a shame to see students make the same mistake that I did in my first semester. I don’t know whether the students are aware of how the credit system works, as if they fail this 20 credit module, they would have to redo it again next year, or repeat the year if they fail over 20 credits.

**If you have difficulties with the course please come and see me.**
Recall that to get a tick you do not need to succeed the task, however you do need to show that you have worked.
(On multiple occasions I refused ticks to students because they were unable to answer a simple question, the answer of which I say very clearly in the corresponding video.)

## Division in python

Note that the output of division in Python depends on the types of variables input:

{% highlight python %}
a = 5
b = 2
print a / b
{% endhighlight %}

The above does not return `5/2` but:

{% highlight python %}
2
{% endhighlight %}

If however we tell Python that one of the inputs is a float we obtain the result as a float:

{% highlight python %}
a = 5
b = float(2)
print a / b
{% endhighlight %}

the above gives:

{% highlight python %}
2.5
{% endhighlight %}

**Be careful with this as it's very easy to make a mistake as a result of this.**

## Indices of lists

Indices with lists work in the exact same way as they do for strings.

{% highlight python %}
myfavouritenumbers = [12, 5, 8, 41, 13, 7]
{% endhighlight %}

To get the first element:

{% highlight python %}
print myfavouritenumbers[0]
{% endhighlight %}

To get the second element:

{% highlight python %}
print myfavouritenumbers[1]
{% endhighlight %}

To get the 3rd till the 5th element:

{% highlight python %}
print myfavouritenumbers[2:5]
{% endhighlight %}

We can also use negative numbers to 'count from the end'.
This gives us the 2nd from last element:

{% highlight python %}
print myfavouritenumbers[-2]
{% endhighlight %}

## Simultaneous assignment

Let's start with two consecutive elements of the Fibonacci sequance `a=5` and `b=8`.

In the solutions to the Fibonacci question we use the following:

{% highlight python %}
a = 5
b = 8
a, b = b, a + b
{% endhighlight %}

At this point we have `a=8` and `b=13` **because we did the assignment at the same time.

The following approach (doing the assignment one after the other) would not work:

{% highlight python %}
a = 5
b = 8
a = b  # At this point a is 8
b = a + b  # So that is just like writing b = b + b, which sets b to 16
{% endhighlight %}

We can though do without simultaneous assignment using a third variable:

{% highlight python %}
a = 5
b = 8
old_a = a
a = b
b = old_a + b
{% endhighlight %}

## Adding particular elements to a list

Here is a way of obtaining the first 10 integers divisible by 4:

{% highlight python %}
mylist = []  # Initiate an empty list that will hold all the number divisible by 4
count = 0  # Initiate a variable that will keep track of the count of numbers divisible by 4 we have
nbr = 0  # Initiate a variable that we will increment and check
while count < 10:  # Keep looping until we have enough numbers divisible by 4
    nbr += 1  # This increments the number we are checking
    if nbr % 4 == 0:  # Checks if the number is divisible by 4
        mylist.append(nbr)  # If it is divisible by 4 we append to our list
        count += 1  # If it is divisible by 4 we increment the counter
{% endhighlight %}

We can equivalently do this this way:

{% highlight python %}
mylist = []   # Initiate an empty list that will hold all the number divisible by 4
nbr = 0  # Initiate a variable that will keep track of the count of numbers divisible by 4 we have
while len(nbr) < 10:  # Keep looping until we have enough numbers in our list
    if nbr % 4 == 0:  # Checks if the number is divisible by 4
        mylist.append(nbr)  # If it is divisible by 4 we append to our list
{% endhighlight %}

## Functions (defining and calling)

There is a difference between **defining** and **using** a function.
Be sure to understand that difference (relevant to question 14 of [week 3]({{site.baseurl}}/LabSheets/Week_03/)

## What you should do next:

- **Get started on the third sheet!**
- **I DO NOT RECOMMEND YOU ONLY APPEAR TO THE SECOND LAB SESSION!**
- Start revising for the class test.
- Come and see Jason (Wed 1300-1500) and/or I (Thu 1300-1500) during office hours.
