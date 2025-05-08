# 🧠 Problem: Contains Duplicate

> Return true if any value appears at least twice in the array.

[View on NeetCode](https://neetcode.io/problems/duplicate-integer/)  
[View on LeetCode](https://leetcode.com/problems/contains-duplicate/)

---

## ✨ Initial Thoughts

Duplicates are a red flag for brute force, but with better space–time trade-offs
we can find faster solutions using hashing or sorting. Sets give us
constant-time lookups, and sorted arrays give us predictable neighbors.

---

## 🚀 Solutions

### 1. Brute Force / Naive Approach

**Approach:**  
Check every pair in a nested loop. If any pair is equal, return true.

**Complexity:**  
- Time: O(n²)  
- Space: O(1)

**Trade-offs:**  
- Easy to write and understand
- Very inefficient for large arrays

### 2. Hashmap

**Approach:**  
Store each item in a hashmap (dict). If it's already there, it's a duplicate.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

**Trade-offs:**  
- Very fast
- Extra memory usage

### 3. Sort and Compare

**Approach:**  
Sort the array and compare each item to its neighbor.

**Complexity:**  
- Time: O(n log n)  
- Space: O(1) (or O(n) depending on sorting algorithm)

**Trade-offs:**  
- Slightly slower than hashmap
- Avoids extra data structures

---

## 🧪 Tests (edge cases)

Edge cases include:
- Empty array
- Single element
- All elements identical
- No duplicates at all

---

## 📌 Reflections & Takeaways

- Hash-based solutions often give the best time complexity for lookup problems.
- Sorting is a reliable fallback if space is a constraint or hash use isn't ideal.
- Writing multiple approaches clarified trade-offs in readability vs performance.

---

## 🧮 Code

> See [`contains_duplicate.py`](./contains_duplicate.py)