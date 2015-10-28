---
layout     : post
categories : 2015-2016
title      : "2015-2016: Handout 5 - The init method and some uses of Python"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- How to create a class and an instance of a class;
- How to give a class attributes;
- How to give a class methods;
- How to create new classes from old through inheritance.

## The `__init__` method

A few of you had some difficulties with the `__init__` method and a few of you
with classes in general.

Let us imagine we are creating a database for students at the university. We
want our students to have the following attributes:

- Number
- Year of birth
- Current year of study

We also want a student to be able to `pass_a_year`.

Here is how we would build our class:

{% highlight python %}
class Student:
    """
    A class for our students
    """

    def __init__(self, number, year_of_birth, current_year_of_study):
        """
        This method is used when we create a given instance. It is called a
        'constructor'
        """
        self.number = number
        self.year_of_birth = year_of_birth
        self.current_year_of_study = current_year_of_study

    def pass_a_year(self):
        """
        This increments the year of study
        """
        self.year_of_birth += 1
{% endhighlight %}

The above just corresponds to us preparing the database. We do not yet have any
students in the data base. Now let's put two students in to our new first year:

{% highlight python %}
vince = Student(12, 1984, 1)
zoe = Student(14, 1983, 1)
{% endhighlight %}

When we create an instance (as above), the `init` method launches. As you can
see above, the `init` method we wrote takes 4 arguments: `self`, `number`,
`year_of_birth` and `current_year_of_study` **but** it looks like we're only
passing it 3 arguments `Student(12, 1984, 1)`. **This is because the first
argument is the instance itself**. Imagine a student enrolling: the student
enrolling is the `self`.

Let's marry `vince` and `zoe` (Zoe is my wife's name). To do that we're going to
add the `become_partner` to our class (this would be copied just below `def
pass_a_year`):

{% highlight python %}
        def become_partner(self, student):
            """
            Assign the instance itself to be the passed student's partner and
            vice versa
            """
            self.partner = student
            student.partner = self
{% endhighlight %}

Now let us make things official:

{% highlight python %}
vince.become_partner(zoe)
print vince.partner.number
print zoe.partner.number
{% endhighlight %}

Here are some further resources that might be helpful:

- [Handout from 2014-2015.](http://vknight.org/Computing_for_mathematics/Handouts/2014-2015/handout05/)
- [Handout from
  2013-2014.](http://vknight.org/Computing_for_mathematics/Handouts/2013-2014/handout05/)
- [A video on classes suggested by 1 of the student
  tutors,](https://www.youtube.com/watch?v=trOZBgZ8F_c)
- [This simple stack overflow question suggested by 1 one of the student
  tutors.](http://stackoverflow.com/questions/11673906/new-to-python-anyone-know-what-init-self-does-simple-expl-please)

## Uses of Python

A few of you have asked me how far you can go with Python: what is Python used
for. Here are some examples:

- Pinterest is built using Python.
- Instagram is built using Python.
- YouTube is built using Python.
- Dropbox is built using Python.

Some recent work using Python might be of interest:

- Using Python to help with landslide relief:
    - [Cardiff news
      site](http://www.cardiff.ac.uk/news/view/97475-supporting-nepals-post-disaster-efforts)
    - [One of the developers on the project's site](http://girishkumar.co/)
    - [His talk next month at PyDiff](http://www.pydiff.wales/events/2015-11-10.html)

- [Talk Python to me](http://talkpython.fm/) is a podcast about Python:
    - [Here is an episode about Python being used at CERN (the large hadron
      collider)](http://talkpython.fm/episodes/show/29/python-at-the-large-hadron-collider-and-cern)
    - [Here is an episode about Python being used for machine
      learning](http://talkpython.fm/episodes/show/31/machine-learning-with-python-and-scikit-learn)

- [A library that you might find interesting is the turtle
  library](https://opentechschool.github.io/python-beginners/en/simple_drawing.html).
  Take a look at (this shows a good example of using classes and methods):

  {% highlight python %}
import turtle

t = turtle.Turtle()
k = 0
while k < 200:
    t.forward(10 + k)
    t.left(90)
    k += 1
  {% endhighlight %}

Try this too: [Sierpinski
triangle](http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsSierpinskiTriangle.html).


## What you should do next:

- Start the next sheet: this is a short one and the aim is for you to be familiar with Sage.
- Continue to revise for the class test: work through all your lab sheets. If you can do exercises in the lab sheets (not just ‘understand them’ but actually ‘do them’) you will be fine.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear please come and see me during office hours.
