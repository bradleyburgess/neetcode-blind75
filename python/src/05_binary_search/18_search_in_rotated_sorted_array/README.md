# 🧠 Problem: Search in Rotated Sorted Array

> You are given an array of length `n` which was originally sorted in ascending
> order. It has now been rotated between `1` and `n` times. For example, the
> array `nums = [1,2,3,4,5,6]` might become:
> 
> - `[3,4,5,6,1,2]` if it was rotated 4 times.
> - `[1,2,3,4,5,6]` if it was rotated 6 times.
> 
> Given the rotated sorted array `nums` and an integer `target`, return the
> index of `target` within `nums`, or `-1` if it is not present.
> 
> You may assume all elements in the sorted rotated array nums are **unique**,
> 
> A solution that runs in `O(n)` time is trivial, can you write an algorithm
> that runs in `O(log n)` time?

[View on NeetCode](https://neetcode.io/problems/find-target-in-rotated-sorted-array)  
[View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

## ✨ Initial Thoughts

Clearly this is going to be similar in many ways to the [previous
problem](../17_find_minimum_in_rotated_array/). The key is going to be in
determining the logic of whether to go `right` or `left` from the `mid` — that
will be different to the **Find Minimum** problem.

---

## 🚀 Solutions

### 1. Binary Search with Tweaked Logic

**Approach:**  
We'll take a similar approach to the [Binary Search
approach](../17_find_minimum_in_rotated_array/README.md#2-true-binary-search) of
the previous problem, however, with some adjusted logic. First we'll determine
if the "break" is to the left or right of us: if the `left` pointer is less than
`mid`, then it's to the right; otherwise it's to the left. If we're in the left
portion (ie before the break), we'll go left if the `target` is between `left`
and `mid`, otherwise we'll go right. If we're in the right portion (ie after the
break), we'll go left if `target` is either about `left` or below `mid`;
otherwise we'll go right. At every point we'll check if `mid` matches `target`.
If we get to the end of the loop and we've not returned a value, we'll return
`-1`, indicating that `target` was not found.

**Complexity:**  
- Time: `O(log n)`
- Space: `O(1)`

**Trade-offs:**  
- Elegant
- Very simple "binary" logic — it's either to the right or to the left (or we're
  on it!)

---

## 🧪 Tests (edge cases)

- One value in the array
- No rotation / fully rotated
- Target not in the array
- Target before the break
- Target after the break
- Target at the very beginning or the very end

---

## 📌 Reflections & Takeaways

**Binary Search** once again shows its power under the right cirsumstances;
namely a sorted array, with or without a rotation.

This problem can seem complex at first, but once you nail down the 2-part logic,
it then appears quite simple.

1. Determine if `mid` is in the "left" (before the break) or "right" (after the
   break) portion.
2. Decide whether to go right or left, based on the answer to (1.) and how the
   value of `target` relates to `nums[left]` and `nums[mid]`.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
