---
layout     : post
categories : handouts
title      : Handout 2 - Indexing a string, if statements and an algorithm for a sqaure root.
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- Variables, variables types etc...
- What we can do to numeric variables;
- What we can do to strings;
- If statements;
- Loops (`for` and `while`);

## Saving files

When you save a python script make sure to include the `.py` extension. This ensures that IDLE will be able to open it.

## Running files

On Windows when you double click a `.py` file (and if you haven't changed your settings) it will automatically execute the script in the terminal (that's the flashing black window).

Write this code snippet and double click on it to see what I mean (this code forces a break by asking for some input):

{% highlight python %}
k = raw_input('Hi!')
{% endhighlight %}

## Finding things in strings

In question 6 on the lab sheet the last 3 lines of code used the `index` method on a string.
This is used to find the location of a smaller string in a string.

{% highlight python %}
string = 'abcdefghjkl'
k = string.index('e')
print k
{% endhighlight %}

The above would output:

{% highlight python %}
4
{% endhighlight %}

Similarly we could also look for the position of substring `efghj`:

{% highlight python %}
k = string.index('efghj')
print k
{% endhighlight %}

The above would produce the same result.

If we try to find a substring that is not in the overall string we get an error:

{% highlight python %}
string.index('vince')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found
{% endhighlight %}

We could avoid the above error by checking if the substring is actually in the string before using the `index` method:

{% highlight python %}
if 'vince' in string:
    print string.index('vince')
else:
    print 'Not in string'
{% endhighlight %}

Understanding how indexing work is an important part of this course as the same approach is used with `lists` (something in the next lab sheet).

## If statements as gates

`if` statements allow us to check certain conditions and execute commands according to the value of a boolean.

{% highlight python %}
mood = 'Happy'

if mood == 'Happy':
    print 'Tick all the tickables!'
{% endhighlight %}

We can use `if` statements in conjunction with the `elif` and `else` command to evaluate alternatives:

{% highlight python %}
mood = 'Grumpy'

if mood == 'Happy':
    print 'Tick all the tickables!'
elif mood == 'Grumpy':
    print 'No ticks...'
else:
    print 'Who knows...'
{% endhighlight %}

## The square root question

Quite a few of you tried the square root question (which is awesome).
Take a look at the solutions and let me know if it's not clear.

## What you should do next:

- **Get started on the second sheet!**
- This one is slightly trickier so be sure to work on the sheets before you get to the labs (like most of you did for this first sheet).
- Come and see Jason (Wed 1300-1500) and/or I (Thu 1300-1500) during office hours.
