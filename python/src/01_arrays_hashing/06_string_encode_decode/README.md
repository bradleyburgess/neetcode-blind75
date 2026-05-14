# 🧠 Problem: Encode and Decode Strings

> Design an algorithm to encode a list of strings to a single string. The
> encoded string is then decoded back to the original list of strings. Please
> implement `encode` and `decode`.

[View on NeetCode](https://neetcode.io/problems/string-encode-and-decode/)  
[View on LeetCode](https://leetcode.com/problems/encode-and-decode-strings/)

---

## ✨ Initial Thoughts

My initial thought is that this problem has already been "solved" by formats
like JSON, which safely encode and decode structured data. However, in an
interview setting, using a built-in like `json.dumps()` may be considered
cheating or may avoid the key part of the challenge: designing your own
encoding scheme.

The main challenge in implementing a custom solution is designing a format that:
- allows for arbitrary characters (including delimiters) within strings,
- can be unambiguously decoded,
- and is efficient to parse.

---

## 🚀 Solutions

### 1. JSON

**Approach:**  
Simply serialize the list to a string using `json.dumps()` and decode using
`json.loads()`.

**Complexity:**  
- Time: `O(n)`, where `n` is the total number of characters across all strings
- Space: `O(n)`

**Trade-offs:**  
- ✅ Extremely easy to implement and reliable  
- ❌ Some interviewers may expect a manual solution  
- ❌ Slight overhead due to JSON escaping and formatting

---

### 2. Length-Prefixed Encoding

**Approach:**  
Use a hand-rolled encoding scheme: prefix each string with its length followed
by a special character (e.g. `#` but could be anything, really), then append the
string itself. This ensures that we know exactly how many characters to read
after each delimiter.

**Example:**
```text
["hello", "world"] => "5#hello5#world"
["", ""] => "0#0#"
```

To decode:  
- Read digits until # to get the length.
- Read that many characters to get the string.
- Repeat.

**Complexity:**  
- Time: O(n)
- Space: O(n)
- Where n is the total length of all strings combined.

**Trade-offs:**  
- ✅ Handles all characters, including #
- ✅ Fast and efficient
- ✅ No need to escape characters
- ✅ Interviewer-friendly manual implementation
- ❌ Slightly more code to write and parse

---

## 🧪 Tests (edge cases)
- Empty strings and empty lists
- Strings with special characters and symbols
- Very long and very short strings
- Strings containing potential delimiters
- Strings with spaces

---

## 📌 Reflections & Takeaways
- This problem is a great example of how to design reversible transformations.
- Avoiding delimiter collisions is crucial — length-prefixing is an elegant
  solution, although I'm sure there are others.
- JSON is acceptable in many real-world use cases, but for interviews, being
  able to design a scheme from scratch shows a deeper understanding.
- I learned to think carefully about how to unambiguously parse data — a common
  real-world concern when dealing with serialization formats.

---

## 🧮 Code

> See [`solution.py`](./solution.py) and [`test.py`](./test.py)
