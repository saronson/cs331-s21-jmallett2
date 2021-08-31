# Lab 11 - Quick Sort

In this lab you will implement the quick-sort algorithm discussed in class and will implement several methods for selecting pivot elements.  Furthermore, instead of the partitioning scheme presented in class you will implement the original partitioning scheme developed by Hoare.
Note that your implementation should be **in-place**, that sorting should not allocate new python lists, but instead only change elements using `lst[pos] = value`.

## Quick Sort Recap

Remember that the **quicksort** algorithm does sort a list by selecting a **pivot** element and then split the input list into two parts: all elements that are smaller or equal to the pivot and all elements that are larger than the pivot. These two parts of the list are then sorted recursively using quick sort.

The selection of a good pivot is essential for achieving good performance. In worst case, i.e., if we always end up choosing the smallest or largest element of a list as the pivot then quick sort requires $O(n^2)$ time. Ideally, when we always choose the median of the current sublist, then quick sort will run in $O(n \log n)$.

## Pivot Selection Approaches

You will implement the following pivot selection approaches. Your implementation of quick sort `qsort` takes the pivot function as an argument `pivot_fn`.

### First element

Always use the first elements of the sublist `lst` as the pivot.

### Random Pivot

Select a random number $i$ between $0$ and $n-1$ and use the element at `list[i]` as the pivot.

### Median of three

Let `n` be the length of the sublist `lst`. The pivot is computed as the median (the middle value) of three values from the input:

```python
median(lst[low], lst[(low + high) // 2], lst[high])
```

## Hoare partition scheme

The partition scheme we have used in class is tightly bound to the choice of pivot. You will implement the more general scheme developed by Hoare (the inventor of quick sort). To partition an array, this scheme maintains two pointers `i` and `j` which are initialized as `i=low` and `j = high` (the bounds of the sublist to be partitioned). The partition scheme alternates between increasing `i` and decreasing `j` until `i >= j`:

- increase `i` until an element is found such that `lst[i] > pivot`
- decrease `j` until an element is found such that `lst[j] <= pivot`
- unless `i >= j`, swap `lst[i]` with `lst[j]` (the two elements in the wrong partition)
  - otherwise return `j`
