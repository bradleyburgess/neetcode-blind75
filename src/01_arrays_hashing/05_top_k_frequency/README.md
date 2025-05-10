# 🧠 Problem: Top K Frequent Elements

> Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
> You may return the answer in **any order**.

[View on NeetCode](https://neetcode.io/problems/top-k-elements-in-list/)  
[View on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

---

## ✨ Initial Thoughts

At first glance, this problem is about **counting frequencies** and then
**returning the top `k` values**. By now, I'm immediately seeing a hashmap being
applicable. But we'll need some way to leverage it and sort it. So my first
instinct is to group the `nums` by frequency, and then create a list and sort
them by frequency, and return the top `k`.

But another approach would be to keep a running list of the top `k`, which is
similar to what we did in [**Two Sum**](../03_two_sum/README.md).

---

## 🚀 Solutions

### 1. Hashmap + Full Sort

**Approach:**  
Use a hashmap to count occurrences of each number. Then turn that into a list of
dictionaries, sort by frequency, and return the top `k`.

**Complexity:**  
- Time: `O(n + k' log k')`, where `n` is the length of `nums`, and `k'` is the
  number of unique elements
- Space: `O(k')`

**Trade-offs:**  
- Very simple to implement
- Not optimal if the number of unique elements is large

---

### 2. Hashmap + Min-Heap of Size k

I did a little digging after I got the first solution working, and I came across
**binary heaps**, and the Python implementation of `heapq`. This is a perfect
way to keep a "running list" as I said above.

**Approach:**  
Use a hashmap to count occurrences. Then push `(freq, num)` into a min-heap. If
the heap exceeds `k`, pop the smallest to retain the three biggest. Finally, pop
the heap to get the top `k` in reverse order, ie highest to lowest frequency.

**Complexity:**  
- Time: `O(n + k' log k)`
- Space: `O(k' + k)`

**Trade-offs:**  
- More efficient when `k` is small compared to `k'`
- A bit more complex but scalable for large input

---

### 3. Bucket Sort

**Approach:**  
Use a hashmap to count frequencies. Create a list of buckets where the index
represents the frequency. Traverse the buckets in reverse to gather the top `k`.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n + k')`

**Trade-offs:**  
- Fastest approach in practice
- Space usage can be higher due to the bucket array
- Might feel less intuitive at first

---

## 🧪 Tests (edge cases)

- Empty list (`[]`)
- `k > len(set(nums))`
- All elements identical
- All elements unique
- Multiple elements with the same frequency

---

## 📌 Reflections & Takeaways

- This is a "group and reduce" problem: count things, then extract the top ones.
- Hashmaps are great for counting, and, as I've discovered, min-heaps are a
  go-to pattern when you want to efficiently track the top or bottom `k` of
  something.
- Bucket sort is a great trick to keep in your back pocket — it's fast and
  elegant, especially when frequencies are bounded.
- As always, choose the algorithm based on the shape of the data: if `k` is
  small and `nums` is large, go for the heap; if everything is small, the
  sort-based one is fine. I think any of these should be appropriate for a
  general use.

---

## 🧮 Code

> See [`top_k_frequency.py`](./top_k_frequency.py)
