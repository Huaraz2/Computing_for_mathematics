---
layout     : post
categories : 2015-2016
title      : '2015-2016: Handout 10 - Referencing a web page...'
comments   : true
---
Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Friday 1500-1700**

## What you have learnt this week:

LaTeX.

## Referencing a web page

If you googled something like 'how to reference a website bibtex' you would have
gotten this:
[tex.stackexchange.com/questions/3587/how-can-i-use-bibtex-to-cite-a-web-page](http://tex.stackexchange.com/questions/3587/how-can-i-use-bibtex-to-cite-a-web-page).

Here is another example of this.

The `bib` file (for example `bibliography.bib`):

{% highlight latex %}
@misc{Google,
  title = {Google},
  howpublished = {\url{https://www.google.com}},
  note = {Accessed: 2015-12-03}
}
{% endhighlight %}

The corresponding `tex` file:

{% highlight latex %}
\documentclass{article}

\usepackage{hyperref}  % This is just so that I can use a hyperlink.

\begin{document}

This website gives you links to helpful information \cite{Google}.

\bibliographystyle{plain}
\bibliography{bibliography.bib}
\end{document}
{% endhighlight %}

Here is a gif showing this work: [g.recordit.co/4wXo4fRNH6.gif](http://g.recordit.co/4wXo4fRNH6.gif).
Here is the video version: [recordit.co/4wXo4fRNH6](http://recordit.co/4wXo4fRNH6).

## Plagiarism

Be careful to not plagiarise. Here are the University's guidelines on plagiarism and unfair practice: [http://cardiff.ac.uk/regis/ifs/plag/](http://cardiff.ac.uk/regis/ifs/plag/).

As long as you reference any work that you use as a source you'll be fine (for example a website from which you have taken some code).

Note that the submission details have been detailed in the [coursework instructions]({{site.baseurl}}/Assessment/IndividualCoursework/).


## Next Semester

Next Semester is a group exercise. You can find information about it here: [{{site.url}}{{site.baseurl}}/Enterprise/]({{site.baseurl}}/Enterprise/).

## What you should do next:

- Think of groups and topics for next semester
- **Finish the coursework**
- If anything is still unclear **please** come and see me during office hours.
