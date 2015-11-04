---
layout     : post
categories : 2015-2016
title      : '2015-2016: Handout 6 - Sage and the Class test'
comments   : false
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- How to carry out basic algebraic operations in Sage (solve equations, simplify expressions etc...)

## Common error when multiplying

Some of you made the following mistake, that occurs because Sage needs to be
told when to multiply:

{% highlight python %}
5 * x  # This works
5x  # This does not
{% endhighlight %}

## Documentation

Some of you are still not documenting your code: **this will lose you marks in
the class test**. If you do not know how to do this please come and speak to me.

## Difference between exact and approximate computation

Question 4 asked you to carry out calculations **exactly**. This is something
that is possible to do in Sage but not immediately in Python.

Take a look at the following:

{% highlight python %}
x ^ (1/2)  # This is exact
{% endhighlight %}

{% highlight python %}
x ^ (.5)  # This is not exact
{% endhighlight %}

The end result of Q4, is just a number, using the second approach gets rid of
the exact value of things and uses approximations (very very precise
approximations but still approximations). Take a look at the solution to Q4 and
make sure you understand the difference.

## Other things about Sage

Do take a look at the two past years' handouts to other things that might be of
interest with regards to Sage.

- [2013-2014]({{site.baseurl}}/Handouts/2013-2014/handout06/)
- [2014-2015]({{site.baseurl}}/Handouts/2014-2015/handout06/)

## Class test

- The class test will be 3 questions with 30 marks for each question and 10 marks for correct conventions, commenting and documentation.
- You will submit your work using a folder on the Shared drive: *you won't have read or write rights to that folder* so you will only be able to submit once!
- You will also submit by emailing me: please get the subject of the email and the names of the files correct.

Contribute to the
[wiki](https://github.com/drvinceknight/Computing_for_mathematics/wiki). I know
some students are sharing notes: **THIS IS GREAT**, but if you do so by using
the wiki than at least you know for sure that the notes are correct (I will read
through them).

## What you should do next:

- **Finish revising for the class test**: be sure to be confident with the lab sheets 1 - 5 (Sage is not on the class test).
- **Start the next sheet**: this is a longer one looking at how to differentiate, integrate and plot in Sage.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear **please** come and see me during office hours.
