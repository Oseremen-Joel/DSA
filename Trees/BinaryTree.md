# Binary Trees

## 1. What is a Binary Tree?

A **binary tree** is a tree where each node has at most two children: a **left child** and a **right child**.

Each node stores:
- Its data.
- A reference to its left child.
- A reference to its right child.

### Implementation in Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create nodes
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)
```

Each node references its children, linking the individual nodes into a tree.

## 2. Types of Binary Trees

- **Full:** Every node has either zero or two children.
- **Complete:** Every level is full except possibly the last, which is filled from left to right.
- **Perfect:** Every internal node has two children, and all leaves are at the same depth.
- **Balanced:** Height is kept sufficiently small relative to the number of nodes. The exact condition depends on the balancing rule; for example, AVL trees require the heights of each node's two subtrees to differ by at most one.

These definitions are different. In particular, every perfect binary tree is full and complete, but not every full or complete tree is perfect.

## 3. Binary Tree Properties

Let:
- $(h)$ = height of the tree, measured in edges.
- $(N)$  = total number of nodes.
- $(L)$  = number of leaves.
- $(T)$  = number of nodes with two children.

### Maximum nodes at depth $(l)$ 

$$
\boxed{2^l}
$$

Each node can have at most two children, so each level can contain at most twice as many nodes as the previous level.

### Maximum nodes in a tree of height $(h)$ 

$$
\boxed{N_{\max}=2^{h+1}-1}
$$

A tree has the maximum number of nodes when every level is full:

$$
1+2+4+\cdots+2^h=2^{h+1}-1
$$

### Minimum height for $(N)$ nodes

$$
\boxed{h_{\min}=\lfloor\log_2 N\rfloor}
$$
Since a tree of height $(h)$ can contain at most $(2^{h+1}-1)$ nodes:

$$
N\leq 2^{h+1}-1
$$

Rearranging gives $(h\geq\log_2(N+1)-1)$, which implies the integer lower bound above.

This minimum is achieved by filling the levels as completely as possible.

### Minimum height for $(L)$ leaves

$$
\boxed{h_{\min}=\lceil\log_2 L\rceil}
$$

A binary tree of height $(h)$ can have at most $(2^h)$ leaves. Therefore, $(L\leq 2^h)$, giving the minimum possible height.

### Leaves and internal nodes in a full binary tree

$$
\boxed{L=T+1}
$$

Proof:
- Every node with two children contributes two edges, so there are $(2T)$ edges.
- Any non-empty tree with $(N)$ nodes has $(N-1)$ edges.
- Since a full binary tree has $(N=T+L)$:

$$
2T=T+L-1
$$

Therefore, $(L=T+1)$.

### Number of edges

$$
\boxed{E=N-1}
$$

Every node except the root has exactly one parent, so each of the other $(N-1)$ nodes contributes one parent-child edge.

## 4. Tree Traversals

A **traversal** visits every node in a specified order. The main binary-tree traversals are depth-first traversals and breadth-first traversal.

### Depth-first traversal (DFS)

DFS explores a subtree before moving to another subtree. The three main orders are:

| Traversal | Order | Common use |
|---|---|---|
| **Preorder** | Root → Left → Right | Copying/serialising a tree |
| **Inorder** | Left → Root → Right | Produces sorted order in a BST |
| **Postorder** | Left → Right → Root | Deleting a tree; evaluating expression trees |

Example tree:

```text
      1
     / \
    2   3
   / \
  4   5
```

- Preorder: `1, 2, 4, 5, 3`
- Inorder: `4, 2, 5, 1, 3`
- Postorder: `4, 5, 2, 3, 1`

### Recursive implementation

```python
def preorder(node):
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)
```

The base case `node is None` stops recursion when a missing child is reached.

All three traversals take **$(O(N))$ time** because each node is visited once. Their auxiliary space is **$(O(h))$** for the recursive call stack, where $(h)$ is the tree's height.

### Breadth-first traversal (BFS / level order)

Visits nodes level by level, from left to right. It uses a **queue** (FIFO).

Algorithm:
1. Add the root to the queue.
2. While the queue is not empty:
   - Remove the front node and visit it.
   - Add its left child if it exists.
   - Add its right child if it exists.

```python
from collections import deque

def level_order(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
```

- **Time Complexity:** $(O(N))$.
- **Auxiliary space:** $(O(N))$ in the worst case, due to the queue.

### Zigzag traversal

Like level order, but alternates direction at each level: left-to-right, then right-to-left, and so on.

It can be implemented using BFS, reversing the output for every other level.

## 5. Searching a Binary Tree

Unless the tree has an ordering property, such as a BST, there is no general way to choose which subtree must contain a target.

Traverse the tree and compare each node's value with the target. Stop when the target is found; if traversal finishes first, it is absent.

- **Time Complexity:** $(O(N))$ in the worst case.
- **Recursive auxiliary space:** $(O(h))$.
- **Iterative auxiliary space:** Depends on the stack or queue used; up to $(O(N))$.

A BST can search more efficiently by using its ordering property.

## 6. Graph DFS and BFS

DFS and BFS also work on **graphs**, which may contain cycles or disconnected components. Binary-tree traversal is a specialised use of these ideas.

### DFS — Depth-first search

- Follow a path as deeply as possible, then backtrack.
- Implement using recursion or a stack.
- Use a `visited` array/set to avoid revisiting vertices in cyclic graphs.

### BFS — Breadth-first search

- Visit vertices in increasing distance from the source, level by level.
- Implement using a queue, such as Python's `collections.deque`.
- Mark vertices as visited when they are added to the queue, preventing duplicates.

### Connected and disconnected graphs

For a connected graph, starting at one source reaches every vertex. For a disconnected graph, repeat the traversal from every vertex that remains unvisited to cover all components.

With an adjacency-list representation:

- **Time:** $(O(V+E))$, where $(V)$ is the number of vertices and $(E)$ is the number of edges.
- **Auxiliary space:** $(O(V))$ for the visited structure and traversal stack or queue, excluding the graph representation and output.

For an undirected graph, each edge usually appears in two adjacency lists, but this does not change the asymptotic time complexity.

## 7. Advantages, Disadvantages and Uses

**Advantages**
- Naturally represents hierarchical data.
- Can support efficient searching and updates when suitably ordered or balanced.
- Can grow and shrink dynamically.

**Disadvantages**
- Each node requires references to its children.
- Recursive traversal can use substantial stack space for very tall trees.
- An unbalanced tree can lead to poor performance.

**Uses**
- Representing hierarchical data and decision trees.
- Expression trees for mathematical expressions.
- Searching and sorting with binary search trees.
- Representing structured data in compilers and other software.
