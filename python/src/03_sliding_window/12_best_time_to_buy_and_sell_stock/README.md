# 🧠 Problem: Best Time to Buy and Sell Stock (Crypto)

> You are given an integer array `prices` where `prices[i]` is the price of NeetCoin
> on the <em>i<sup>th</sup></em> day.
> 
> You may choose a **single day** to buy one NeetCoin and choose a **different
> day in the future to sell it**.
> 
> Return the maximum profit you can achieve. You may choose to not make any
> transactions, in which case the profit would be `0`.

[View on NeetCode](https://neetcode.io/problems/buy-and-sell-crypto/)  
[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## ✨ Initial Thoughts

This is the first of the **Sliding Window** problems. I deliberately haven't
looked into what that approach entails; I want to see if I can figure that out
unassisted.

I'll brute force it initially, and then work through what the core of the
problem is in optimizing the solution.

---

## 🚀 Solutions

### 1. Brute Force

**Approach:**  
Loop over the array twice, comparing every buy price (`i`) with every sell price
(`j`), where `j` > `i`.

**Complexity:**  
- Time: `O(n²)`
- Space: `O(1)`

**Trade-offs:**  
- Very simple
- Inelegant and will waste a lot of time

---

### 2. One Pass, Left to Right

**Approach:**  
I don't know if this is the "Sliding Window" technique, but essentially what my
thinking is behind this approach is to (a) work left to right, (b) keeping track
of the `max_profit` as well as the `min_buy` price, and always comparing the
tracked `max_profit` with the profit by selling at the current price compared to
the current `min_buy` price.

**Complexity:**  
- Time: `O(n)`
- Space: `O(1)`

**Trade-offs:**  
- Not actually that complex once you realize this is a problem that always
  involves comparing values to the left of the curret pointer
- Way faster than a nested loop

---

## 🧪 Tests (edge cases)

- Prices decrease; no profit
- Only one price; no transaction
- Empty list
- All the same price; no profit

---

## 📌 Reflections & Takeaways

According to [GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/):

> Sliding Window problems involve moving a fixed or variable-size window through
> a data structure, typically an array or string, to solve problems efficiently
> based on continuous subsets of elements. This technique is used when we need
> to find subarrays or substrings according to a given set of conditions.

So it would appear that my instincts were spot on for how to effectively solve
this problem!

This is a very elegant way to solve a problem. You get many of the benefits of
the simplicity of the nested loop approach, but with the efficiency of linear
time. That's a big win.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
