# 🧠 Problem: Three Sum

> Given an integer array `nums`, return all the triplets `[nums[i], nums[j],
> nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j`
> and `k` are all distinct. The output should *not* contain any duplicate
> triplets. You may return the output and the triplets in any order.

[View on NeetCode](https://neetcode.io/problems/three-integer-sum/)  
[View on LeetCode](https://leetcode.com/problems/3sum/)

---

## ✨ Initial Thoughts

Of course this is an extension of [**Two
Sum**](../../01_arrays_hashing/03_two_sum/). As I normally, I'm going to start
with a brute force method and just loop through the array three times.

A better approach would be — as the category would suggest — to use a **two
pointer** method.

---

## 🚀 Solutions

### 1. Brute Force

**Approach:**  
Loop over the list three times, looking for the sum of zero. We'll need to check
for duplicates, and — because the array isn't necessarily sorted — we'll have to
do that manually. It'll be an ugly mess for sure.

**Complexity:**  
- Time: `O(n³)` (Yowzer!)
- Space: `O(n)`

**Trade-offs:**  
- Simple in theory, but not actually that simple in practice, because of the
  duplicate checking and the fact that it's a *doubly* nested loop.

---

### 2. Two Pointer

**Approach:**  
First, sort the list. Then fix the first item of the triplet (`i`) and use the
two-pointer method to find a `j` and `k` that give us the correct sum. If the
sum is too big, move the left pointer right; if it's too small, move the right
pointer left. When a match is found, skip over the duplicates.

**Complexity:**  
- Time: `O(n²)`
- Space: `O(n)`

**Trade-offs:**  
- A little more complex high-level logic, but in practice possibly simpler than
  the brute force method!
- Sorting the array first means we can guarantee no duplicate triplets.

---

## 🧪 Tests (edge cases)

- Empty list
- All elements the same value
- No valid results
- Duplicate triplets
- Fewer than three elements
- Triplets at both ends of the list

---

## 📌 Reflections & Takeaways

- The two-pointer method is really powerful and can *seriously* cut down the
  time complexity.
- Sorting can add a little computational time, but it often can drastically
  reduce algorithmic logic in duplicate checking.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
