# 🧠 Problem: Longest Repeating Character Replacement

> You are given a string `s` consisting of only uppercase english characters and
> an integer `k`. You can choose up to `k` characters of the string and replace
> them
> with any other uppercase English character.
> 
> After performing at most `k` replacements, return the length of the longest
> substring which contains only one distinct character.

[View on NeetCode](https://neetcode.io/problems/longest-repeating-substring-with-replacement/)  
[View on LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## ✨ Initial Thoughts

On first glance, this problem doesn't seem that different from [the previous
one](../13_longest_substring_without_repeating_characters/). However, I had to
think about it for a while! The crux here lies in keeping track of the most
frequent character in the givven window, and then working out the logic for how
to adjust the window.

---

## 🚀 Solutions

### 1. Sliding Window: Continuous Max Frequency Character

**Approach:**  
Keep a `char_count` hash where you keep track of the frequency of each character
in the window. Start at `0` for both the `left` and `right` parts of the window.
Loop through the array, expanding the `right` edge on every iteration. Check if
the windows size minus the max character frequency is greater than `k`, and move
the left pointer if it is, and decrementing the left pointer's character count.

**Complexity:**  
- Time: `O(n)` (actually `O(26n)`, but simplifies to this)
- Space: `O(n')` (unique characters in the string)

**Trade-offs:**  
- Technically `O(n)`, but it depends on the number of unique characters
- Fairly simple logic, that doesn't require much interms of accounting for edge cases

### 2. Sliding Window: Only track `max_freq`

**Approach:**  
In the previous solution, we constantly checked to find the character with the
highest frequency in the given window. This requires iterating over `char_count`
every iteration of the `s` loop. However, we only care about the **maximum**
count. This means that we don't necessarily care about the accuracy of the
current window; we only care about updating the `max_freq` character, as this is
what ultimately determines our result. (`max_length` gets updated, and `k` is
constant.) Therefore we can only check if the current character (ie at
`s[right]`) is higher than the currently-tracked `max_freq` character, and
update it if needed. Ultimately this also boils down to `O(n)` like the previous
solution, but it will absolutely be faster, because we're not iterating over
`char_count` each time.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n')` (unique characters in the string)

## 🧪 Tests (edge cases)

- Empty string
- Only one character
- All the same character
- All unique characters
- Extremes of the array

---

## 📌 Reflections & Takeaways

- This problem got me to the "aha" moment of **Sliding Window**: Sliding Window
  is about finding **what** to track, and working out **how** and **when** to
  adjust the window. In this example, it was realizing that the logic boilined
  down to: if `window size` minus `max_freq` character is less than or equal to
  `k`, keep the `left` pointer where it is; otherwise, move it to the right.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
