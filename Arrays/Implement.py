class DynamicArray:
    def __init__(self, capacity):
        # Create an array with a fixed initial capacity.
        # None represents unused space.
        self.data = [None] * capacity

        # Number of actual elements currently stored.
        self.size = 0

        # Total amount of space currently available.
        self.capacity = capacity

    def append(self, value):
        # If there is no more unused space,
        # increase the capacity before adding the new element.
        if self.size == self.capacity:
            self.resize()

        # Put the new value in the first unused position.
        # self.size represents the next available index.
        self.data[self.size] = value

        # We now have one more actual element.
        self.size += 1

        print(f"Array (append): {self.data}")
        print("-" * 58)

    def range_check(self, index):
        # Valid elements are stored at indices:
        # 0, 1, 2, ..., size - 1
        #
        # We use size rather than capacity because unused
        # capacity is not considered part of the array yet.
        if index >= self.size or index < 0:
            print("Index out of range")
            return False

        return True

    def get(self, index):
        # Make sure the index refers to an actual element.
        if not self.range_check(index):
            return False

        # Return the element at the requested index.
        # Array access is O(1).
        return self.data[index]

    def set(self, index, value):
        # Make sure the index refers to an actual element.
        if not self.range_check(index):
            return False

        # Replace the existing value with the new value.
        # No elements need to be shifted, so this is O(1).
        self.data[index] = value

        print(f"Array (set): {self.data}")
        print("-" * 58)

    def insert(self, index, value):
        # Make sure the index is valid.
        if not self.range_check(index):
            return False

        # If the array is full, create more space first.
        if self.size == self.capacity:
            self.resize()

        # Shift all elements from 'index' onwards one position
        # to the right.
        #
        # We start from the end and work backwards so that
        # we don't overwrite values before moving them.
        #
        # Example:
        # [10, 20, 30, None]
        #       ↓ insert 15 at index 1
        #
        # Shift 30 → index 3
        # Shift 20 → index 2
        # Then put 15 → index 1
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        # Put the new value into the newly-created space.
        self.data[index] = value

        # The array now contains one additional element.
        self.size += 1

        print(f"Array (insert): {self.data}")
        print("-" * 58)

    def remove(self, index):
        # Make sure the index refers to an existing element.
        if not self.range_check(index):
            return False

        # Shift every element after the removed element
        # one position to the left.
        #
        # Example:
        # [10, 20, 30, 40]
        #       ↓ remove index 1
        #
        # 30 moves to index 1
        # 40 moves to index 2
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        # The last actual element is now duplicated at
        # the previous position, so clear the old final position.
        self.data[self.size - 1] = None

        # The array now contains one fewer element.
        self.size -= 1

        print(f"Array (remove): {self.data}")
        print("-" * 58)

    def pop(self):
        # Cannot remove an element if the array is empty.
        if self.size == 0:
            return False

        # The last element is located at size - 1.
        value = self.data[self.size - 1]

        # Clear the old final position.
        self.data[self.size - 1] = None

        # The array now contains one fewer element.
        self.size -= 1

        # Return the removed value.
        return value

    def resize(self):
        # Increase the capacity.
        # Doubling is more efficient than increasing by 1
        # because it reduces how often we need to copy elements.
        self.capacity *= 2

        # Create a new, larger array.
        new = [None] * self.capacity

        # Copy all existing elements into the new array.
        for i in range(self.size):
            new[i] = self.data[i]

        # Replace the old array with the new one.
        self.data = new
    
    def linear(self, key):
        # Check every element from the beginning of the array.
        # Linear search does not require the array to be sorted.
        for i in range(0, self.size):

            # Check whether the current element is the value we want.
            if self.data[i] == key:
                # Return True as soon as the key is found.
                return True

        # If the loop finishes, the key was not found.
        return False


    def binary(self, key, low, high):
        # If low passes high, there are no elements left to search.
        if low > high:
            return False

        # Find the middle index of the current search range.
        # This avoids potentially overflowing with (low + high) // 2
        # in languages where integer overflow is possible.
        mid = low + (high - low) // 2

        # Check whether the middle element is the key.
        if self.data[mid] == key:
            return mid

        # If the middle element is greater than the key,
        # the key must be in the left half.
        #
        # This only works because the array is sorted.
        if self.data[mid] > key:
            return self.binary(key, low, mid - 1)

        # Otherwise, the key must be in the right half.
        return self.binary(key, mid + 1, high)


    def bubble(self, k):
        # Tracks whether any elements were swapped during this pass.
        # If no swaps occur, the array is already sorted.
        swapped = False

        # Compare adjacent elements.
        #
        # After each pass, the largest unsorted element has moved
        # to the end, so we can ignore the last k elements.
        for i in range(0, self.size - k - 1):

            # If two adjacent elements are in the wrong order,
            # swap them.
            if self.data[i] > self.data[i + 1]:
                self.data[i], self.data[i + 1] = (
                    self.data[i + 1],
                    self.data[i]
                )
                swapped = True

        # If nothing was swapped, the array is sorted.
        # k == self.size is an additional stopping condition
        # once all passes have been completed.
        if not swapped or k == self.size:
            return self.data

        # Perform the next pass.
        # k increases because one more element is now in its
        # final sorted position at the end of the array.
        return self.bubble(k + 1)


    def insertion(self):
        # Start at index 1 because a single element at index 0
        # is already considered sorted.
        for i in range(1, self.size):

            # Store the element we want to insert into the
            # already-sorted section of the array.
            key = self.data[i]

            # Start by looking at the element immediately before key.
            j = i - 1

            # Move larger elements one position to the right
            # until the correct position for key is found.
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1

            # j is now one position before where key belongs,
            # so insert key at j + 1.
            self.data[j + 1] = key
    
    def selection(self):
        # Each iteration places the smallest remaining element into its correct position
        # We stop at size - 1 because once all previous positions are sorted, the final element must already be in place.
        for i in range(0, self.size - 1):

            # Assume the first element in the unsorted section
            # is the smallest.
            smallest = i

            # Search the rest of the unsorted section for
            # an element smaller than our current smallest.
            for j in range(i + 1, self.size):

                # If we find a smaller element, remember its index.
                if self.data[j] < self.data[smallest]:
                    smallest = j

            # Once the smallest element has been found, swap it
            # with the first element of the unsorted section.
            self.data[i], self.data[smallest] = (
                self.data[smallest],
                self.data[i]
            )

        print(self.data)

arr = DynamicArray(10)

arr.data = [2, 1, 5, 6, 3, 9, 7, 4, 10, 8]
arr.size = 10

# 1, 2, 5, 6 | 3, 9, 7


print(arr.selection())
"""
Merge Sort
Quick Sort
""" 

# Practising array implementation