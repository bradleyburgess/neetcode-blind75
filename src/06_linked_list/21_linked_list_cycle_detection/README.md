# 🧠 Problem: Linked List Cycle Detection

> Given the beginning of a linked list `head`, return `true` if there is a cycle in
> the linked list. Otherwise, return `false`.
> 
> There is a cycle in a linked list if at least one node in the list can be
> visited again by following the `next` pointer.
> 
> Internally, `index` determines the index of the beginning of the cycle, if it
> exists. The tail node of the list will set its `next` pointer to the
> `index-th` node. If `index = -1`, then the tail node points to `null` and no
> cycle exists.
> 
> Note: `index` is not given to you as a parameter.

[View on NeetCode](https://neetcode.io/problems/linked-list-cycle-detection/)  
[View on LeetCode](https://leetcode.com/problems/linked-list-cycle/)

---

## ✨ Initial Thoughts

It's not made clear whether the values in the nodes are distinct / unique or
not. We'll begin by doing the naive approach, which is to collect memory
references to nodes and check if the current node exists in the set.

---

## 🚀 Solutions

### 1. Brute Force: Set-based memory comparison

**Approach:**  
Create a set to collect memory references / pointers. Iterate over the linked
list. Check if the pointer (`id`) exists in the set. If it does, return `True`.
If we get to the end of the list (ie `node` is `None`), return False.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

**Trade-offs:**  
- Very simple implementation
- However, requires memory

### 2. Fast-Slow Technique (Floyd's Tortoise and Hare)

**Approach:**  
What we really care about is if any two memory references are the same. So
instead of collecting them, we could send to "runners" through the list — one
fast, and one slow. If at any point they have the same memory reference, we for
sure have a loop. This approach is known as [Floyd's Tortoise and Hare
Algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare)

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- Same time complexity, but `O(1)` space complexity, as we're not creating new
  data structures
---

## 🧪 Tests (edge cases)

- Empty list
- One item in the list
- Two items in the list
- Duplicates (only works with Solution 1)

---

## 📌 Reflections & Takeaways

Again we have a problem where knowing the **minimum** requirements can be
beneficial in creating a more optimized / efficient solution. My first instinct
was to collect all the memory references and check the set as we walk through
the list.

However, we don't really need all of the `id`s. What we actually **need** to
know is if any two are the same. If there's a loop, we're bound to have a
situation where the two are the same. And, with the Floyd technique, we might
arrive at that result *faster* than the other approach, as we have one "runner"
going at double the speed.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
