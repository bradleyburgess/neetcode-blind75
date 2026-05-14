# 🧠 Problem: Valid Parentheses

> You are given a string `s` consisting of the following characters: `'('`,
> `')'`, `'{'`, `'}'`, `'['` and `']'`.
> 
> The input string `s` is valid if and only if:
> 
> - Every open bracket is closed by the same type of close bracket.
> - Open brackets are closed in the correct order.
> - Every close bracket has a corresponding open bracket of the same type.
> 
> Return `true` if s is a valid string, and `false` otherwise.

[View on NeetCode](https://neetcode.io/problems/validate-parentheses/)  
[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)

---

## ✨ Initial Thoughts

This clearly calls for a **stack**, especially since the problem is about
matching nested structures. It doesn't seem too complex at first glance, but
care is needed for edge cases.

---

## 🚀 Solutions

### 1. Stack: Check for matching pairs and empty stack

**Approach:**  
Loop over the string. If the current character is an open parenthesis, add the
type (round, square, or curly) to the stack. If the current character is a close
parenthesis, `try` `pop` from the stack and confirm that they match. Return `true`
if all the pairs match **and** nothing is left on the stack; otherwise `false`.

**Complexity:**  
- Time: `O(n)` (only brackets processed)
- Space: `O(n')` (only brackets)

**Trade-offs:**  
- Uses an `Enum` for clarity, but adds some verbosity  
- `try-except` blocks may feel inelegant, though they safely handle underflows  
- Stack is a natural fit and makes the logic clear


### 2. Stack: Optimized

**Approach:**  
Similar to above but refined. Instead of using an `Enum`, use a hash and instead
of a switch (`match`) compare against the hash.

**Complexity:**  
- Time: `O(n)` (only brackets processed)
- Space: `O(n')` (only brackets)

**Trade-offs:**  
- Simpler and more idiomatic Python  
- Loses explicitness of `Enum`, but still very readable  
- Fewer lines of code with the same logic and performance

---

## 🧪 Tests (edge cases)

- Empty string
- Only one parenthesis (open or closed)
- Only open / closed parentheses
- Out of sequence (e.g. `([)]`)

---

## 📌 Reflections & Takeaways

This problem isn’t algorithmically complex, but it’s a great example of how
elegant and effective a stack can be for parsing and matching problems.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
