---
layout: post
title:  "Lab Sheet 07: Symbolic Calculus"
---

# Basics

1. **Tickable** Calculating limits.

   It is possible to calculate limits easily with SymPy. Let us consider the
   following function as a running example:

   $$f(x)=1/x$$

   First let us define this function in Python as a function of the symbolic
   variable `x`:

   ```python
   >>> from sympy import *
   >>> x  = symbols('x')
   >>> def f(x):
   ...     return 1 / x
   >>> f(x)
   1/x

   ```

   We can compute the limits at \\(\pm\infty\\):

   ```python
   >>> limit(f(x), x, oo)
   0
   >>> limit(f(x), x, -oo)
   0
   >>> limit(f(x), x, +oo)
   0

   ```

   We can also compute the limit at \\(0\\) however we must be careful here (you
   will recall from basic calculus that the limit depends on the direction):

   ```python
   >>> limit(f(x), x, 0)  # The default direction of approach is positive.
   oo
   >>> limit(f(x), x, 0, dir="+")
   oo
   >>> limit(f(x), x, 0, dir="-")
   -oo

   ```

2. **Tickable** Differentiation.

   We can use SymPy to carry out differentiation:

   ```python
   >>> diff(f(x), x)
   -1/x**2
   >>> diff(cos(x), x)
   -sin(x)

   ```

   We can carry out various orders of differentiation. These all give the second
   order derivative of \\(\cos(x)\\):

   ```python
   >>> diff(diff(cos(x), x), x)
   -cos(x)
   >>> diff(cos(x), x, x)
   -cos(x)
   >>> diff(cos(x), x, 2)
   -cos(x)

   ```

   SymPy can handle differentiation of functions with multiple variables (you
   will learn more about this in further Calculus):

   ```python
   >>> y = symbols('y')
   >>> diff(cos(x) * sin(y), x)  # Differentiating with respect to x
   -sin(x)*sin(y)
   >>> diff(cos(x) * sin(y), y)  # Differentiating with respect to y
   cos(x)*cos(y)

   ```

   Finally it is also possible for SymPy to differentiate hypothetical functions
   (ones that we do not know anything about):

   ```python
   >>> g = Function('g')  # We create g as a generic function
   >>> diff(g(x), x, 2)
   Derivative(g(x), x, x)

   ```

   Try and experiment with differentiating more complicated functions.

3. **Tickable** Integration.

   As well as differentiation it's possible to carry out integration.

   We can do both definite and indefinite integrals:

   ```python
   >>> integrate(f(x), x)  # An indefinite integral
   log(x)
   >>> integrate(f(x), (x, exp(1), exp(5)))  # A definite integral
   4

   ```

   We can use this to verify the [fundamental theorem of
   calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus) for
   the specific example of our function \\(f\\):

   ```python
   >>> integrate(diff(f(x), x), x)
   1/x

   ```

   We can also verify this for generic functions:

   ```python
   >>> g = Function('g')
   >>> integrate(diff(g(x), x), x) == g(x)
   True
   >>> diff(integrate(g(x), x), x) == g(x)
   True

   ```

4. **Tickable** Plotting. It is possible to use SymPy to create plots.

   To view these in jupyter we need to run this line:

   ```python
   %matplotlib inline
   ```

   We can then create plots using the `plot` command:

   ```python
   >>> plot(f(x), (x, -1, 1))
   <...

   ```

   That's not very clear, let us modify the limits on the y axis.

   ```python
   >>> plot(f(x), (x, -1, 1), ylim=(-10, 10))
   <...

   ```

   We can also choose to modify the labels on the axes:

   ```python
   >>> plot(f(x), (x, -1, 1), ylim=(-10, 10), xlabel=None, ylabel="$1/x$")
   <...

   ```

   Finally we can also combine various plots of different functions together. To
   do this we build each plot separately (telling Python not to `show` them) and
   then combine them:

   ```python
   >>> p1 = plot(f(x), (x, -1, 1), show=False)
   >>> p2 = plot(x, (x, -1, 1), show=False, line_color="red")
   >>> p1.extend(p2)
   >>> p1.ylim = (-10, 10)
   >>> p1.xlabel = None  # Try using strings here
   >>> p1.ylabel = None
   >>> p1.show()

   ```

   It is also possible to save a file of the graph. Depending on how you name
   the file the type of tile will be different:

   ```python
   >>> p1.save("my_plot.pdf")  # Try `.png` etc...

   ```

