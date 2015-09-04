---
layout     : post
categories : 2014-2015
title      : '2014-2015: Handout 7 - Tangent lines and using data'
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- How to plot in Sage (domain of plot and ‘addition’ of plots);
- How to obtain limits in Sage;
- How to differentiate in Sage;
- How to integrate in Sage;
- How to to upload data to Sage.

## Solutions

Be sure to look at the Sage solutions: you can copy them in to your own project.
The solutions to the class test are also available online.

## Tangent lines

Most of the difficulty this week was due to difficulties with mathematical concepts.
Here is an overview of how to find the equation of a straight line tangent to a function \\(f\\) at the point \\(x=a\\).

Let the straight line be \\(g(x)=mx+b\\) for some \\(m\\) and \\(b\\) which will be functions of \\(f\\) and \\(a\\).
By definition of the derivative \\(m=\frac{df}{dx}(a)\\) (which we will write as \\(f'(a)\\) for short).
Thus:

$$g(x)=f'(a)x+b$$

To obtain \\(b\\) we need a single point \\(x\\) for which we know the value of \\(g(x)\\) so that we would have:

$$
b=g(x)-f'(a)x
$$

Thankfully, we know that \\(g\\) and \\(f\\) intersect at \\(x=a\\) thus \\(g(a)=f(a)\\) so we have:

$$
b=f(a)-f'(a)a
$$

putting this all together gives the equation of the tangent to \\(f\\) at \\(x=a\\):

$$
g(x)=f'(a)x+f(a)-f'(a)a
$$

Take a look at the solutions to see how I coded that.

## Using data

Q9 on this lab sheet seemed to be quite challenging.
It is **extremely** similar to a variety of things we have done previously and here is another example.

Consider the following data set which holds list of `[a,b,c]` for the quadratic of the form \\(ax^2+bx+c\\):

{% highlight python %}
data = [[1, 2, 3], [4, 5, 1], [6, 5, 3], [7, 8, 1], [0, 2, 1]]
{% endhighlight %}

For the above data set let us calculate the mean value of the derivative of our quadratic at the point \\(x=5\\).

{% highlight python %}
class datadiff():  # There is no need to create a class to do this however using classes is to be encouraged and allows for nice manipulation further on
    """
    A class for each integral.

    Methods: init

    Attributes:
        a: coefficient of x ^ 2
        b: coefficient of x
        c: coefficient of x ^ 0


    """
    def __init__(self, a, b, c):
        """
        Initialisation method.

        Arguments:
            a: coefficient of x ^ 2
            b: coefficient of x
            c: coefficient of x ^ 0
            derivativeat5: the value of the derivative at x=5
        """
        self.a = a
        self.b = b
        self.c = c
        self.derivativeat5 = diff(a * x ^ 2 + b * x + c, x).subs(x=5)
{% endhighlight %}

Now that we have our class let us create a list of our instances.

{% highlight python %}
instances = [datadiff(row[0], row[1], row[2]) for row in data]
{% endhighlight %}

We can now easily get the mean of the derivative:

{% highlight python %}
mean([dd.derivativeat5 for dd in instances])
{% endhighlight %}

## Individual coursework

The next piece of assessment is some individual coursework which is due at the end of Week 11.
You can find instructions and examples of past work: [http://vincent-knight.com/Computing_for_mathematics/Assessment/](http://vincent-knight.com/Computing_for_mathematics/Assessment/) (under 'Individual Coursework').
You will be required to use LaTeX which is what is the subject of Week 10.
You can start thinking about a particular subject and run that by me if you want.

## What you should do next:

- Start thinking about the individual coursework
- Start the next sheet: make sure you spend time working on the sheet BEFORE the labs.
- Contribute to the wiki.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear please come and see me during office hours.
