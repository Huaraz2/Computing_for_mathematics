---
layout     : post
title      : "CfM : Class test 2014-2015"
categories : classtest
comments   : true
---
# Computing for Mathematics: Class test

## Instructions

- You have 50 minutes to carry out the following 3 questions;
- You are allowed access to the internet and any books/notes you may have with you. **However, YOU ARE NOT PERMITTED TO COMMUNICATE WITH ANY OTHER STUDENT**.
As such you are simply not allowed to log in to an email client, facebook etc...
If you are caught using any site that an invigilator suspects you may be able to use to communicate with another student you will be asked to stop working on this class test and you will be reported.
- Write three separate scripts for each question naming them as follows: `ma1003-studentnumber-q1.py` (replacing studentnumber by your actual student number and q1 with q2 or q3 for each of the questions). Submission details are given at the end of this sheet. Start every script with a multiline comment with your student number and question number. For example:


        """
        Class test - question 1
        c123456789
        """


**10 marks are available for convention, comments and general presentation of code.**


## Q1

The following dictionary contains course code - course name pairs:

        coursedictionary = {1: "Analysis I",
                            2: "Geometry",
                            3: "Algebra I",
                            4: "Computing for Mathematics"}

    The following list contains lists containing a student name as well as a list of the course codes on which they are enrolled:

        Student_List = [["Adam", [1, 2, 3]],
                        ["Zoe", [4, 2, 1]],
                        ["Ben", [3]],
                        ["Thomas", [4]]]

    **Using object orientated programming** obtain the number of students enrolled on each course as well as a dictionary containing student names as keys and lists of enrolled courses as values.

(Available marks: 30)

## Q2

Write a script that will write the first 500 numbers of the form \\(4k+1\\) for \\(k\in\mathbb{Z}\\) to a file named `output.txt`.

(Available marks: 30)

## Q3

A perfect number is a natural number that is equal to the sum of its divisors (excluding itself).
For example \\(1,2,4,7\\) and \\(14\\) divide \\(28\\) and \\(28=1+2+4+7+14\\).

Write:

- A function `isperfect` that returns `True` if the input is a perfect number and `False` otherwise.
- Using the above function, output the number of perfect numbers less than 10000.

(Available marks: 30)

## Solutions

- [Q1](./Solutions/solutionq1.py)
- [Q2](./Solutions/solutionq2.py)
- [Q3](./Solutions/solutionq3.py)
