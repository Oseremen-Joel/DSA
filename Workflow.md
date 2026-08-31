# Step 1 — Read the basic GFG article

Start with the GeeksforGeeks article on **Arrays**.

Don't try to memorise anything yet.

As you read, focus on answering these questions:

1. What is an array?
2. Why would I use one?
3. How is data stored?
4. How do I access an element?
5. What operations can I perform?
6. What are the advantages and disadvantages?
7. What is the time complexity of each operation?

While reading, you can put very rough notes into your `.md` file, such as:

```md
# Arrays

## What is an array?

- 

## Operations

- Access:
- Search:
- Insertion:
- Deletion:

## Advantages

-

## Disadvantages

-
```

Don't fill everything in immediately. Just use it as a place to collect information.

---

# Step 2 — Understand arrays conceptually

Before coding, make sure you understand this:

```text
Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
Array:  [10] [20] [30] [40] [50]
```

If I want:

```python
array[3]
```

I immediately get:

```text
40
```

This is **O(1)** because the computer can directly access the element at that index.

You don't need to memorise the formal mathematical definition of Big O yet.

Just understand:

> **Accessing an array element by index is fast because the computer knows exactly where to look.**

Then contrast that with searching:

```python
for x in array:
    if x == 40:
        ...
```

You may have to check:

```text
10 → 20 → 30 → 40
```

So that's **O(n)** in the worst case.

At this point, go back to GFG and make sure you understand **why** the complexities they give you are what they are.

---

# Step 3 — Learn the operations

Go through the common array operations.

I'd make a table in your notes:

```md
## Time Complexity

| Operation | Time Complexity |
|---|---|
| Access by index | O(1) |
| Search | O(n) |
| Insertion | O(n) |
| Deletion | O(n) |
```

Don't blindly trust the table, though.

Ask:

> "Why?"

For example, consider:

```text
[10, 20, 30, 40, 50]
```

You want to insert `25`:

```text
[10, 20, 25, 30, 40, 50]
```

The elements after `25` have to move.

That's why insertion can be **O(n)**.

Similarly, deleting:

```text
[10, 20, 30, 40, 50]
         ↓
       delete
         ↓
[10, 20, 40, 50]
```

Elements may need to shift.

---

# Step 4 — Learn the difference between arrays and Python lists

This is **particularly important for you**.

You're learning DSA using Python, so don't just blindly assume:

> Python list = array

It's more accurate to think:

> Python's `list` is a **dynamic array-like data structure**.

You should understand what that means.

Look at the Python documentation for `list` after you've finished the basic GFG material.

Explore:

```python
numbers.append(5)
numbers.insert(0, 5)
numbers.pop()
numbers.remove(5)
numbers.extend([1, 2, 3])
numbers.sort()
numbers.reverse()
```

You don't need to memorise every method.

Your goal is to start thinking:

> "I need to do X. Does Python's standard library already have something for that?"

That's one of the skills you specifically said you wanted to improve.

---

# Step 5 — Implement an array yourself

This is where I'd spend a good chunk of your time.

Since Python's `list` already does everything for you, I wouldn't just write:

```python
arr = []
arr.append(1)
```

You already know how to do that.

Instead, implement a simplified **dynamic array** yourself.

Create a file:

```text
dynamic_array.py
```

Start with:

```python
class DynamicArray:
    def __init__(self):
        ...
```

Then try to implement:

```text
append()
get()
set()
insert()
remove()
pop()
resize()
```

Don't immediately look up an implementation.

Try to figure out how you'd do it.

You might encounter questions like:

> "How do I store the elements?"

> "What happens when I run out of space?"

> "How do I insert something in the middle?"

> "How do I remove something?"

This is where you're actually learning.

---

# Step 6 — Investigate something you don't understand

You'll probably reach something like:

```text
What happens when the array is full?
```

Suppose you have:

```text
Capacity = 4

[10, 20, 30, 40]
```

And you want:

```python
append(50)
```

You need to:

1. Create a larger array.
2. Copy the existing elements.
3. Add `50`.

This is where you should investigate **dynamic array resizing**.

You should understand why:

```text
append → usually O(1)
resize → O(n)
```

but append is generally considered:

```text
O(1) amortised
```

You don't need to master amortised analysis yet. Just understand the basic idea:

> Most appends are cheap, but occasionally an expensive resize happens. Spread over many appends, the average cost is O(1).

