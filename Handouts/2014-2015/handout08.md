---
layout     : post
categories : [handouts, 2014-2015]
title      : 'Handout 8 - Repeating actions with loops, the individual coursework and Class test feedback.'
comments   : false
---
Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- You learnt about the mathematical topic of linear algebra;
- You saw how to make relevant calculation in Sage:

    - Determinant
    - Inverse

## Creating patterns

Modern mathematical theory is often developed thanks to the use of a computer package like Sage.
For example let us say that we think the following is perhaps true:

> A number is divisible by 11 if and only if the alternating sum of it's digits is divisble by 11.

For example:

- For 11: \\(1-1= 0\\)
- For \\(473=11\times 43\\): \\(4 - 7 + 3 = 0\\)
- For \\(209=11\times 19\\): \\(2 - 0 + 11 = 11\\)

Of course we could prove this algebraically very simply but let us imagine that we wanted to gather a large amount of data of our conjecture:

{% highlight python %}
class Experiment():
    """
    A class for an experiment
    """
    def __init__(self, N):
        """
        Initialisation method:
            inputs: N - the number for which we will check the conjecture
        """
        self.N = N
        self.divisible_by_11 = N % 11 == 0
        self.sum_of_consecutive_digits = sum([(-1) ** d *int(str(N)[d]) for d in range(len(str(N)))])
    def test_conjecture(self):
        """
        Returns True if 'A number is divisible by 11 iff the sum of alternating digits is divisble by 11'
        """
        if self.divisible_by_11:
            return self.sum_of_consecutive_digits % 11 == 0
        return self.sum_of_consecutive_digits % 11 != 0
{% endhighlight %}

Let's test if the above works:

{% highlight python %}
exp = Experiment(11)
exp.test_conjectures()
exp = Experiment(12)
exp.test_conjectures()
exp = Experiment(473)
exp.test_conjectures()
exp = Experiment(472)
exp.test_conjectures()
{% endhighlight %}

In practice we'd want to test this for a **very large** set of numbers:

{% highlight python %}
print all(Experiment(n).test_conjecture() for n in range(10000))
{% endhighlight %}

## Repeating actions over a list

Q8 caused a few difficulties for some students.
This question was very similar to questions we have done multiple times: taking something from one list, doing something to it and then putting it in another list.
The only difference in this instance was that the 'doing something' was perhaps a bit complicated but nothing more complicated than we had done before.
Take a careful read through the solutions and if it still doesn't make sense please do come and see me or Jason.

## Individual coursework

The individual coursework is now available (**due in week 11**): [{{site.baseurl}}/Assessment/IndividualCoursework/]({{site.baseurl}}/Assessment/IndividualCoursework/).

It requires you to use LaTeX (how mathematicians write mathematics). Take a look at the 10th Lab sheet if you want to get started (in the meantime you can get going with the required coding).

## Class test

Here are some summary statistics about the class test marks:

- Total mark:

    - mean: 74.66
    - median: 75.00
    - max: 100.00

- q1 mark:

    - mean: 87.56
    - median: 100.00
    - Best: 100.00

- q2 mark:

    - mean: 74.29
    - median: 90.00
    - Best: 100.00

- q3 mark:

    - mean: 46.81
    - median: 50.00
    - Best: 100.00

- Documentation mark:

    - mean: 90.00
    - median: 100.00
    - Best: 100.00

Percentage of marks above given mark:

- 0.97 of scripts \\(\geq\\) 40%
- 0.93 of scripts \\(\geq\\) 50%
- 0.82 of scripts \\(\geq\\) 60%
- 0.66 of scripts \\(\geq\\) 70%
- 0.42 of scripts \\(\geq\\) 80%
- 0.24 of scripts \\(\geq\\) 90%

A picture of the distribution of the marks:

![]({{site.baseurl}}/Handouts/2014-2015/Images/classtestmarkdistribution-2014-2015.svg)

## What you should do next:

- **Start the next sheet**: make sure you spend time working on the sheet **BEFORE** the labs.
- **Start the coursework**
- Contribute to the wiki.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear **please** come and see me during office hours.
