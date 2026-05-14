# 🧠 Problem: Reorder Linked List

> You are given the `head` of a singly linked-list.
> 
> The positions of a linked list of `length = 7` for example, can initially be
> represented as:
> 
> `[0, 1, 2, 3, 4, 5, 6]`
> 
> Reorder the nodes of the linked list to be in the following order:
> 
> `[0, 6, 1, 5, 2, 4, 3]`
> 
> Notice that in the general case for a list of `length = n` the nodes are
> reordered to be in the following order:
> 
> `[0, n-1, 1, n-2, 2, n-3, ...]`
> 
> You may not modify the values in the list's nodes, but instead you must
> reorder the nodes themselves.

[View on NeetCode](https://neetcode.io/problems/reorder-linked-list/)  
[View on LeetCode](https://leetcode.com/problems/reorder-list/)

---

## ✨ Initial Thoughts

This is a Medium problem, so I was expecting to have to sit with this for a bit,
but the initial approach came to me immediately once I wrote down a visual
representation of what needs to be done.

The reordering is essentially pairing off nodes: the first with the last, the
second with the second-last, etc. All that we need to do is find the length of
the list, and then we can calculate the pairs. We'll need to take care in the
middle, to make sure that the list terminates correctly.

The list should be modified in-place, as that is part of the requirements.

---

## 🚀 Solutions

### 1. Pairing

**Approach:**  
Wire the pairs together: First, find the length of the list, and therefore the
`distance` between the first half of the first pair (index `0`) and the other
half of the first pair (index `len - 1`). Adjust the distance as you work your
way towards the middle, and take care to end the list correctly.

**Complexity:**  
- Time: `O(n²)`
- Space: `O(1)`

**Trade-offs:**  
- Quite simple conceptually
- Inefficient: Creates a nested loop, as you're traversing the length of the
  list every iteration

### 2. Reverse and Merge (Using Floyd)

**Approach:**  
Another way to think of this problem is merging two lists: the `head` to the
middle in order, and the `tail` to the middle in reverse. This means we can: (1)
Find the middle of the list, (2) Reverse the back half, and (3) Merge the two
sublists.

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- Much faster
- This initial implementation has a duplicate middle node which needs to be
  handled (see below)

### 3. Reverse and Merge (Simpler)

**Approach:**  
Exactly the same high-level approach as the above. However, instead of including
the duplicated middle node, cut off the list one node later, and have the end of
the first portion point to `None`. This requires less manual intervention when
merging the lists.

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- Same benefits as [#2](#2-reverse-and-merge-using-floyd)
- Less manual intervention in the merging

---

## 🧪 Tests (edge cases)

- Empty list
- One item in the list
- Two items in the list
- Odd list
- Even list

---

## 📌 Reflections & Takeaways

My initial thought produced a completely functional solution. However, on closer
inspection, I discovered that it resulted in a nested loop (traversing the list
every iteration), and therefore was far from the best time complexity.

Sometimes a problem can have multiple high-level approaches, and it's important
to evaluate the trade-offs of each. The Reverse and Merge approach isn't
conceptually more complex than the Pairing approach, however it gives far better
performance and time complexity.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