---

# Step 7 — Do a small project

Now use arrays/lists for something.

I suggest something simple, like a **leaderboard**:

```text
players = [
    ("Alex", 100),
    ("Bob", 75),
    ("Charlie", 120)
]
```

Implement:

* Add player
* Remove player
* Update score
* Find player
* Sort leaderboard
* Display top 10

Then start asking questions.

> "How quickly can I find a player?"

Your list solution might be:

```python
for player in players:
    if player.name == target:
        ...
```

That's O(n).

Later, when you learn hash tables/dictionaries, you'll realise you could potentially do this much faster.

**This is the kind of connection you want to make throughout DSA.**

---

# Step 8 — Solve problems

Now do maybe **5–10 easy array problems**.

Don't try to grind 50.

Start with things like:

* Find the largest element
* Reverse an array
* Find the second largest
* Remove duplicates
* Move zeroes
* Rotate an array
* Find a missing number
* Two Sum
* Merge sorted arrays

For every problem, follow this process:

### 1. Try it yourself

Don't look at the solution.

### 2. Analyse your solution

Ask:

```text
Time complexity?
Space complexity?
```

### 3. Try to improve it

Ask:

> "Can I use less memory?"

> "Can I make it faster?"

> "Am I repeatedly doing the same work?"

### 4. Look at the solution

Only if necessary.

### 5. Understand the solution

Don't just copy it.

Ask:

> "What did they notice that I didn't?"

That last question is probably the most valuable part.

---

# Step 9 — Revisit the topic

After you've done all of that, close GFG and your notes.

Try to explain arrays without looking.

You should be able to answer:

```text
What is an array?

Why is accessing arr[i] O(1)?

Why is searching O(n)?

Why can insertion/deletion be O(n)?

What is a dynamic array?

Why does resizing happen?

Why is append amortised O(1)?

What is Python's equivalent?

When would I use a list?
```

If you can answer those comfortably, **you're done with the topic**.

---

# Step 10 — Finish your `.md` notes

Only now should you clean up your notes.

I'd aim for something like this:

```md
# Arrays

## What is an array?

An array stores elements in a sequential/contiguous block of memory,
allowing elements to be accessed directly using an index.

Python's `list` is a dynamic array-like data structure.

## Operations

| Operation | Time |
|---|---|
| Access by index | O(1) |
| Search | O(n) |
| Insert | O(n) |
| Delete | O(n) |
| Append | O(1) amortised |

## Advantages

- Fast random access using an index
- Simple to use
- Good cache locality

## Disadvantages

- Inserting/deleting elements can be expensive
- Resizing a dynamic array can require copying elements

## Python

Common list operations:

- `append()`
- `extend()`
- `insert()`
- `pop()`
- `remove()`
- `sort()`
- `reverse()`

## Key ideas

- Indexing is O(1) because the location can be calculated directly.
- Searching an unsorted array is O(n).
- Inserting/deleting may require elements to shift.
- Dynamic arrays resize when capacity is reached.
- Append is O(1) amortised.

## What I implemented

- Dynamic array
- [link to GitHub/code]

## Problems solved

- [Problem]
- [Problem]
- [Problem]

## Things I struggled with

- 
```

The important thing is that **you shouldn't write all of that before learning**. Your final notes are the *result* of the learning process.

---

# Your overall process

I'd make this your standard workflow for every DSA topic:

> **1. GFG → Understand the concept**
> ↓
> **2. Write rough notes → Only key ideas**
> ↓
> **3. Understand complexity → Know why**
> ↓
> **4. Implement from scratch → Don't copy**
> ↓
> **5. Investigate Python's implementation/tools → Read docs**
> ↓
> **6. Build a small practical project**
> ↓
> **7. Solve 5–10 problems**
> ↓
> **8. Revisit from memory**
> ↓
> **9. Clean up `.md` notes**
> ↓
> **10. Move to the next topic**

I'd strongly recommend **not getting stuck trying to perfect arrays**. Once you've implemented a dynamic array, understood its complexity, used Python lists, and solved some problems, move on. You'll understand arrays even better later when you learn **stacks, queues, hash tables, heaps, and sorting**, because you'll repeatedly see where arrays are useful and where they aren't.

For **your first topic**, I think the most important thing is to learn this workflow itself. Once you've done arrays this way, you can reuse the exact same process for every DSA topic you study.
