# Lab 03 - Search and Sort

In this lab we will put the recently dicussed binary search and the sorting algorithms we just talked about into practice. Recall that binary search only works when the input is sorted. We want to put binary search into practice to search for query strings in a document of size `n` (`n` characters). This problem arises, e.g., in text editors. Most text editors allow the user to search for some string in a document. Of course this should be efficient even for relatively large documents. The approach we iteratively develop in this lab is efficient (`O(log n)` for search), but has a `O(n log n)` upfront cost that is paid once per document.

The challenge here is that the query strings may be of any size. Note that if all search strings are of the same size `k`, then we can just generate all substrings of the document of size `k`, put them into a list and sort them. To find a string, we can then just use binary search over this list. It is easy to see that with a sorted list of substrings of length `k` we can also support searches for strings of size `l < k` by just comparing the first `l` characters in binary search. However, how can we efficiently support search strings of any length without having to store all substrings of length up to `n`? We will introduce a simple, but elegant data structure that avoids having to store all these substrings.

## Exercise 1: Implement generic sort and binary search

Implement one of the sort algorithms discussed in class (or read up on other search algorithms and implement one of those) as a function `mysort`. The difference to the sort algorithms discussed in class is that:

1. Your sort algorithm takes as input a sequence of any type `T`
2. The caller provides a function `compare: T, T -> int` which compares two elements of type `T`. The function should return:
  - `-1` if the left is smaller than the right element
  - `1` if the left is larger than the right
  - `0` if the two elements are equal.

Furthermore, implement a generic binary sort as function `mybinsort`. Like our generic sort, this method takes a list of elements of type `T`. However, we allow the element we are searching for to be of a different type `S`. The callers has to pass a comparison function `compare: T, S -> int` that commpares an element of the list with the element we are searching for. The return values are defined as for sorting above. The function should assume that the input has been sorted using `mysort` using a compatible comparison function.

## Exercise 2: Search for strings up to length `n`

Implement the algorithm in a class `PrefixSearcher`. Instances of the class are initialized with a documents (a `str`) and a number `k` which is the maximum size of search strings that should be supported. During initialization of an instance of this class, you should create a list of all substrings of length `k`, then use `mysort` to sort this list. Note that we have to accomodate some strings that are shorter than `k`, namely the one at the end of the document, e.g., for `k = 3` and input `Hello world` you should create substrings:

```
'Hel', 'ell', 'llo', 'lo ', 'o w', ' wo', 'wor', 'orl', 'rld', 'ld', 'd'
```

## Exercise 3: SuffixArrays

In the last part of this lab we will implement a data structure called a SuffixArray that allow us to use binary search to search for any substring of any length in a document at only linear space overhead in the size `n` of the document. Instead of replicating all possible substrings, the suffix array uses indirection to avoid having to replicate substrings that already exist as consecutive subsequences of characters in the input document. For an document of size `n`, a suffix array for the document is a list of length `n` that contains all numbers of `[0,n-1]`. A number `i` represents any substring of the input document starting at offset `i`. For example, consider the string and positions shown below. The number 2 represents all substrings

```
0 1 2 3 4 5 6 7 8 9 10
H e l l o   W o r l d
```

In a suffix array the positions `[0,n-1]` are sorted in the list based on the lexicographical order of substrings that start at these positions. For instance, according to this sort order, the position `2` of our example string is less than the position `9`, because the substring starting at `2` (`llo World`) is lexicographically smaller than (`ld`). You should implement a class `SuffixArray`. Instances of this class are initialized with a document. During the initializion of an instance, you should construct a suffix array that is stored as an instance variable. For that initialize a list with all integers `[0,n-1]`. Use `mysort` to sort the array. You need to implement a comparison function for integers that has access to the document to compare integers as explained above. Note that you would want to nest functions here to make the document accessable from within the `compare` function without having to pass the document as an explicit parameter. The `search` and `contains` methods of this class should use generic binary search over the suffix array to find strings.
