# Lab 01 - Basic Python

## Exercise 1: Perfect Numbers

Most of the lab notebooks you'll be working on for this class will come with a fair bit of skeleton code, i.e., stubbed out classes and functions that you need to complete or modify to get working correctly.

In the cell below, for instance, you'll find a stubbed out function named `is_perfect`, which should return `True` if the number passed to it is a "perfect" number, and `False` otherwise.

A perfect number is a postive integer whose value is equal to the sum of its proper divisors (i.e., its factors excluding the number itself). 6 is the first perfect number, as its divisors 1, 2, and 3 add up to 6.

Fill in your own implementation of the function below:

```python
def is_perfect(n):
    pass
```

Each exercise will also be accompanied by one or more *unit tests*, each of which is meant to test some aspect of your implementation. When you run the unit test cell(s) after evaluating your implementation, you'll either find errors reported, which should help you identify what you need to fix, or they will complete silently, which means you've passed the test(s).

**It's important that you ensure your implementation and test cell(s) actually run to completion before moving on** --- there's a big difference between a cell not producing an error and not completing! (A "`In [*]`" marker next to the cell means that it's still being evaluated by the interpreter.)

We will often run additional *hidden tests* upon submission of your notebook to guard against hardcoded solutions.  While you won't see the specific test cases, you can resubmit your work as many times as you wish (before the deadline) to ensure they pass.

## Exercise 2: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Complete the following function, which finds the sum of all the multiples of 3 or 5 below the argument `n`.

```python
def multiples_of_3_and_5(n):
    pass
```

## Exercise 3: Integer Right Triangles

Given a perimeter of 60, we can find two right triangles with integral length sides: `[(10, 24, 26), (15, 20, 25)]`. Complete the following function, which takes an integer `p` and returns the number of unique integer right triangles with perimeter `p`.

Note that your solution should take care to limit the number of triangles it tests --- **your function must complete in under 3 seconds for all values of `p` used in the tests to earn credit.**

## Exercise 4: Simple ASCII Art

For this next exercise, you'll need to complete the function `gen_pattern`, which, when called with a string of length $\ge$ 1, will print an ASCII art pattern of concentric diamonds using those characters. The following are examples of patterns printed by the function (note the newline at the end of the last line!):

    > gen_pattern('X')

    X

    > gen_pattern('XY')

    ..Y..
    Y.X.Y
    ..Y..

    > gen_pattern('WXYZ')

    ......Z......
    ....Z.Y.Z....
    ..Z.Y.X.Y.Z..
    Z.Y.X.W.X.Y.Z
    ..Z.Y.X.Y.Z..
    ....Z.Y.Z....
    ......Z......

You ought to find the string [`join`](https://docs.python.org/3.6/library/stdtypes.html#str.join) and [`center`](https://docs.python.org/3.6/library/stdtypes.html#str.center) methods helpful in your implementation. They are demonstrated here:

    > '*'.join('abcde')

    'a*b*c*d*e'

    > 'hello'.center(11, '*')

    '***hello***'

Complete the `gen_pattern` function shown below:

```python
def gen_pattern(chars):
    pass
```

## Testing your implementation

You can execute the tests for all 4 exercises by running:

```python
python lab01.py
```

If you are working from an python interpreter, IDE, or editor that supports it you can also run individual test cases. For example:

```
test1()
```
