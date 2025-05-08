# 🧠 Problem: Valid Anagram

> Given two strings, determine if they are anagrams of each other.

[View on NeetCode](https://neetcode.io/problems/is-anagram/)  
[View on LeedCode](https://leetcode.com/problems/valid-anagram/description/)

---

## ✨ Initial Thoughts

Anagrams are essentially the same characters in a different order. You can solve
this with sorting or by counting character (e.g. in a hashmap).

The NeetCode problem doesn't mention anything about capitalization and
non-character letters like numbers. However, to make the solutions more robust,
I will "normalize" the inputs in the methods, which will strip out anything
that's not `[a-zA-Z]`.

---

## 🚀 Solutions

### 1. Hashmap (for each string)

**Approach:**  
Count letters in each string using a dictionary. Then compare the dictionaries.

**Complexity:**  
- Time: O(n)
- Space: O(n)

(for each string)

**Trade-offs:**  
- Straightforward
- Uses two dicts

### 2. Optimized Hashmap (single dictionary for both)

**Approach:**  
Use one dictionary and increment for the first string, decrement for the second.
If all values end up as zero, they're anagrams.

**Complexity:**  
- Time: O(n) (for each string)
- Space: O(n) (total)

**Trade-offs:**  
- More memory efficient
- Only slightly more complex logic

### 3. Sort and Compare

**Approach:**  
Sort both strings and compare them.

**Complexity:**  
- Time: O(n log n) (for each string)
- Space: O(n) (for each string)

**Trade-offs:**  
- Easiest to write
- Slower than hashmap

---

## 🧪 Tests (edge cases)

- Unequal lengths
- Same characters, different order
- Punctuation or spaces (if applicable)

---

## 📌 Reflections & Takeaways

- Rewriting the solution to use a single hash structure helped reduce memory
  usage and clarified logic flow.
- Hashmaps remain faster and cleaner than sorting for this kind of comparison
  task.
- Understanding when counts should balance out to zero is a useful
  anagram-checking trick.
---

## 🧮 Code

> See [`valid_anagram.py`](./valid_anagram.py)
