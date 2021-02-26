# Lab 04 - Array-Backed Lists

## Overview

For this assignment you will complete the implementation of the array-backed list data structure (`ArrayList`) started during class, so that it supports (nearly) all the [common](https://docs.python.org/3.5/library/stdtypes.html#common-sequence-operations) and [mutable](https://docs.python.org/3.5/library/stdtypes.html#mutable-sequence-types) sequence operations.

## Implementation Details

For the `ArrayList`'s underlying data storage mechanism you will use the built-in Python list, constrained so that only the following operations (as would be supported by a primitive array) are available:

- create a "list" with `n` elements
- `lst[i]` for getting and setting a value at an *existing, positive* index `i`
- `len(lst)` to obtain the number of slots

### `ConstrainedList`

To help keep us honest, we've defined an API-constrained sub-class of the built-in list -- `ConstrainedList` -- an instance of which is assigned to the `data` attribute of each `ArrayList`. You should not change the definition of `ConstrainedList`, and ensure that your `ArrayList` implementation never assigns a regular Python list to its `data` attribute. So long as you use `ConstrainedList` in your implementation, you can be certain you're not performing any "illegal" operations (i.e., outside the constraints established above). If you invoke a disallowed operation, an appropriate exception will be raised.

### `ArrayList`

And now for the task at hand. We've partitioned the `ArrayList` methods you need to implement (and the test cases that follow) into seven categories:

1. Subscript-based access (completed in class)
2. Stringification
3. Single-element manipulation
4. Predicates (True/False queries)
5. Queries
6. Bulk operations
7. Iteration

All told, there are 23 methods --- a handful of which have already been implemented for you --- whose behavior are specified in their docstrings below. Note that we left out API support for *slices* (e.g., `lst[start:stop:step]`); you can read about [how to support slices in the Python docs](https://docs.python.org/3.5/reference/datamodel.html#object.__length_hint__), but we just don't think it's worth the extra busywork.


### Hints / Advice

We strongly advise that you start with the first category of functions and move down the list sequentially, pausing after each to run the corresponding test cases. The only category that might be worth skipping to early on is *Iteration* --- which can help simplify several other methods. Keep in mind that while you're not permitted to make use of high level APIs in the underlying list, you can certainly make use of `ArrayList` methods you've already implemented.

For instance, your implementations of `pop` and `remove` can (and should) use the `del` operator on your own list to remove elements from the middle, and it probably makes sense to use `extend` in your `__add__` and `copy` methods.
