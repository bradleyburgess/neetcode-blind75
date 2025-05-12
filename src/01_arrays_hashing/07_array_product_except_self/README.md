# 🧠 Problem: Product of Array Except Self

> Given an integer array `nums`, return an array output where `output[i]` is the
> product of all the elements of `nums` except `nums[i]`.

[View on NeetCode](https://neetcode.io/problems/products-of-array-discluding-self/)  
[View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

---

## ✨ Initial Thoughts

My first thought is to get the product of the whole array and then just loop
over the array dividing by `i` each time. Of course we'd have to check for
`nums[i] == 0` so we don't get a Division by Zero error.

There is a follow-up part to the problem:  
> Could you solve it in `O(n)` time without using the division operation?

This seems like an interesting follow-up challenge, and I don't have any
thoughts right off the bat.

---

## 🚀 Solutions

### 1. Product of Entire Array ÷ Self

**Approach:**  
Get the product of the entire array, and then loop over the array, dividing by
self.

**Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

(Time is really `2n`, as we loop through the array once to geth the product, and
then we loop through it again to get the result. But we ignore constants for
**Big O Notation**, so it's `O(n)`.)

**Trade-offs:**  
- Simple
- Need check for `nums[i] == 0` for Division by Zero errors

---

### 2. Prefix and Suffix Products

After thinking about it for a while, it becamse obvious that the product of the
array except for `nums[i]` is the product of everything before `i` times the
product of everything after `i`.

**Approach:**  
Loop through the array twice: once to get the product of all the **prefix**
elements, and once to get the product of all the **suffix** elements.

The loops will multiply the value of the previous `nums` value (to the left for
`prefix` and to the right for `suffix`) by the previous value of the *-fix array
(again, to the left if `prefix`; to the right if `suffix`).

**Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

(Same disclaimer about `2n` as above — this time for both space and time. We're
looping twice — once for prefixes and once for suffixes — and we're creating
arrays for both.)

**Trade-offs:**  
- Not quite as simple as above, however there's no checking for `0`!
- More space required than the Zero Index solution, however you could probably
  get away with one array and updating in-place.

  ---

  ### 3. Prefix and Suffix Optimized

  For the sake of completeness, here is an approach that optimizes the previous
  solution in terms of space.

  **Approach:**  
  Loop through the `nums` array twice. The first time, update the result array
  to be the prefix products. The second time, multiply those values in-place by
  the suffix products.

  **Complexity:**  
- Time: `O(n)`
- Space: `O(n)`

This has the same time complexity and — in Big O Notation — the same space
complexity. However, we are using fully **half** the space, which I think is
worth noting.

**Trade-offs:**  
- Half the space than the previous solution
- More complex, in my book

---

## 🧪 Tests (edge cases)

- Empty list (`[]`)
- Negative numbers
- Zero in one index
- Zero in multiple indices
- All elements identical

---

## 📌 Reflections & Takeaways

- The prefix/suffix solution is really elegant, and highlights that sometimes
  you can trade a little more nuanced logic for less error checking.
- 

---

## 🧮 Code

> See [`array_product_except_self.py`](./array_product_except_self.py)
