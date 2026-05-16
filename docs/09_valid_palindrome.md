# 🧠 Problem: Valid Palindrome

> Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.
> Only consider alphabetic characters, and ignore casing.

[View on NeetCode](https://neetcode.io/problems/is-palindrome/)  
[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)

---

## ✨ Initial Thoughts

There aren't a whole lot of different ways to approach this. We need to check if
a (cleaned) string is the same forwards and backwards. We can check it manually,
or by using a built-in like `reversed`.

---

## 🚀 Solutions

### 1. Two-Pointer With Preprocessing (Manual)

**Approach:**  
Use a regular expression or similar device to remove non-alphabetic characters
and lowercase the string. Then use two pointers from both ends inward to compare
characters, stopping before the pointers cross each other.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

**Trade-offs:**  
- Straightforward and readable.
- Memory usage could be reduced if we avoid preprocessing.

---

### 2. Reverse

**Approach:**  
Clean up the string, then compare it with its reverse.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

**Trade-offs:**  
- Cleanest and most concise solution.
- Still allocates memory for both the cleaned list and its reverse.

---

### 3. Two-Pointer Optimized (No Preprocessing)

**Approach:**  
Use two pointers directly on the raw string. Skip non-alphabetic characters
while traversing, and compare lowercase letters on the fly.

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- Most memory-efficient.
- Slightly more complex logic.

---

## 🧪 Tests (edge cases)

- Empty string `""`
- Only non-alphabetic characters `".,"`
- Palindromes with punctuation and spaces
- Case sensitivity
- Non-palindromes like `"hello"`

---

## 📌 Reflections & Takeaways

- Two-pointer techniques are great for problems that require symmetric
  comparisons.
- Regex makes string preprocessing very expressive in Python, but it’s worth
  considering memory trade-offs.
- Sometimes avoiding preprocessing gives you both performance and elegance — if
  you're willing to write slightly more complex logic.

---

## 🧮 Code

> See [`solution.py`](../python/src/09_valid_palindrome/solution.py) and [`test.py`](../python/src/09_valid_palindrome/test.py)
