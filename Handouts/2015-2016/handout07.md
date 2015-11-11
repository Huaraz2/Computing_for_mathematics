---
layout     : post
categories : 2015-2016
title      : '2015-2016: Handout 7 - A level calculus, debugging and class test'
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

## Tangent lines

**This is a repetition of last years lab sheet so this was available to you**

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

## Debugging

A lot of student write all their code in one go and in one cell. When the code
is then run it is difficult/impossible to debug.

Consider the problem below:

> Obtain a plot showing the number of primes less than or equal to \\(n\\) for
> \\(n\leq 100\\). After that, obtain the plot of the number of primes less than
> or equal to \\(n\\) divided by \\(n\\).

Here is an example of how all this code could be thrown together in one go
(**there are errors**):

{% highlight python %}
def find_primes(n)
    """Find primes up till n"""
    for i in range(n + 1):
        if is_prime(i):
            count += 1

# Let's now get the plot of number of primes:

plot = plot(find_primes(n) for n in range(100), title="Number of primes)
plot

# Now for the other plot

plot = plot(find_primes(n) / n for n in range(100), title="Number of primes divided by N)
plot

{% endhighlight %}

If we just run that we get all sorts of errors that are hard to identify. You
can see this at this [sage
worksheet](https://cloud.sagemath.com/projects/3b2249d5-a951-4f25-979a-571f71ccdde6/files/debugging.sagews).
**It is important to write small pieces of code at a time and slowly build
things up: THERE IS NOTHING MAGIC ABOUT CODE**.  I will debug that in class (so
that link will show how the code **should** be written once I'm done).

## Individual coursework

The next piece of assessment is some individual coursework which is due at the end of Week 11.
You can find instructions and examples of past work: [http://vincent-knight.com/Computing_for_mathematics/Assessment/](http://vincent-knight.com/Computing_for_mathematics/Assessment/) (under 'Individual Coursework').
You will be required to use LaTeX which is what is the subject of Week 10.
You can start thinking about a particular subject and run that by me if you want.

## Class test

Here are some summary statistics about the class test marks:

- Total mark:

    - mean: 57.66
    - median: 55.00
    - max: 100.00

- q1 mark:

    - mean: 66.36
    - median: 100.00
    - Best: 100.00

- q2 mark:

    - mean: 59.10
    - median: 60.00
    - Best: 100.00

- q3 mark:

    - mean: 37.54
    - median: 30.00
    - Best: 100.00

- Documentation mark:

    - mean: 87.54
    - median: 90.00
    - Best: 100.00

Percentage of marks above given mark:

- 0.77 of students \\(\geq\\) 40%
- 0.63 of students \\(\geq\\) 50%
- 0.45 of students \\(\geq\\) 60%
- 0.33 of students \\(\geq\\) 70%
- 0.19 of students \\(\geq\\) 80%
- 0.10 of students \\(\geq\\) 90%

A picture of the distribution of the marks:

![]({{site.baseurl}}/Handouts/2015-2016/Images/classtestmarkdistribution-2015-2016.svg)

## What you should do next:

- Start thinking about the individual coursework
- Start the next sheet: make sure you spend time working on the sheet BEFORE the labs.
- Contribute to the wiki.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear please come and see me during office hours.
