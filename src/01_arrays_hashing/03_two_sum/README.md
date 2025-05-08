# 🧠 Problem: Two Sum

> Given an array of integers `nums` and an integer `target`, return the indices
> `i` and `j` such that `nums[i] + nums[j] == target` and i `!= j`.

The problem has the constraint that there is only one valid pair of numbers per
list of `nums`.

[View on NeetCode](https://neetcode.io/problems/two-integer-sum/)  
[View on LeetCode](https://leetcode.com/problems/two-sum/)

---

## ✨ Initial Thoughts

The obvious, brute force / naive approach is to loop through `nums` twice —
similar to the Contains Duplicate problem. But once again, I know hashmaps are
going to be a better approach. I also know that the unique solution constraint
is going to be a huge help, as we can probably eliminate a lot of edge cases.

---

## 🚀 Solutions

### 1. Brute Force / Naive

**Approach:**  
Loop through the list twice, checking each pair.

**Complexity:**  
- Time: O(n²)
- Space: O(1)

**Trade-offs:**  
- Straightforward
- Very inefficient

### 2. Hash Map

**Approach:**  
Make a hash map for every item in the list of `value: index`. Check if the
complement exists in the hashmap.

**Complexity:**  
- Time: O(n)
- Space: O(n)

**Trade-offs:**  
- Much better performance time-wise
- Uses more than `n` space (creates a dictionary)
- A little more complex logically

---

## 🧪 Tests (edge cases)

- negative numbers
- negative target
- duplicate values (e.g. `[5, 5]`)

---

## 📌 Reflections & Takeaways

My original hashmap solution created the hashmap with values and *then* looped
through the `nums` list to check for complements. I was concerned that duplicate
values might cause the hashmap to overwrite earlier indices, but this didn't
affect correctness due to how the loop was structured; we start the loop again,
and so the duplicate value (if any) is guaranteed to be the second instance in
the list.

My improved hashmap solution does the checking and adding to the hashmap in one
pass. Basically: get the complement required; if it's in the hashmap, return it
— otherwise add `value: index` to the hashmap and continue the loop.

---

## 🧮 Code

> See [`two_sum.py`](./two_sum.py)
