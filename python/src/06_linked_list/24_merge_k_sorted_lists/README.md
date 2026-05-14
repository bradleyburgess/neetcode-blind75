# 🧠 Problem: Merge K Sorted Linked Lists

> You are given an array of `k` linked lists `lists`, where each list is sorted
> in ascending order.
> 
> Return the **sorted** linked list that is the result of merging all of the
> individual linked lists.

[View on NeetCode](https://neetcode.io/problems/merge-k-sorted-linked-lists/)  
[View on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## ✨ Initial Thoughts

This is an extension of the [Merge Two Sorted
Lists](../20_merge_two_sorted_linked_lists/) problem. Obviously, not knowing how
many lists there are makes things more tricky, as we have to build more
flexibility in our code. NeetCode says we should aim for `O(n * k)` time
complexity and `O(1)` space complexity.

We could manually handle the node comparisons manually, but that could really
dicey in terms of manual logic. It would, however, give us the desired `O(n *
k)` time. And easier — **and also faster** — approach would be to use a
**Priority Queue** to handle the comparisons.

---

## 🚀 Solutions

### 1. Priority Queue

**Approach:**  
Create a `dummy` node and also a priority queue (the min-heap `heapq` in
Python). Check the `head`s of each of the `k` `lists` and — if they're not null
— add them all to the queue. From here we just pop off the next element of the
queue, add it to the merged list, and replace the popped node with it's `next`,
if it's not `None`. Return `dummy.next`.

**Complexity:**  
- Time: `O(n log k)` (`n` nodes, with each requiring `log k` for handling in the
  queue)
- Space: `O(k)` (max one node per list in the queue at a time)

**Trade-offs:**  
- Extremely simple to implement
- Very robust, requires minimal checking
- Very performant: `O(n log k)` is better than the `O(n * k)` that was asked for

---

## 🧪 Tests (edge cases)

- Empty list(s)
- Single-value list(s)
- Empty `lists`

---

## 📌 Reflections & Takeaways

This is not the first problem for which I've used a **Priority Queue** (`heapq`)
— the first was [Top K
Frequency](../../01_arrays_hashing/05_top_k_frequency/README.md). However, I
feel that the power of this technique *really* shines in this problem. We could
definitely handle the value comparison manually (and I might come back and add
that solution at some point), but it's just so much easier, quicker, and more
reliable solving this problem using a PQ.

A lot of these problems come down to trade-offs. We're sacrificing a little
space (not much actually — only `(k)`), but we're gaining robustness and
computing performance. That sounds like a win to me.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
