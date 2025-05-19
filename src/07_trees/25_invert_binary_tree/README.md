# 🧠 Problem: Invert Binary Tree

> You are given the root of a binary tree `root`. Invert the binary tree and
> return its `root`.

[View on NeetCode](https://neetcode.io/problems/invert-a-binary-tree/)  
[View on LeetCode](https://leetcode.com/problems/invert-binary-tree/)

---

## ✨ Initial Thoughts

Problems where the quantity or depth isn't known automatically make me think to
reach for **recursion**. I would like to solve this both iteratively and
recursively, but we'll start with the latter.

---

## 🚀 Solutions

### 1. Recursive

**Approach:**  
Call the method on the `root`. The method will do a null check on `root` and
then swap the `left` and `right` nodes, then calling itself on the `left` and
`right` nodes in turn. (This results in a pre-order **depth-first search**; see
below.)

**Complexity:**  
- Time: `O(n)`
- Space: `O(h)`, where `h` is the height of the tree (each level will be added
  to the call stack)

**Trade-offs:**  
- Extremely simple to implement
- A little memory required, due to piling the levels on the call stack

### 2. Iterative: DFS Stack

**Approach:**  
There are two main ways to traverse a tree: **depth-first search** (DFS) and
**breadth-first search** (BFS). The former involes going all the way down (often
 left first) before you move across; the latter has you doing each level in its
entirety before you move down. There are thus two ways to invert a tree
iteratively: via **DFS**, which uses a **stack**; and via **BFS**, which uses a
**queue**. The [recursive solution above](#1-recursive) necessitates a pre-order
DFS; it's a very similar result. 

Add the `root` node to the stack. From there, we `pop` off a node from the
stack, process it, and then add it's children to the stack, which in turn get
popped off.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

**Trade-offs:**  
- Very similar to recursive approach
- Slightly more complicated implementation
- Worst-case space is `O(n)` for highly **unbalanced** trees (all `left` or all
  `right`). This is similar to the [recursive approach](#1-recursive).

### 3. Iterative: BFS Queue

**Approach:**  
This approach to the iterative solution uses **BFS** and a **queue**. A node
(first the `root`) gets dequeued and processed; its children then get added to
the end of the queue. This ensures a level is completed before moving down to
any child nodes.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

**Trade-offs:**  
- Very similar to DFS / Stack in complexity and implementation
- Worst-case space is `O(n)` for highly **balanced** trees. As we descend the
  levels, the nodes increase exponentially.

---

## 🧪 Tests (edge cases)

- Null root
- Only one level
- Unbalanced tree

---

## 📌 Reflections & Takeaways

This problem is much simpler when done recursively. Again, there are trade-offs,
and it's helpful to know something about your data before deciding which
implementation to use.

If the tree is very balanced, the [BFS / Queue](#3-iterative-bfs-queue)
implementation is going to use the most memory. If it's unbalanced, a [DFS /
Stack](#2-iterative-dfs-stack) approach will be more memory-efficient. A
recursive approach might be best if you're not sure.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
