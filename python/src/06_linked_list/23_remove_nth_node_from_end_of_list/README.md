# 🧠 Problem: Remove Nth Node From End of List

> You are given the beginning of a linked list `head`, and an integer `n`.
> 
> Remove the `nth` node from the end of the list and return the beginning of the
> list.

[View on NeetCode](https://neetcode.io/problems/remove-node-from-end-of-linked-list/)  
[View on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## ✨ Initial Thoughts

The obvious approach is to first find the length of the list and then work our
way towards the `nth + 1` node from the end, and wire `node.next` to be
`node.next.next`, skipping the node to be removed. This is still a linear
complexity, but we can probably find a way to avoid the first pass to discover
the length.

---

## 🚀 Solutions

### 1. Two Passes

**Approach:**  
First find the length of the list. Calculate the "index" of the node to be
removed, traverse the list to that point, and remove it.

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- Very simple approach
- Good performance, but with two passes, it's technically `O(2n)` for two loops.

### 2. One Pass Using Floyd

**Approach:**  
Using Floyd's Tortoise and Hare approach, send the `fast` pointer through the
list until it has traveled `n` nodes. Then send the `slow` and `fast` nodes
together (both 1x speed), and travel until `fast` has reached the end of the
list.

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- Same time complexity, but avoids needing a second pass

### 3. One Pass: Simplified with Dummy Node

**Approach:**  
Same approach as [#2](#2-one-pass-using-floyd), but use a Dummy node to simplify
for cases where we're removing the `head` node.

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- Less manual checking than [#2](#2-one-pass-using-floyd)

---

## 🧪 Tests (edge cases)

- Empty list
- One item in the list
- Removing head
- Removing tail

---

## 📌 Reflections & Takeaways

I had seen the dummy node trick before, but haven't used it until now. I now
know why it's such a great tool, especially for Linked List problems. You can
avoid edge cases and manual checking involving the `head` node very easily!

Floyd continues to shine. I'm seeing that it's one of the most "bang for your
buck" techniques when it comes to Linked List problems.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
