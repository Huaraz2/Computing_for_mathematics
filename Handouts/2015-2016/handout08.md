---
layout     : post
categories : 2015-2016
title      : '2015-2016: Handout 8 - Reading, Q8, and the individual coursework.'
comments   : true
---
Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Friday 1500-1700**

## What you have learnt this week:

- You learnt about the mathematical topic of linear algebra;
- You saw how to make relevant calculations in Sage:

    - Determinant
    - Inverse

## Reading

Still the main piece of feedback I am getting from tutors is that students are
not reading questions properly. Here is something that one of the student tutors
wrote:

> I thought of a couple of general things you should stress to your students (to
> make up for the fact I didn't send you feedback Wednesday).  I know you've
> probably already told them to read the question twice/thrice before attempting
> it, but they still aren't. A lot of problems occur from students just not
> having read what is expected. Also, I would say the majority of people who
> struggle with computing, it's still the same in my programming module this
> year, are the ones who can't get their heads around the question.  The pen and
> paper process is so useful, and I don't know how many people are actually
> trying it when they get stuck. Also, accepting that you're going to get it
> wrong 30 times before you get it right. That's just computing.

I would make one change to this tutor's quote:

> That's just mathematics.

## Creating patterns

Modern mathematical theory is often developed thanks to the use of a computer
package like Sage.

Take a look at [this blog post about proving a condition for divisibility by 11,
it's a small example of how modern mathematics is carried out](http://vknight.org/unpeudemath/code/2014/11/22/on-divisibility-by-11/).


## Repeating actions over a list

Q8 caused a few difficulties for some students.  This question was very similar
to questions we have done multiple times: taking something from one list, doing
something to it and then putting it in another list.  The only difference in
this instance was that the 'doing something' was perhaps a bit complicated but
nothing more complicated than we had done before.

Let us consider the following similar problem:

> Write to file a data set with 10000 rows of the following columns:

{% highlight python %}
alpha, beta, gamma
{% endhighlight %}

> Where \\(\alpha, \beta\\) are random integers between 0 and 10 and
> \\(\gamma\\) is a random reel number between 0 and 1.

> Once you have written that file, read in the data and calculate the average
> of:

$$
\left.\frac{d(\alpha x^{\beta})}{dx}\right|_{x=\gamma}\
$$

Here is a class:

{% highlight python %}
import random
import csv

class RandomParameters:
    """A class for a random parameter set"""
    def __init__(self):
        self.alpha = random.randint(0, 10)
        self.beta = random.randint(0, 10)
        self.gamma = random.random()

f = open('file.csv', 'w')  # Open a file in write mode
csvwrtr = csv.writer(f)  # Create a csv writer instance
for row in range(10000):  # Loop over 10000 instances
    rp = RandomParameters()  # Create a random instance
    csvwrtr.writerow([rp.alpha, rp.beta, rp.gamma])  # Write these parameters to file
f.close()  # Close the file
{% endhighlight %}

Now let us read in that data file and calculate the observed average.

{% highlight python %}
import csv

class ParameterSet:
    """A class for a given parameter set"""
    def __init__(self, alpha, beta, gamma):
        self.deriv = diff(alpha * (x ^ \beta), x).subs(x=gamma)

f = open('file.csv', 'r')  # Open the file in read mode
csvrdr = csv.reader(f)  # Create a reader instance
data = [ParameterSet(eval(row([0]), eval(row[1]), eval(row[2]) for row in csvrdr]  # Get the data
print mean(data)  # Obtain the mean
{% endhighlight %}

Note that we can check if this result what we expect:

$$
\left.\frac{d(\alpha x^{\beta})}{dx}\right|_{x=\gamma}\ = \alpha\beta
(\gamma)^{\beta - 1}
$$

So we can compute all of this in one go:

{% highlight python %}
data = []
for k in range(10000):
    alpha = random.randint(0, 10)
    beta = random.randint(0, 10)
    gamma = random.random()
    data.append(alpha * beta * (gamma ^ (beta - 1)))
print mean(data)
{% endhighlight %}

**Note that for all files, when using cloud.sagemath the files are not on your
physical computer but in the cloud. Apparently some students were confused by
that.**

## Individual coursework

The individual coursework is now available (**due in week 11**):
[{{site.baseurl}}/Assessment/IndividualCoursework/]({{site.baseurl}}/Assessment/IndividualCoursework/).

It requires you to use LaTeX (how mathematicians write mathematics). Take a look
at the 10th Lab sheet if you want to get started (in the meantime you can get
going with the required coding).


## What you should do next:

- **Start the next sheet**: make sure you spend time working on the sheet **BEFORE** the labs.
- **Start the coursework**
- Contribute to the wiki.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear **please** come and see me during office hours.
