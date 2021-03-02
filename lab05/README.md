# Lab 05 - Doubly Linked List

## Overview

For this assignment you will complete the implementation of the linked list data structure (`LinkedList`) started during class, so that it supports (nearly) all the [common](https://docs.python.org/3.5/library/stdtypes.html#common-sequence-operations) and [mutable](https://docs.python.org/3.5/library/stdtypes.html#mutable-sequence-types) sequence operations.

Your implementation should make use of doubly-linked nodes (i.e., each containing a `prior` and `next` reference), an ever-present sentinel `head` node, and a "circular" topology (where the head and last nodes are, logically, neighbors). This setup should substantially simplify your implementation by reducing the edge cases and amount of iteration you have to perform.

Your implementation should *not* make use of the built-in Python list data structure (finally!).

## Implementation Details

### `LinkedList`

As with the previous assignment, we've partitioned the `LinkedList` methods you need to implement (and the test cases that follow) into categories:

1. Subscript-based access
2. Cursor-based access
3. Stringification
4. Single-element manipulation
5. Predicates (True/False queries)
6. Queries
7. Bulk operations
8. Iteration
9. Reverse

Besides (2), you should be familiar with the APIs from all the other categories, as you implemented them for the previous lab. The cursor-based methods are described in the next section.

## Cursor-based access

As discussed in lecture, it makes sense for a linked-list data structure to enable access to elements via a cursor-based API. This avoids the need to repeatedly locate a node at a given index for reading / inserting / deleting elements at that location. In this way we can better take advantage of the O(1) insert/delete operations.

The cursor-based APIs you need to implement are as follows:

- `cursor_get`: retrieves the value at the current cursor position
- `cursor_set`: sets the cursor to the node at the provided index
- `cursor_move`: moves the cursor forward or backward by the provided offset (a positive or negative integer);  note that it is possible to advance the cursor by further than the length of the list, in which case the cursor will just "wrap around" the list, skipping over the sentinel node, as needed
- `cursor_insert`: inserts a new value after the cursor and sets the cursor to the new node
- `cursor_delete`: deletes the node the cursor refers to and sets the cursor to the following node

### Hints / Advice

While you will have to implement some of the methods from scratch — i.e., in terms of the new underlying linked storage mechanism — you should be able to reuse quite a few of your method implementations from the previous assignment (the array-backed list), providing you defined them in terms of other, lower-level methods. This may not always be the most efficient (e.g., loops that repeatedly make use of `__getitem__` to access succeeding elements are clear offenders), but while we recommend that you try to optimize for improved run-time efficiency it is not a grading criterion for this assignment.
