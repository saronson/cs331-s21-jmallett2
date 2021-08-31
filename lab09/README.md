# Lab 9 - BS-trees with History Using Immutability

In this lab we will develop a binary search tree that allows access to past states of the tree. That is, the data structure maintains a list of the roots of previous versions of the tree and allows access to this past versions. We starting with a single versions that is an empty tree:

```python
t = HBStree()
t
```

```
================================================================================
Version: 0
================================================================================
 -
```

Every insert and delete operation will create a new version of the tree. For example,

```python
t = HBStree()
t.insert(3)
t.insert(1)
t.insert(5)
t.insert(2)
t.insert(8)
t.insert(4)
t
```

```
================================================================================
Version: 0
================================================================================
 -
================================================================================
Version: 1
================================================================================
   3
================================================================================
Version: 2
================================================================================
       3
   1       -
================================================================================
Version: 3
================================================================================
       3
   1       5
================================================================================
Version: 4
================================================================================
               3
       1               5
   -       2       -       -
================================================================================
Version: 5
================================================================================
               3
       1               5
   -       2       -       8
================================================================================
Version: 6
================================================================================
               3
       1               5
   -       2       4       8
```

```python
t.delete(5)
t.delete(2)
t
```

```
================================================================================
Version: 0
================================================================================
 -
================================================================================
Version: 1
================================================================================
   3
================================================================================
Version: 2
================================================================================
       3
   1       -
================================================================================
Version: 3
================================================================================
       3
   1       5
================================================================================
Version: 4
================================================================================
               3
       1               5
   -       2       -       -
================================================================================
Version: 5
================================================================================
               3
       1               5
   -       2       -       8
================================================================================
Version: 6
================================================================================
               3
       1               5
   -       2       4       8
================================================================================
Version: 7
================================================================================
               3
       1               4
   -       2       -       8
================================================================================
Version: 8
================================================================================
               3
       1               4
   -       -       -       8
```

A naive way to store all versions of a tree is to create a copy at each operation and then execute the destructive operation (insert or delete) on this copy. However, for `n` insert operations this would require `O(n^2)` space (`SUM[i=0,n] i` nodes in total in the trees encoding the versions). In your implementation, you will use a smarter storage scheme that allows nodes to be shared across versions of the trees. We have to be careful when sharing nodes, because changing a node in one version would then modify all other versions of the tree that share that node. The solution we are applying here is to use immutable data structures as discussed next.

## Immutable Data Structures

As discussed in the beginning of the course, a data structure is immutable if it cannot be changed after creation. For the purpose of this exercise, we will make the node structure immutable. Implementing trees with immutable node data structures is how tree-based data structures are implemented in languages which do not have mutable objects, e.g., functional programming languages that you may learn about in future courses.

The consequence of making nodes immutable is that whenever we want to modify the structure or content of the tree, we have to create new nodes. Naively, we could construct a new tree from scratch for every update. As discussed above, we want to be smarter and share nodes across versions where possible. For that you will implement the insertion and deletion algorithms discussed next.

## The `HBStree` data structure

Before discussing the algorithms for the insert and delete operations, we first discuss some other requirements for the implementation:

- your implementation should maintain a list `self.root_versions` that stores the roots of all versions of your tree from oldest to newest. That is, the root of the current version of the tree is `self.root_versions[-1]`.
- the immutable node datastructure is provided as class `INode`. Do not modify this class.
- when creating a HBStree, initially it should contain one version that is the empty tree: `self.root_versions = [None]`.
- `__getitem__(self,key)` should return `key` if it exists in the current version of the tree and otherwise raise an `KeyError`.
- `delete` should not throw an error if the key to be delete does not exist in the current version of the tree. Also do **not** create a new version when the key does not exist.
- `insert` should not throw an error if the key to be inserted does already exist in the tree. In this case you should **not** create a new version of the tree.
- `version_iter(self, timetravel=0)` iterate over all keys in a particular version of the tree in sort order. The version is specified using the `timetravel` argument. `0` is the current version, `1` is the previous version, and so on.
- you can use the `__repr__` or `__str__` methods of the tree to visualize all versions. This creates a printout as shown above.

## Immutable BS-trees Operations

Note that the provided skeleton code implements a method `share_factor` which calculates the average number of times each node is shared. For example, a share factor of `2.0` means that each node appears on average in two versions to the tree. You can use this to better understand the behavior of your data structure.

### Insert

To insert a new key, we first need to find the position in the tree where the key should be inserted. So far this is the same as in a regular BS-tree. For example, consider the tree shown below (only the latest version is shown). We give each nodes an identifier to be able to illustrate sharing of nodes between the versions before and after the insert.


```
================================================================================
Version: 7
================================================================================
                  5[a]
       2[b]                  7[c]
  1[d]       3[e]       6[f]       8[g]
```

Assume we want to insert key `9`. This key would be inserted as the right child of node `g` (with value 8). However, since we cannot modify `g`, we have to create a new node to replace `g` in the new version of the tree. This in turn requires us to replace `c` with a new node that points to the new node replacing `g`. Observe, that this always will cause us to replace all ancestors of the node we modifying including the root. The replacement of the root will become the root of the new version of the tree. In our example, we have to create new versions of `a`,`c`, and `g`. The new version of `a` becomes the new root of the tree:

```
================================================================================
Version: 8
================================================================================
                  5[h]
       2[b]                  7[i]
  1[d]       3[e]       6[f]       8[j]
                                       9[k]
```

Note that since we replace all nodes on a path from the root to a leaf to deal with an insertion, the worst-case complexity is `O(height(tree))`.

### Delete

The algorithm for deletion uses a similar trick. When deleting a node, we need to create a new version of the parent of the node that no longer points at the deleted node and this again causes to replace all nodes on the path from the root to the parent of the deleted node. For example, let us delete key `3` (node `e`) in our example above. We need to replace `b` and `h` with new nodes (`l` and `m`). Node `m` becomes the root of the new version of the tree.

```
================================================================================
Version: 9
================================================================================
                  5[m]
       2[l]                  7[i]
  1[d]                 6[f]       8[j]
                                       9[k]
```


Recall that when deleting an intermediate node from a binary search tree, we have to deal with three cases:

1. The node only has a left child. In this case we can replace the node with its left child (and create new versions of its ancestors)
2. The node only has a right child. In this case we can replace the node with its right child (and create new versions of its ancestors)
3. The node has both a left and a right child. In this case, we have to remove the largest element `x` from the left subtree (this is a deletion within the left subtree that we have to treat just like a user provided deletion) and replace the node with a new node with  `x` as a value and the modified left child of the node (after deleting `x`) as the left child and the original right child of the node as the right child.

Let us illustrate the most complex case (3) using our running example. Let us delete key `5` from the tree which is currently the root of the tree (node `m`). Since `m` has two children, we need to delete the largest value `x=2` from the left subtree under `m`. Since `l` (the node storing `2`) has only one child we can replace it with that child (node `d`). Then we create a new node replacing `m`, say `n` which has two children, then modified left subtree rooted at `d` and the original right subtree rooted at `i`.  The final result is

```
================================================================================
Version: 10
================================================================================
                  2[n]
       1[d]                  7[i]
                       6[f]       8[j]
                                       9[k]
```
