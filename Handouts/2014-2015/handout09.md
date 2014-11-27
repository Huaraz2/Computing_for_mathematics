---
layout     : post
categories : [handouts, 2014-2015]
title      : 'Handout 9 - Some ideas...'
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

## Extracting parts of an equation

Some difficulty on this lab sheet was associated to extracting expressions from solutions of equations.

This basically revolves around the fact that the output of `desolve_system` is a list of equations and not a list of functions.
Plotting equations does not make mathematical sense but plotting a function does (a plot is a graphical representation of a mapping of one set to another).

Take a look at the conversation I had with Henry at the bottom of the Week 9 lab sheet which should explain/direct you to the right spot.

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

## Some ideas

- Take a look at [http://preshing.com/20110926/high-resolution-mandelbrot-in-obfuscated-python/](http://preshing.com/20110926/high-resolution-mandelbrot-in-obfuscated-python/) which shows some Python code that generates a fractal **but also** looks like a fractal. The code itself is pretty complicated.
- There's a whole area of mathematics that looks at studying queues (Queuing Theory). Here's is the shortest bit of Python script that Jason, Gerain and I managed to write that simulates a simple queue: [https://github.com/drvinceknight/ShortMM1Q/blob/master/MM1Q.py](https://github.com/drvinceknight/ShortMM1Q/blob/master/MM1Q.py). **Note that that is not well written code: it's just short**.
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
