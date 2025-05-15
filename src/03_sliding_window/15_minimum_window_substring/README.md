# 🧠 Problem: Minimum Window Substring

> Given two strings `s` and `t`, return the shortest **substring** of `s` such
> that every character in `t`, including duplicates, is present in the
> substring. If such a substring does not exist, return an empty string `""`.
> 
> You may assume that the correct output is always unique.

[View on NeetCode](https://neetcode.io/problems/minimum-window-with-characters)  
[View on LeetCode](https://leetcode.com/problems/minimum-window-substring/)

---

## ✨ Initial Thoughts

My first thought is that we need to track the characters in each string while
moving the window. We'll need to find the initial character count for `t`, and
then compare that with `s` as we loop over the array.

---

## 🚀 Solutions

### 1. Sliding Window: Brute Force

**Approach:**  
This is going to be ugly, but we'll loop over the array, moving the `right`
pointer. If all the characters of the `t` counter match the `s` counts, we have
a match. Then we can try to move the `left` pointer, constantly checking against
the `t` counter.

**Complexity:**  
- Time: `O(|s| * |s'| * |t|)`, where `n'` is the window
- Space: `O(|t|)`

**Trade-offs:**  
- Simple
- Very inefficient, because we're creating a new `Counter` for the `s` window
  *every iteration*, **and** we're looping over the `t` chars every time we move
  a pointer. Ouch!

### 2. Sliding Window: Brute Force, Optimized

**Approach:**  
Similar to above, but instead of creating a new `Counter` for the `s` window
every iteration, we keep one hash map and update it incrementally.

**Complexity:**  
- Time: `O(|s| * |t|)`
- Space: `O(|s| + |t|)`

**Trade-offs:**  
- Better performance than the simple brute force solution
- Still a lot of duplication

### 3. Sliding Window: Have vs Need

**Approach:**  
What we really care about is if all the requirements have been met, not about
checking all the required characters every time. So let's have a `need` counter,
which would be the length of `t` (or `Counter.total()`), and also a `have`
counter, which tracks the number of requirements we've met. As we loop over the
array, if the `current` character satisfies the requirement (e.g. we need three
`A`s, and this character gives us the third one), we can increment out `have`
counter. Once we've met the requirements and try to shift our `left` pointer
inward, if shifting it causes us to lose a required character, we decrement
`have`.

**Complexity:**  
- Time: `O(|s|)` (finally!)
- Space: `O(|s| + |t|)` (we can't really get better than this)

**Trade-offs:**  
- Not as obvious a solution, because our first instinct is to monitor every
  character closely
- However, the implementation is arguably *simpler* than the brute force
  solution, because we're not cross-examining each character every time — only
  the current character at hand
- **Much** more efficient than either of the other solutions

---

## 🧪 Tests (edge cases)

- Empty `s` and/or `t`
- Only one character in `s` and/or `t`
- `|t|` > `|s|`
- No valid results

---

## 📌 Reflections & Takeaways

This problem was a masterclass in **clearly defining** what you *actually* care
about. Our first instinct is to check that every character is satisfied on every
iteration. However, this isn't *actually* needed. What we care about is that
*all* of the requirements are met, and we can do so incrementally. As we adjust
the `right` pointer, we can make necessary updates to our counters, and — once
we've got a match — we can do the same for the `left` pointer.

The bottom line: Be precise about what the requirements *actually* are. You
can avoid a lot of duplication if you do!

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
