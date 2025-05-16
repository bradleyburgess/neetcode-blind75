# 🧠 Problem: Find Minimum in Rotated Sorted Array

> You are given an array of length `n` which was originally sorted in ascending
> order. It has now been rotated between `1` and `n` times. For example, the
> array `nums = [1,2,3,4,5,6]` might become:
> 
> - `[3,4,5,6,1,2]` if it was rotated `4` times.
> - `[1,2,3,4,5,6]` if it was rotated `6` times.
> 
> Assuming all elements in the rotated sorted array nums are unique, return the
> minimum element of this array.
> 
> A solution that runs in `O(n)` time is trivial, can you write an algorithm
> that runs in `O(log n)` time?

[View on NeetCode](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/)  
[View on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

## ✨ Initial Thoughts

The first thought that came to mind was a **binary search**. This is because we
are told that the array is **sorted**. A binary search involved going to the
mid-point between `left` and `right` pointers and comparing the value to your
search. In a traditional binary search, we know the value we're looking for.
However, in this case, we don't know the exact value, so we'll need to make some
chances to the logic.

---

## 🚀 Solutions

### 1. Verbose: Left and Right directions

**Approach:**  
We're trying to find the divide: the point in the array where `nums[i] > nums[i
+ 1]`. We'll keep asking, "Which direction should I go?" If I'm going right and the
+ current position is *greater* than `left`, we keep going right; if it's *less*
  than `left`, we need to double back, so we change the direction to `left`. The
  opposite applies for if the direction was `right`. We'll keep comparing the
  current value against the minimum, and we'll stop if the next index is the
  same as where we currently are.

**Complexity:**  
- Time: `O(log n)`
- Space: `O(1)`

**Trade-offs:**  
- This is very *simple* but it's also very *verbose*
- We're keeping track of several values manually: `left`, `right`, `direction`, and `min_val`

### 2. True Binary Search

**Approach:**  
The actual result of this approach will be very similar to the above, but the
logic and implementation will be much simpler. We start with `left` at `0` and
`right` as the last index of the array. Go to the mid-point. If it's *greater*
than the `left` pointer, we are in the "left" portion of the array (the rotated
portion); if it's *less* than the `left` pointer, we're in the "right" portion
of the array (original, sorted portion). If left, go to the mid-point of the
right half of our current position (`mid + 1`); if right, go to the left half of
our current position (`mid - 1`). Compare the `min` values, and keep going until
the `left` pointer crosses the `right` pointer and the search is no longer
valid.

**Complexity:**  
- Time: `O(log n)`
- Space: `O(1)`

**Trade-offs:**  
- Same performance as above
- But much less "in the weeds" with manually dictating `direction`
- Much more elegant and conceptually simpler

---

## 🧪 Tests (edge cases)

- One value in the array
- Min value at the start (ie not rotated or fully rotated)
- Min value at the end (rotated `n - 1` times)
- Min value somewhere in the middle

---

## 📌 Reflections & Takeaways

**Binary Search** is powerful and elegant. The "brute force" approach for this
would give you `O(n)` time — quite performant by all measures — but Binary
Search gives you a much more efficient `O(log n)`.

Instead of trying to find an actual value, we were trying to find the "divide"
in the array — the point between the the first index and the last index in the
original array.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
