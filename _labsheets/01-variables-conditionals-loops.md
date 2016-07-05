---
layout: post
title:  "Lab sheet 01"
---

General description.

# Installing and running Python

Python is a programming language. There are various other programming languages:

- Java
- C
- C++
- Ruby
- VBA
- and many more.

A programming language allows you to write a program which is a sequence of
instructions that specifies how to perform a computation.

When writing a program you need two things:

- Something to save the code (a text editor for example)
- Something to run the code

We will be using a combination of these 2 things called **notebooks**.

# Install Python

There are various distributions of Python, we will use
[Anaconda](https://www.continuum.io/why-anaconda) which comes packaged with a
variety of other useful tools (including the notebooks I mentioned above).

To install it on your personal machine follow these steps:

1. Go to this webpage:
   [www.continuum.io/downloads](https://www.continuum.io/downloads).
2. Identify and download the version of Python 3 for your operating system
   (Windows, Mac OSX, Linux).
3. Run the installer.

We will use a Jupyter notebook which runs in your browser. To open a local
server find the Continuum navigator and click on Jupyter.

These lab sheets will include code snippets. They show what code you should
write but also the output you should see. Try the following:

```python
>>> print("Hello world")  # Code written
Hello world

```

# Basics

These questions aim to show you the basic building blocks of programming

- **TICKABLE** Creating numeric variables.

  One of the building block of any
  programming language is variables. This is how we store a particular variable
  that we can reuse:

  ```python
  >>> age = 20  # Pointing the variable age at the numeric value 20
  >>> print(age)  # Recalling the value of the variable
  20

  ```

  It is possible to carry out a variety of numeric operations and reassigning the value of the variable:

  ```python
  >>> age = age + 1  # Adding 1 to age
  >>> print(age)
  21

  ```

  Python has some **short hand** for the above:

  ```python
  >>> age += 1  # Adding 1 to age
  >>> print(age)
  22

  ```

  We can do more than just addition (experiment with these as you might need
  them later on):

  - Subtraction: `-`
  - Multiplication: `*`
  - Division: `/`
  - Exponentiation: `**`
  - Modulo division: `%`

- **TICKABLE** Creating character variables.

  Another type of variable used is called a character variable. **In
  programming these are called strings**.

  ```python
  >>> firstname = "Vince"
  >>> print(firstname)
  Vince

  ```

  There are various things that we can do with character variables:

  ```python
  >>> len(firstname)  # How many characters are in the variable
  5

  ```

  ```python
  >>> firstname[0]  # We can point at individual characters, 0 is the first
  'V'
  >>> firstname[4]
  'e'
  >>> firstname[-1]  # We can use negative number to start counting from the end
  'e'
  >>> firstname[0:4]  # We can 'slice' scrings
  'Vinc'

  ```

  We can also create new strings from other ones:

  ```python
  >>> lastname = "Knight"
  >>> fullname = firstname + " " + lastname
  >>> fullname
  'Vince Knight'

  ```

- **T** If statements: boolean variables
- **T** For and while loops: for and while loops

# Further work

These questions aim to push a bit further.

- Use code to check the following identity:

  $$\sum_{i=0}^{n}\frac{n(n+1)}{2}$$

  for \(n=200\).

- **T** Modify **the above** to check it for all values less than 1000.

3 other questions that push students a bit.
