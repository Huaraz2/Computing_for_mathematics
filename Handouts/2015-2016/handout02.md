---
layout     : post
categories : 2015-2016
title      : "2015-2016: Handout 2 - Slicing strings, modulo, types"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [gitter.im/drvinceknight/Computing_for_mathematics](https://gitter.im/drvinceknight/Computing_for_mathematics)

**Office hours: Friday 1500-1700**

## What you have learnt this week:

- Variables, variables types etc...
- What we can do to numeric variables;
- What we can do to strings;
- If statements;
- Loops (`for` and `while`);

# Slicing strings

In the last part of question 6 you had to do what is called 'slicing'. This
means taking out a portion of a string.

Here is an example:

{% highlight python %}
question = "Should vince do movember this november?"
{% endhighlight %}

Let us say that I want to 'cut' out the parts of the text that start where
"movember" starts.

First I need to find out where that position is:

{% highlight python %}
position = question.index("movember")
print(position)
{% endhighlight %}

This gives `16`. Let us take a look at the type of `position`:

{% highlight python %}
print(type(position))
{% endhighlight %}

We see that `position` is an integer.

We can get the sub string of our original string by going from that position to
the end (recall that in python the last element is at index `-1`):

{% highlight Python %}
print(question[16:-1])
{% endhighlight %}

This gives: `'movember this november'` **but** I could do that another way. In
this instance, `position` is just pointing at `16` anyway (they are both the
same integers). So this is the same as the previous statement:

{% highlight Python %}
print(question[position:-1])
{% endhighlight %}

I could also get the first 5 letters of "movember" from the substring:

{% highlight Python %}
print(question[position: position + 5])
{% endhighlight %}

which is just the same as:

{% highlight Python %}
print(question[16:21])
{% endhighlight %}

# Modulo arithmetic

You can get the remainder when dividing one number by another very easily in
Python:

{% highlight Python %}
for i in range(24):
    print(i % 12)
{% endhighlight %}

The above code loops through all numbers from 0 to 23 and displays the remainder
(mathematically referred to as modulus) when dividing by 12. This is basically
the same as looking at a clock: 1am is equivalent to 1 modulo 12 and 1pm is
equivalent to 13 module 12.

This can then be used to find the numbers that are divisible or not by another
number (they have remainder 0):

{% highlight Python %}
for i in range(24):
    if i % 12 != 0:
        print(i)
{% endhighlight %}

The above only displays the numbers that **are not** divisible by 12.
Note that the above is in fact equivalent to:

{% highlight Python %}
for i in range(24):
    remainder = i % 12
    is_not_divisible = remainder != 0
    if is_not_divisible:
        print(i)
{% endhighlight %}

The type of `is_not_divisible` in this case is `bool` (it's a boolean so is either `True`
or `False`).

# Question 13

A few people had an 'off by one' error in question 13. Take a look through the
solution but my main advice to everyone I spoke to was to do a simpler version
by hand:

> Write some code to find \\(N\\) such that \\(\sum\_{i=0}^Ni^2\\) is more than 10.

This can be done by hand very easily: \\(1^2=1\\), \\(1^2+2^2=5\\) but
\\(1^2+2^2+3^2=14\\) so \\(N=3\\).

What we have done here is take a counter: \\(i=1\\) and consider a sum \\(s\\).
We start by adding \\(i^2\\) to \\(s\\) to get \\(s=1\\). We check if
\\(s>10\\), as it's not we add 1 to our counter: \\(i=2\\) __and then__ add that
to \\(s=5\\). We check if \\(s>10\\), as it's not we add 1 to our counter:
\\(i=3\\) __and then__ add that to \\(s=14\\). We check if \\(s>10\\): it is, so
we know that \\(N=i=3\\).

The above is a description of how you would do this by hand. Once you have done
that it's relatively simple to write out the code (see the solution). If you had
an off by one error it was because you were adding to \\(s\\) __then__ adding to
\\(i\\) and __then__ checking \\(s\\).

## What you should do next:

- **Get started on the second sheet!**
- This one is slightly trickier so be sure to work on the sheets before you get
  to the labs (like most of you did for this first sheet).
- Make sure you **read** the question, watch the videos, read the handouts
  etc... Often it is the mathematics that is confusing and not the code.
- Come and see me (Fri 1500-1700) during office hours.

## Pydiff and Code Club

If you are interested in Python and/or other aspects of code take a look at:

- [pydiff.github.io/](http://pydiff.github.io/)
- [cardiffmathematicscodeclub.github.io/](http://cardiffmathematicscodeclub.github.io/)
