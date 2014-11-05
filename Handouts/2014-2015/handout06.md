---
layout     : post
categories : [handouts, 2014-2015]
title      : 'Handout 6 - Sage and the Class test'
comments   : false
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- How to carry out basic algebraic operations in Sage (solve equations, simplify expressions etc...)

## What is Sage?

- Sage is a mathematics package built on Python. This implies that you can use the Python code you learnt in the first weeks of this class in Sage.
- Sage can be used to check formulae. For example: what is the formula for \\(\sum_{i=0}^{\infty}ix^{i-1}\\)?

        {% raw %}
        i = var('i')
        sum(i * x ^ (i - 1), i, 0, infinity)
        {% endraw %}

- Sage can also be used to plot functions (this could help when attempting to visualise a particular theorem):

        {% raw %}
        k = 20
        p = plot(x^0,color=rainbow(20)[0], legend_label="$x^0$")
        for i in range(1,20):
            p += plot(x^i,color=rainbow(20)[i],legend_label="$x^{%s}$" % i)
        p
        {% endraw %}

    Here is something a bit more visually impressive (the code is slightly more compact as it uses some Sage tricks):

        k = 20
        rb = rainbow(k+1)
        sum(plot(sin(i*x)*i,color=rb[k-i], legend_label=r"${0}\sin({0}x)$".format(i)) for i in [0..k])

- Sage is a tool available to you to help you through your time at Cardiff.

## Solving equations

A variety of equations exist that cannot be solved algebraically.
Here is one example of this:

$$
x + \log(x) = 6
$$

Here is how we'd ask sage to solve it:

{% highlight python %}
solve(x + log(x) == 6, x)
{% endhighlight %}

We get nothing helpful:

{% highlight python %}
[x == -log(x) + 6]
{% endhighlight %}

Finding a solution to this equation is equivalent to finding a 'root' (also called: a 'zero') of the function \\(f(x)=x+\log(x)-6\\).
Let's take a look at this function:

{% highlight python %}
f(x) = x + log(x) - 6
plot(f,x,0,100)
{% endhighlight %}

We get:

![]({{site.baseurl}}/assets/Images/plot_of_non_algebraically_solvable_equation.svg)

which obviously has a root, which looks to be for \\(5<x<15\\), so here's how we can get sage to find it numerically:

{% highlight python %}
find_root(f,5,15)
{% endhighlight %}

## Typeset mode

You can turn on the 'nicer' display of mathematics using:

{% highlight python %}
typeset_mode(true)
{% endhighlight %}

Note that this displays the mathematical output using something called LaTeX which you will learn in Week 10.
It is nice to look at but isn't terribly useful: know when and when not to use it (simply replace `true` by `false`).

## Markdown

You can include the tag `%md` to write in a language called __markdown__ in a cell.
This allows you to make your worksheets look a bit nicer.
Here is an example:

{% highlight html %}
%md
# Q1
This is where I will write my answer to Q1 of [this lab sheet](http://vincent-knight.com/Computing_for_mathematics/LabSheets/Week_07/).
{% endhighlight %}

If you would like to learn more markdown take a look at this video: [https://www.youtube.com/watch?v=6A5EpqqDOdk](https://www.youtube.com/watch?v=6A5EpqqDOdk).

## Installing Sage locally

Some of you have asked to install sage on your own machine, here is a video showing how to do this on Mac OS: [https://www.youtube.com/watch?v=Z_gWgCoChC8](https://www.youtube.com/watch?v=Z_gWgCoChC8).

The process on Linux is very similar (feel free to ask me), I'm afraid that I've never done it on Windows but it is possible.

## Class test

- The class test will be 3 questions with 30 marks for each question and 10 marks for correct conventions, commenting and documentation.
- You will submit your work using a folder on the Shared drive: *you won't have read or write rights to that folder* so you will only be able to submit once!
- You will also submit by emailing me: please get the subject of the email and the names of the files correct.

## What you should do next:

- **Finish revising for the class test**: be sure to be confident with the lab sheets 1 - 5 (Sage is not on the class test).
- **Start the next sheet**: this is a longer one looking at how to differentiate, integrate and plot in Sage.
- Contribute to the wiki.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear **please** come and see me during office hours.