5. **Worked example**

   We are going to use the above to attempt to find and classify all points of
   inflection for following quartic function:

   $$f(x) = - x^{4} + 9 x^{2} + 4 x - 12$$

   First let us take a look at the function:

   ```python
   >>> def f(x):
   ...     return  -x ** 4 + 9 * x ** 2 + 4 * x - 12
   >>> plot(f(x), (x, -20, 20) , ylim=(-20, 20))
   <...

   ```

   First let us find the roots of the functions:

   ```python
   >>> solveset(f(x), x)
   {-2, 1, 3}

   ```

   We have a quatric so one of those roots (of which there are only 3) must be
   repeated, let us see if we can factor our function:

   ```python
   >>> f(x).factor()
   -(x - 3)*(x - 1)*(x + 2)**2

   ```

   We see that \(2\) is a repeated root.

   Let's confirm the limiting behaviour of our function:

   ```python
   >>> limit(f(x), x, oo)
   -oo
   >>> limit(f(x), x, -oo)
   -oo

   ```

   Finally, we also see that there are 3 points of inflection so let us find
   them:

   ```python
   >>> poi = solveset(diff(f(x), x), x)
   >>> poi
   {-2, 1 + sqrt(6)/2, -sqrt(6)/2 + 1}

   ```

   Let us now evaluate which of these gives a positive or negative value of the
   second derivative:

   ```python
   >>> for point in list(poi):  # We convert the poi to a list
   ...     print(point, (diff(f(x), x, 2).subs({x: point})) > 0)
   -2 False
   1 + sqrt(6)/2 False
   -sqrt(6)/2 + 1 True

   ```

   We see that 2 points of inflection give negative second derivative (so they
   are local maxima, whereas \\(-\sqrt{6}/2+1\\) is a local minimum. This
   confirms the plot.

   **Further work**

   These questions aim to push a bit further.

6. Consider the function below:

   $$f(x) =- x^{4} + 10 x^{3} - 29 x^{2} + 8 x + 48$$

   Identify the roots and limits (at \\(\pm\infty\\) of the function and confirm
   this with a plot.

7. **Tickable** For the function of question 6, identify and classify all points
   of inflection.

8. There are various algebraic relationships on limits:

   $$\lim_{x\to a}[f(x)+g(x)]=\lim_{x\to a}f(x) + \lim_{x\to a}g(x)$$

   $$\lim_{x\to a}[f(x)\times g(x)]=\lim_{x\to a}f(x) \times \lim_{x\to a}g(x)$$

   $$\lim_{x\to a}[f(x)/g(x)]=\lim_{x\to a}f(x) / \lim_{x\to a}g(x) \text{ if } \lim_{x\to a}g(a)\ne 0$$

   Confirm these for generic functions \\(f\\) and \\(g\\) but also for the
   following particular examples:

    $$f(x) = x^2 + x$$

    $$g(x) = 1 / (x ^ 2 + 1)$$

9. The point of this question is to investigate the definition of a derivative:

   $$\frac{df}{dx}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$

   1. Consider \\(f(x) = x^3 + 3x - 20\\);
   2. Compute \\(\frac{f(x+h)-f(x)}{h}\\);
   3. Compute the above limit as \\(h\to 0\\) and verify that this is the
      derivative of \\(f\\).


10. A probability density function \\(f(x)\\) gives the probability of a random event \\(x\\). One such function, that corresponds to the exponential distribution is given by:

    $$f(x)=\begin{cases}
        \lambda e^{- \lambda x}&,\text{ for }x\geq 0\\
        0&,\text{ otherwise}
      \end{cases}$$

    1. Prove that the probability of all events occuring is 1 (you will need to integrate).
    2. Obtain the cumulative distribution function, defined by:

       $$F(x) = \int_{-\infty}^{x}f(t)\,dt$$

    Repeat this with the following probability distribution functions:

    1. Normal distribution: \\(f(x)=\frac{1}{\sqrt{2\sigma^2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}\\)
    2. The Logistic distribution: \\(f(x)=\frac{e^{\frac{x-\mu}{s}}}{s\left(1+e^{\frac{x-\mu}{s}}\right)^2}\\)