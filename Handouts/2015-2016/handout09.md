---
layout     : post
categories : 2015-2016
title      : '2015-2016: Handout 9 - Spoons, spoons, spoons'
comments   : true
---
Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

Some basic Sage code to solve differential equations:

- ODEs;
- Systems of ODEs;
- Numerical solutions of ODEs (for when they can't be solved exactly).

## Initial conditions

The only comment I've had about this lab sheet was students not fully
understanding the concept of an initial solution.

Let's take a look at the solution to question 6.

{% highlight python %}
t = var('t')
y = function('y', t)
x = function('x', t)
sols = desolve_system([diff(x, t) == - y, diff(y, t) == - 5 * x], [y,x], ics=[0,100,700])
{% endhighlight %}

Looking at the differential equations we see that the first army (\\(x\\)) is
"better" than the second army (\\(y\\)), the rate of decrease of the second army
is "faster".

If play with the initial conditions `ics=[...]` and plot the results we see different
outcomes (in particular the second army needs a lot of troupes to not lose).

## Numerical analysis

Certain equations and differential equations can't be solved or are very difficult to solve. In this case numerical solutions can still be found. This is what `desolve_rk4` is for.

This is all part of a subject called [Numerical Analysis](http://en.wikipedia.org/wiki/Numerical_analysis).

Some applications of this include the solution of equations that describe how many people would be in a queue throughout a day across different hours of the day.

## LaTeX

LaTeX is a language for typesetting (writing) documents.

- Go through the videos on the corresponding [lab sheet]({{site.baseurl}}/LabSheets/Week_10/).
- Take a look at my [coursework template](http://goo.gl/huzjyq).
- There are various other templates available at [https://www.writelatex.com/templates](https://www.writelatex.com/templates).
- If you are having a hard time understanding how 'floats' behave (figures not being in the correct place) in LaTeX take a look at [http://drvinceknight.blogspot.co.uk/2013/12/explaining-floats-in-latex.html](http://drvinceknight.blogspot.co.uk/2013/12/explaining-floats-in-latex.html).

If you would like to install LaTeX on your own machine (instead of using the cloud based solutions discussed in the lab sheet):

- Mac OS: [https://www.youtube.com/watch?v=5CNmIaRxS20](https://www.youtube.com/watch?v=5CNmIaRxS20)
- PC: [http://miktex.org/about](http://miktex.org/about)

Come and chat to me if you're having trouble with either.

## Submitting your coursework and plagiarism

You will be submitting your coursework via learning central: please [read the
instructions](http://0.0.0.0:4000/Computing_for_mathematics/Assessment/IndividualCoursework/)
as well as [this video](https://vimeo.com/114969438). **Do not leave this till the last
minute**. If you don't submit, your mark will be 0.

## Some ideas

I sent you an email with various projects that might give you some ideas. Here
are some more:

- Take a look at [http://preshing.com/20110926/high-resolution-mandelbrot-in-obfuscated-python/](http://preshing.com/20110926/high-resolution-mandelbrot-in-obfuscated-python/) which shows some Python code that generates a fractal **but also** looks like a fractal. The code itself is pretty complicated.
- There's a whole area of mathematics that looks at studying queues (Queuing Theory). Here's is the shortest bit of Python script that Jason, Geraint and I managed to write that simulates a simple queue: [https://github.com/drvinceknight/ShortMM1Q/blob/master/MM1Q.py](https://github.com/drvinceknight/ShortMM1Q/blob/master/MM1Q.py). **Note that that is not well written code: it's just short**.
- Here's something that I wrote a while back looking at random matrices and creating gifs: [http://drvinceknight.blogspot.co.uk/2013/09/for-no-reason-whatsoever-animated-gifs.html](http://drvinceknight.blogspot.co.uk/2013/09/for-no-reason-whatsoever-animated-gifs.html).
- Here's something I wrote when some of the postgrads started messing around with pigeon holes: [http://drvinceknight.blogspot.co.uk/2013/10/pigeon-holes-markov-chains-and-sagemath.html](http://drvinceknight.blogspot.co.uk/2013/10/pigeon-holes-markov-chains-and-sagemath.html).
- If you play [Clash of Clans](http://www.supercell.net/games/view/clash-of-clans) this might be of interest: [http://drvinceknight.blogspot.co.uk/2014/05/wizards-giants-linear-programming-and.html](http://drvinceknight.blogspot.co.uk/2014/05/wizards-giants-linear-programming-and.html),
- Here is how I will be scheduling your final group presentations next term: [http://drvinceknight.blogspot.co.uk/2014/03/scheduling-group-presentations-using.html](http://drvinceknight.blogspot.co.uk/2014/03/scheduling-group-presentations-using.html).

## Code Club

We are approaching the part of the course where you will all be working on various specific and different projects.
This fits in to the remit of [Code Club](http://cardiffmathematicscodeclub.github.io/sessions.html), so it might be a place to get some assistance.

## What you should do next:

- Work through LaTeX lab sheets.
- **Finish the coursework**
- Contribute to the wiki.
- If anything is still unclear **please** come and see me during office hours.
