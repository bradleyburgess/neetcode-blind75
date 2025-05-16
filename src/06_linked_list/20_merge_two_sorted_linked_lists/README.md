# 🧠 Problem: Merge Two Sorted Linked Lists

> You are given the heads of two sorted linked lists `list1` and `list2`.
> 
> Merge the two lists into one **sorted** linked list and return the head of the
> new sorted linked list.
> 
> The new list should be made up of nodes from `list1` and `list2`.

[View on NeetCode](https://neetcode.io/problems/merge-two-sorted-linked-lists/)  
[View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## ✨ Initial Thoughts

Think of each list as a conveyor belt delivering numbers in order. You always
take the smaller number from the front of either belt and attach it to the new
list.

---

## 🚀 Solutions

### 1. Two Conveyor Belts

**Approach:**  
Inspect the two lists given. If one of the lists is empty, return the other.
(This will work if **both** are empty as well; we'll just return `None` as a
result, which is what we want.) Make `new_head` the lower of the two `head`
nodes. While there are still nodes in **both** lists, add the lower one as the
`next` of the new list's last node. If at any point one list is empty, just fuse
in the remainder of the non-empty list.

**Complexity:**  
- Time: `O(n + m)`, where `n` is `list1` and `m` is `list2`
- Space: `O(1)`

**Trade-offs:**  
- Simple
- No extra memory required, as we're using existing nodes

---

## 🧪 Tests (edge cases)

- One list empty
- Both lists empty
- Duplicate values in the list(s)

---

## 📌 Reflections & Takeaways

Having a visual analogy helped me avoid common pitfalls (like skipping a node or
not terminating the list). In an interview, having a solid metaphor can anchor
your explanation.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
