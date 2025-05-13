# 🧠 Problem: Group Anagrams

> Given an array of strings `strs`, group all anagrams together into sublists.
> You may return the output in any order.

[View on NeetCode](https://neetcode.io/problems/anagram-groups/)  
[View on LeetCode](https://leetcode.com/problems/group-anagrams/)

---

## ✨ Initial Thoughts

This is the first of the "medium" level challenges in NeetCode Blind75. Of
course, this is an extension of [Problem 2: Valid
Anagram](../02_valid_anagram/README.md).

My first thought is to use a hashmap to group the anagrams together; the key of
each group can be the sorted word, e.g.:
```python
hash = {
  "act": ["act", "cat"],
  "opst": ["stop", "pots", "tops", "spot"],
}
```

---

## 🚀 Solutions

### 1. Hashmap of Sorted Words

**Approach:**  
Create a hash; the keys are the sorted word and the values are each matching
word.

**Complexity:**  
- Time: O(n * k log k), where `n` is the words and `k` is the characters in each
  word
- Space: O(n)

**Trade-offs:**  
- Straightforward
- Uses only one extra data structure

### 2. Character Count

**Approach:**  
Also create a hash, but instead of the keys being the sorted word, use a tuple
key that has the characated count for each letter in the word.

**Complexity:**  
- Time: O(n)
- Space: O(n * k), where `n` is words and `k` is characters in each word

**Tradeoffs:**  
- A bit more abstract
- No sorting required; potentially faster for edge cases with very long words

---

## 🧪 Tests (edge cases)

- empty strings (`["", ""]`)
- empty list (`[]`)
- no anagrams
- single word
- all anagrams

---

## 📌 Reflections & Takeaways

- As I've come to expect, hashmaps are really useful for these kinds of
  operations. They really are useful for grouping.
- The first solution is probably best for most use cases, but the second will
  definitely be better for lists with extremely long words.
- The key to this is a categorizing/grouping the words using a **derived key**.
  Another interesting way (but probably really impractival) would be to assign
  each letter a prime number, and then have the key be the product of the
  letters. This would probably result in integer overflow in longer words,
  though.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
