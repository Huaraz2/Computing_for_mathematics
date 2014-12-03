---
layout     : post
categories : [handouts, 2014-2015]
title      : 'Handout 10 - Minor issues and next semester...'
comments   : true
---
Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

LaTeX.

## Small things

There are various minor details that some people had trouble with:

- Names of files and images...
- Organisation of the preamble...

For the above two issues take a look at my handout for [last year]({{site.baseurl}}/Handouts/2013-2014/handout10).

Some students had difficulties with creating bibliographies when using CloudSageMath:

Be sure when you create the `.bib` file to NOT CLICK ON `LaTeX` file but on `New File`.
This can be clearly seen in the relevant video.

## Cloud.sagemath sometimes being slow

This is due to various architectural issues.
William Stein describes it as '"like a computer booting up" and is expected'.
In other words: don't worry it _will_ speed up.

## Showing Code in LaTeX

This is easy to see how to do if you take a look at my model answer (I really recommend you look at that).

Here is how one includes code in LaTeX:

{% highlight latex %}
\begin{verbatim}
def illustrate(f, a):
    """
    Function to take a function and illustrate the limiting definition of a derivative at a given point.
    """
    lst = []
    for h in srange(.01, 3, .01):
        lst.append([h,(f(a+h)-f(a))/h])
    return list_plot(lst, axes_labels=['$x$','$\\frac{f(%.02f+h)-f(%.02f)}{h}$' % (a,a)])
\end{verbatim}
{% endhighlight %}

## Plagiarism

Be careful to not plagiarise. Here are the University's guidelines on plagiarism and unfair practice: [http://cardiff.ac.uk/regis/ifs/plag/](http://cardiff.ac.uk/regis/ifs/plag/).

As long as you reference any work that you use as a source you'll be fine (for example a website from which you have taken some code).

Note that the submission details have been detailed in the [coursework instructions]({{site.baseurl}}/Assessment/IndividualCoursework/).

## What you should do next:

- Think of groups and topics for next semester
- **Finish the coursework**
- If anything is still unclear **please** come and see me during office hours.
