# ARRAYS

## What is an array?

An **array** is a collection of elements of the same data type stored in **contiguous memory locations**.

## Why do we need arrays?

Arrays allow multiple related values to be stored in a single data structure and accessed using an index.

They are particularly useful when fast random access to elements is needed.

## Array operations

| Operation | Description | Time Complexity |
|---|---|---|
| Access | Get an element using its index | $O(1)$ |
| Traversal | Visit every element | $O(n)$ |
| Search | Find a particular element | $O(n)$ |
| Insertion | Add an element | $O(n)$ |
| Deletion | Remove an element | $O(n)$ |
| Update | Change an existing element | $O(1)$ |

---

## Traversal

- The process of visiting elements in an array sequentially, typically to perform a specific operation.
- Two common types are **linear** and **reverse** traversal.
- Traversal can be implemented using a `while` loop or a `for` loop.

### Linear traversal

- Visits each element starting from the first and moving towards the last.
- Time complexity: $O(n)$ because every element may need to be visited.
- Auxiliary space: $O(1)$ because only a constant amount of additional memory is used.

### Reverse traversal

- Visits each element starting from the last and moving towards the first.
- Time complexity: $O(n)$ because every element may need to be visited.
- Auxiliary space: $O(1)$ because only a constant amount of additional memory is used.

---

## Accessing elements

Elements can be accessed using their index:

```py
arr[index]
```
- Time complexity: $O(1)$
- The memory address of an element can be calculated using its index because array elements have the same size and are stored contiguously.

## Modifying elements

- An element can be modified by accessing its index and assigning it a new value.

```py
arr[index] = new_value
```
- Time complexity: $O(1)$

## Advantages
- Random access takes $O(1)$ time.
- Multiple values of the same data type can be stored in one structure.
- Contiguous storage can improve cache performance.

## Disadvantages
- Fixed-size arrays cannot easily grow or shrink. Resizing requires allocating new memory and copying elements.
- Inserting or deleting elements may require other elements to be shifted, resulting in O(n) time complexity.
- Elements must generally be of the same data type.