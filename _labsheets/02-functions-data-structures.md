---
layout: post
title:  "Lab Sheet 02: Functions and Data Structures"
---

General description.

# Basics

These questions aim to show you the basic building blocks of programming

- **T** Building a very simple function

  ```python
  >>> def say_hi():
  ...     return "Hello world"

  ```

  ```python
  >>> say_hi()
  'Hello world'

  ```

- **T** Building a slightly more complicated function

  ```python
  >>> def sum_till_n(n):
  ...     """This is called a doctstring. We use it to describe what a function
  ...     does. This function adds the first n numbers together."""
  ...     total = 0
  ...     count = 1
  ...     while count <= n:
  ...         total += count
  ...         count += 1
  ...     return total
  >>> sum_till_n(3)
  6

  ```

- **T** Lists

  ```python
  >>> favourite_numbers = [0, 1, 2, 3, 4]
  >>> favourite_numbers
  [0, 1, 2, 3, 4]

  >>> type(favourite_numbers)
  <type 'list'>
  >>> sum(favourite_numbers)
  10

  >>> max(favourite_numbers)
  4

  >>> min(favourite_numbers)
  0

  >>> total = 0
  >>> for n in favourite_numbers:
  ...     if n % 2 == 0:  # Check if n is divisible by 2
  ...         total += n
  >>> total
  6

  ```

- **T** List comprehension

  ```python
  >>> square_of_favourite_numbers = [x ** 2 for x in favourite_numbers]
  >>> square_of_favourite_numbers
  [0, 1, 4, 9, 16]

  ```

  This is familiar:

  $$\{n \in S \;| \text{ if } n \text{ is divisible by  2}\}$$

  ```python
  >>> sum([n for n in favourite_numbers if n % 2 == 0])
  6

  ```

# Further work

These questions aim to push a bit further.

- Triangular numbers

- **T** Fibonacci function

- Create a list of numbers whose fibonacci function is divisible by 2. Is the
  result surprising?

- Divisibility by 11

- Dictionaries
