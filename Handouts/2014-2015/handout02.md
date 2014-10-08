---
layout     : post
categories : handouts
title      : Handout 1 - What you need to know
comments   : false
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

Script/idle/terminal etc...

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

(elif)

## Square root question
