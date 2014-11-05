---
layout     : post
categories : [pasthandouts, 2013-2014]
title      : '2014-2015: handout 6 - Sage and the Class test'
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
- Sage can be used to check formulae. For example: what is the formula for \\(\sum_{i=a}^bx^{i}\\)?

        a = var('a')
        b = var('b')
        i = var('i')
        x = var('x')
        sum(x^i,i,a,b)

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
- Sage allows you to share files with particular people (if you know their username) and also allows you to publish it.

## Solving equations
## Typeset mode
## Markdown
## Installing Sage locally
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
