# Trees

## 1. What is a Tree?

A **tree** is a non-linear data structure that organises data hierarchically using **nodes** connected by edges.

- **Root:** Top node; has no parent.
- **Parent / Child:** Directly connected nodes above / below one another.
- **Leaf (external node):** Node with no children.
- **Internal node:** Node with at least one child.
- **Sibling:** Nodes sharing the same parent.
- **Ancestor / Descendant:** Nodes above / below a given node along a path.
- **Subtree:** A node and all its descendants.
- **Neighbour:** A node's parent or children.

### Levels and Height

- **Depth (level) of a node:** Number of edges from the root to that node. The root has depth 0.
- **Height of a tree:** Number of edges on the longest path from the root to a leaf.
  - A tree containing only a root has height 0.
  - An empty tree is conventionally assigned height -1.

## 2. Tree Representation in Python

A tree can be represented using nodes that store data and references to other nodes.

For a general tree, each node can have any number of children:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
```

For a binary tree, each node instead has separate `left` and `right` references.

## 3. Advantages and Disadvantages

**Advantages**
- Naturally represents hierarchical data, e.g. file systems.
- Can support efficient searching, insertion and deletion.
- Dynamic structure; can grow and shrink as needed.
- Ordered trees can support efficient sorting and minimum/maximum operations.

**Disadvantages**
- Requires memory for nodes and their references.
- Unbalanced trees can have poor performance.
- More complex to implement and manipulate than basic linear structures.

## 4. Types of Trees

- **General (N-ary) tree:** Nodes can have any number of children.
- **Binary tree:** Each node has at most two children.
- **Binary Search Tree (BST):** A binary tree ordered by key values; values in the left subtree are smaller and values in the right subtree are greater, assuming distinct keys.
- **Balanced binary tree:** A tree maintained to prevent excessive height, improving operation efficiency.
- **Fenwick Tree (Binary Indexed Tree):** A specialised structure for efficient prefix-sum queries and updates on an array.