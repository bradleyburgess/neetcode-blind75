# 🧠 Problem: Reverse Linked List

> Given the beginning of a singly linked list `head`, reverse the list, and
> return the new beginning of the list.

[View on NeetCode](https://neetcode.io/problems/reverse-a-linked-list/)  
[View on LeetCode](https://leetcode.com/problems/reverse-linked-list/)

---

## ✨ Initial Thoughts

This is the first of the Linked List problems. I can see two broad ways to
tackle reversing a linked list:

1. Traverse the list to the end, adding each node to a stack, and then pop nodes
   off the stack, reversing the `next` relationships.
2. Iteratively reverse the `next` relationships by stepping through the list,
   using a `temp` node as a buffer.

---

## 🚀 Solutions

### 1. Brute Force

**Approach:**  
Add the **value** of each `node` to a stack. Pop off the stack, creating new
`node`s with the values from the stack.

**Complexity:**  
- Time: `O(n)` (in practice, `2n`)
- Space: `O(n)`

**Trade-offs:**  
- Very simple
- Not a huge performance hit, but you are having to handle each node twice: once
  traversing to the end of the list, and secondly making your way back,
  reversing the relationships

### 2. Brute Force: Optimized

**Approach:**  
Very similar to above. But instead of creating new `node`s from the values, just
reverse the relationships on the stack.

**Complexity:**  
- Time: `O(n)` (in practice, `2n`)
- Space: `O(n)`

**Trade-offs:**  
- Also very simple
- Less memory, as we're not creating new `node`s
  
  ### 3. Iterative

  **Approach:**  
Go through the list once, iteratively rewiring the `next` relationships, using a
`temp` node to fascilitate the joining.

**Complexity:**  
- Time: `O(n)` (actually)
- Space: `O(1)`

**Trade-offs:**  
- A little more work logically
- Uses no extra memory

---

## 🧪 Tests (edge cases)

- Empty list
- One item in the list

---

## 📌 Reflections & Takeaways

**Linked Lists** are great for linear, 1D relationships. This problem is not
majorly complex, but it can be a little "finicky", as you're having to really
think through the nodes and the `next` relationships, especially in the
iterative approach.

I also got caught out in the optimized brute force solution, as I initially
forgot to set the last node (the original `head` node) `next` to `None`, which
resulted in an infinite loop between the original `head` node and the original
second node, each pointing to eachother.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
