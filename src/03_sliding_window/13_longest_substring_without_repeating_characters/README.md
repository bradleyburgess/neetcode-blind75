# 🧠 Problem: Longest Substring Without Repeating Characters

> Given a string `s`, find the *length of the longest substring* without duplicate
> characters.
> 
> A **substring** is a contiguous sequence of characters within a string.

[View on NeetCode](https://neetcode.io/problems/longest-substring-without-duplicates/)  
[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## ✨ Initial Thoughts

I usually start with a brute force / naive solution to these problems. However,
I actually couldn't really come up with one in the vein of a simple nested loop
/ `O(n²)` approach. The first solution I thought of is — not unexpectedly, given
the problem category — a **sliding window** solution. One can probably argue
over minutiae about implementation, but I think the basic approach remains the
same.

---

## 🚀 Solutions

### 1. Sliding Window: Deque-based

**Approach:**  
Loop over the string. Keep track of the current `substring` and the `max_length`
of `substring` that we've found. If the current character is not in the
substring, add it. If it is in the substring, `pop` the first character off the
`substring` until the current character is not in the `substring`, then add the
current character. Return the maximum value found.

**Complexity:**  
- Time: `O(n)`-ish (see below)
- Space: `O(n)` (max)

**Trade-offs:**  
- Not really complex logically once you understand **sliding window**.
- Not a lot of space required; maximum of `O(n)`, but that assumes no repeating
  characters at all.
- `in` is not as performant for `deque` as it is for other data structures
  (`O(n)`, for `n` items in the `deque`)

### 2. Sliding Window: Hash-based

**Approach:**  
Create a hash table / dict where `key = character` and `value = index`. Loop
over the array. If the current character is in the hash, update the index of the
character, set the new `left`-most edge of the substring to that `index + 1`,
and update the `max_length` if needed. Return the `max_length`.

**Complexity:**  
- Time: `O(n)` (true)
- Space: `O(n')` (unique characters in the string)

---

## 🧪 Tests (edge cases)

- Empty string
- Only one character
- All the same character
- All unique characters

---

## 📌 Reflections & Takeaways

- This was the first NeetCode problem I've done using the `deque` collection
  type. It's perfect for this, because you can `pop` from the start or the end
  (ie both Stack and Queue); obviously for this I needed from the start
  (`popleft`).
- My first instinct (and the approach I took) was to do this problem from left
  to right, but you could just as easily do it from right to left.
- After some research, I found that `in` lookups for `deque` are `O(n)` for `n`
  items in the `deque`, while `in` lookups for `dict`s are `O(1)`. So the
  hash-based approach will be more performant, especially with long strings.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
