---
layout     : post
title      : "CfM : Class test 2015-2016"
categories : classtest
comments   : true
---
# Computing for Mathematics: Class test

## Instructions

-   You have 50 minutes to carry out the following 3 questions;
-   You are allowed access to the internet and any books/notes you may
    have with you. **However, YOU ARE NOT PERMITTED TO COMMUNICATE WITH
    ANY OTHER STUDENT**. As such you are simply not allowed to log in to
    an email client, facebook etc… If you are caught using any site that
    an invigilator suspects you may be able to use to communicate with
    another student you will be asked to stop working on this class test
    and you will be reported.
-   Write three separate scripts, one for each question, naming them as
    follows: `ma1003-studentnumber-q1.py` (replacing studentnumber by
    your actual student number and q1 with q2 or q3 for each of the
    questions). Submission details are given at the end of this sheet.
    **Start every script with a multiline comment with your student
    number and question number**. For example:

        """
        Class test - question 1
        c123456789
        """


**10 marks are available for convention, comments and general
presentation of code.**


## Q1

Create a function that uses the following sequences to approximate
\\(\sqrt{K}\\):

$$x_{n+1} = \frac{x_n+K/x_n}{2}$$

Write some code that compares the output of this algorithm to the actual
square root for the first 10000 digits.

(Available marks: 30)


## Q2

For this questions you might find the “math” library of use. For example
the following gives the square root of a number:

    >>> import math
    >>> math.sqrt(4)
    2.0

Consider the mathematical sequence \\(a_n\\) where the \\(n\\)th term of the
sequence is defined in the following two ways:

$$a_n = 2a_{n-1}+a_{n-2},\;a_0=a_1=1$$

and:

$$a_n=\frac{(1+\sqrt{2})^n+(1-\sqrt{2})^n}{2}$$

1.  Write an iterative function that returns \\(a_n\\);

2.  Write a recursive function that returns \\(a_n\\);

3.  Verify that the two formulations give the same result for the first
    10 values of \\(a_n\\).

(Available marks: 30)

## Q3

Here is a formula by Srinivasa Ramanujan (1887-1920) that gives an
expression for \\(\pi\\).

$$\pi = \frac{9801}{\sqrt{8}}\left(\sum_{k=0}^{\infty}\frac{(4k)!(1103+26390k)}{(k!)^4396^{4k}}\right)^{-1}$$

Note that the above is an **infinite** sum, but nonetheless calculating
the \\(n\\)th term still can give a good approximation of \\(\pi\\). Let us
define \\(f(n)\\):

$$f(n) = \frac{9801}{\sqrt{8}}\left(\sum_{k=0}^{n}\frac{(4k)!(1103+26390k)}{(k!)^4396^{4k}}\right)^{-1}$$

-   Define the above function \\(f\\) in python;

-   Using this, print to screen \\(f(n)\\) for integer values
    \\(1\leq n\leq 10\\).

(Available marks: 30)

## Solutions

- [Q1](./Solutions/solutionq1.py)
- [Q2](./Solutions/solutionq2.py)
- [Q3](./Solutions/solutionq3.py)
