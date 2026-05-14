# 🧠 Problem: Longest Consecutive Sequence

> Given an array of integers `nums`, return the length of the longest
> consecutive sequence of elements that can be formed. A consecutive sequence is
> a sequence of elements in which each element is exactly `1` greater than the
> previous element. The elements do *not* have to be consecutive in the original
> array. You must write an algorithm that runs in `O(n)` time.

[View on NeetCode](https://neetcode.io/problems/longest-consecutive-sequence/)  
[View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)

---

## ✨ Initial Thoughts

I know off the bat we're going to need a hashmap of some sort. We'll need to
loop over the array and check for neighbouring values. E.g.: "Current `num` is
`3`; is there a `2` and/or a `4`?"

The tricky part is going to be doing it in `O(n)` time as per the requirement.

---

## 🚀 Solutions

### 1. Brute Force

**Approach:**  
Just to get started, let's brute force our way through it. We'll create a hash
table and then loop over the array: For every element, we'll see how far down
and how far up we can go in a chain, and keep track of the longest chain.

**Complexity:**  
- Time: `O(n²)` probably at worst
- Space: `O(n)`

**Trade-offs:**  
- Simple
- Inelegant and slooooow, as we're checking each element and going up and down
  for each.

---

### 2. Set with chain starts

After thinking about this for a minute, you realize that you really don't have
to check every element in the collection: You can get away with only worrying
about numbers that are the start of a chain.

**Approach:**  
Create a set or hash table. Loop over the array: If the number is not the start
of a chain (i.e. if `num - 1` is not in the set), `continue`. If it is the
start, see how far up you can go.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

**Trade-offs:**  
- Much faster
- Not actually that much more complex, once you realize you can check for the
  start of the chain basically for free.

  ---

  ## 🧪 Tests (edge cases)

- Empty list (`[]`)
- Negative numbers
- Multiple chains of the same length
- No chains

---

## 📌 Reflections & Takeaways

- It's good to start with a naive / brute force solution to establish a
  baseline. However, very often, there is a much more efficient solution that
  isn't actually that much more complex.
- Sets are **powerful** when you need them. 

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
