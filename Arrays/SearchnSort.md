# Searching algorithms

## Linear search

- Searching involves checking elements to find a target value. 
- Types: Linear, Binary
- Linear search checks each element sequentially until the target is found:
```py
arr = [10, 20, 30, 40, 50]
target = 30
found = False

for i in range(len(arr)):
    if arr[i] == target:
        found = True
        break

if found:
    print("Element found!")
else:
    print("Element not found!")
```
Output: 
```
Element found!
```
- Time complexity: `O(n)` in the worst case because every element may need to be checked.
- Auxiliary space: `O(1)` because only a constant amount of additional memory is used.

### Advantages
- Simeple to implement 
- No prereuisites
- Constant space complexity
- Fast for smaller datasets, especially if the target is the first element


### Disadvantages
- Inefficient for large datasets

---

## Binary search

- Binary searcch is a searching algorithm that operates on a sorted or monotonic search space
    - a monotonic search space just means the target property changes no more than once throughout the range of inputs. In our case this means the array is either always increasing or decreasing as you go from left to right

- prerequisites:
    - The data structure must be sorted. (as it needs to know which half to eliminate based on element sizes in order)
    - Access to any element of the data structure should take constant time. (to maximise the efficiency)

1. Divide the search space into two halves by finding the middle index "mid". 
2. Compare the middle of the search space with the key. If the key is found at middle, the process is terminated. If the key is not found at middle, choose which half will be used as the next search space:
    - If the key is smaller than the middle, then the left side is used for next search.
    - If the key is larger than the middle, then the right side is used for next search.
3. This process is continued until the key is found or the total search space is exhausted.

```py
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return False 


arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, x)
if result:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
```
Output: 
```
"Element is present at index 3
```
- Time complexity: $O(log~n)$ in the worst case because the list is halved each iteration.
- Auxiliary space: $O(1)$ because only a constant amount of additional memory is used. (`low`, `mid` and `high`)

### Advantages
- Very efficient for large datasets

### Disadvantages
- Requires array to be sorted
- Overkill for small datasets, linear search is better

---

# Sorting algorithms 
- Sorting algorithms arrange data in a specific order.
- Types: Bubble, Insertion

## Bubble Sort
- Bubble sort works by:
    - Traversing the array, repeatedly swapping adjacent elements if they are incorrectly arranged. One iteration of this is called a pass
    - It repeats these passes until the array is sorted. This condition is met when there is a pass with no swaps
    - In every pass, process only those that have already not moved to correct position. After k passes, the largest k must have been moved to the last k positions. This is why the inner loop gets smaller each iteration


```py
# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
```
Output: 
```
[11, 12, 22, 25, 34, 64, 90]
```

- Time Complexity: $O(n^2)$ due to the nested loop
- Auxiliary Space: $O(1)$

### Advantages
- Easy to understand and implement
- Doesn't require additional memory space
- It is a stable sorting algorithm (preserves the relative order of elements with equal keys / values in the sorted output, exactly as they appeared in the input.)

### Disadvantages
- Slow for large dara sets
- Almost no real world applications

---

## Insertion Sort
- Insertion sort iteratively insertine each element of an unsorted list into its correct position in a sorted portion of the list
    - Start with the second element as the first element is assumed to be sorted.
    - Compare the second element with the first if the second iS smaller then swap them.
    - Move to the third element, compare it with the first two, and put it in its correct position. Repeat until the entire array is sorted.

```py
# Python program for implementation of Insertion Sort

# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# A utility function to print array of size n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver method
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
printArray(arr)
```
Output: 
```
[5, 6, 11, 12, 13]
```

- Time Complexity: $O(n^2)$, as the list could be in reverse order
- Auxiliary Space: $O(1)$

### Advantages
- Simple and easy to implement.
- Stable sorting algorithm.
- Efficient for small lists and nearly sorted lists ($O(n)$ inversions).
- Space-efficient as it is an in-place algorithm.
- Adoptive. the number of inversions is directly proportional to number of swaps. For example, no swapping happens for a sorted array and it takes O(n) time only.
    - an inversion is a pair of indices such that i < j and arr[i] > arr[j]

### Disadvantages
- Inefficient for large lists.
- Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.

---

## Selection Sort
- Selection Sort is a comparison-based sorting algorithm. 
- It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.

Steps:
1. Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
2. Then find the second smallest and swap it with the second element. Repeat this until we get all elements moved to correct position.

```py
# Python program for implementation of Selection
# Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
print_array(arr)
```
Output:
```
[11, 12, 22, 25, 64]
```

- Time Complexity: $O(n^2)$, as there are two nested loops
- Auxiliary Space: $O(1)$ the only extra memory used is for temporary variables.

### Advantages
- Easy to understand and implement, making it ideal for teaching basic sorting concepts.
- Requires only a constant $O(1)$ extra memory space.
- It requires less number of memory writes compared to many other standard algorithms.

### Disadvantages
- Selection sort has a time complexity of $O(n^2)$ makes it slower compared to algorithms like Quick Sort or Merge Sort.
- Does not maintain the relative order of equal elements which means it is not stable.

---

## Merge Sort

Steps:

```py

```
Output:
```

```

- Time Complexity: 
- Auxiliary Space: 

### Advantages

### Disadvantages

---