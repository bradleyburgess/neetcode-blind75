# 🧠 Problem: Container With Most Water

> You are given an integer array `heights` where `heights[i]` represents the
> height of the <em>i<sup>th</sup></em> bar. 
>
> You may choose any two bars to form
> a container. Return the *maximum* amount of water a container can store.

[View on NeetCode](https://neetcode.io/problems/max-water-container/)  
[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)

---

## ✨ Initial Thoughts

This is an interesting challenge! Essenially we're trying to find the maximum 2D
area possible given the heights of the bars (Y) and the width between them (X).

I'll start with the brute force method where we check every possible combination
of two bars.

But the more elegant solution will probably involve **two pointers** (again, the
category name gives it away). The trick here will be deciding how to move the
pointers.

---

## 🚀 Solutions

### 1. Brute Force

**Approach:**  
Loop over the list twice times. Check the area of every combination of bars (min
height * difference in indexes).

**Complexity:**  
- Time: `O(n²)`
- Space: `O(1)`

**Trade-offs:**  
- Dead simple
- Inelegant and will waste a lot of time

---

### 2. Two Pointer

**Approach:**  
Start at opposite ends of the array. Move the pointer with the lower height
inward; if they're the same, you could move either one or move the one that is
going up if you move it. To keep it simple, I'll just pick one to move, reducing
the if-else logic.

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- More complex logic
- Way faster

---

## 🧪 Tests (edge cases)

- Decreasing / increasing heights
- Plateaus
- Peaks in the middle
- Only one bar

---

## 📌 Reflections & Takeaways

- The two-pointer method really shines in this kind of problem, and drastically
  cuts down computating time.
- This is the last of the **Two Pointer** problems, but I'm going to continue to
  look out for applications of it in the furture.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
