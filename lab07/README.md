# Lab 7 - Hashtables

## Extensible Hashtables with Open Addressing

In this lab you will build a hashtable implementation that uses **linear probing** to solve collisions and that increases the hashtable size automatically if the hashtable's fillfactor exceeds a given threshold. Once the hashtable if more than `fillfactor` full, you should rebuild it, doubling the number of buckets. For example, if you have a hashtable with fillfactor `0.5` and `100` buckets, then you need to rebuilt it using `200` buckets once it stores more than `0.5 * 100 = 50` elements.

You should implement all the methods shown below.

### Methods

Some remarks regarding the methods you need to implement

- `__iter__(self)` - show iterate over the keys of the hashtable
- `__getitem__(self,key)` - needs to raise a `KeyError` if `key` does not exist in the hashtable
- `__len__(self)` - returns the number of entries stored in the hashtable
- `items(self)` - should be a generator returning the entries of the hash table as tuples `(key,value)`

### Skeleton

```python
class ExtensibleHashTable:

    def __init__(self, n_buckets=1000, fillfactor=0.5):
        self.n_buckets = n_buckets
        self.fillfactor = fillfactor
        self.buckets = [None] * n_buckets
        self.nitems = 0

    def find_bucket(self, key):
        # BEGIN_SOLUTION
        # END_SOLUTION

    def __get_item__(self,  key):
        # BEGIN_SOLUTION
        # END_SOLUTION

    def __set_item__(self, key, value):
        # BEGIN_SOLUTION
        # END_SOLUTION

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False

    def __len__(self):
        return self.nitems

    def __bool__(self):
        return self.__len__() != 0

    def __iter__(self):
        ### BEGIN SOLUTION
        ### END SOLUTION

    def keys(self):
        return iter(self)

    def values(self):
        ### BEGIN SOLUTION
        ### END SOLUTION

    def items(self):
        ### BEGIN SOLUTION
        ### END SOLUTION

    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'

    def __repr__(self):
        return str(self)
```
