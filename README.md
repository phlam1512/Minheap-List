# Minheap List
Implementation of a min-heaplist, which is a variant of mini-heap.

## Aim
The aim is to implement a data structure called min-heaplist, without the use of Python library functions. The specifications of the min-heaplist data structure is given in the following section.

## Specification
The operations supported by a min-heaplist are as follows:
- `insert(x)`: Inserts a new value to the min-heaplist in $O(1)$ time, by adding a single-element min-heap to the root list.
- `linkheaps(h1,h2)`: Combines two min-heaps to make a single min-heap. Returns a pointer to the new min-heap.
- `extractMin()`: Removes and returns an element with the minimum value. The rootlist is then "cleaned-up" by combining all min-heaps in the collection into a single min-heap.
- `decreaseKey(n,k)`: Decreases the value stored at node `n` to a given value `k`.
- `union(H)`: Combines the current min-heaplist with another min-heaplist `H`.

## Remarks
This project is submitted as part of assessed coursework.

## Files
- `minheaplist.py` contains all Python code.
