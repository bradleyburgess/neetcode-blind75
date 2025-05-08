# NeetCode Blind 75 Solutions

This repository contains my solutions to the [NeetCode Blind
75](https://neetcode.io/practice) problems. I'm solving them in Python and
documenting my thought process as I go.

Each problem is organized by topic and includes:
- Multiple solution strategies (e.g. brute force, optimized)
- Unit tests
- Writeups for thoughts / takeaways

I'm also publishing selected writeups on my [dev
blog](https://dev.bradley-burgess.com/tags/neetcode/).

## Structure

Structure is:
```
./src/
    01_arrays_hashing/
        01_contains_duplicate/
            contains_duplicate.py
            contains_duplicate_test.py
            README.md
        02_valid_anagram/
        ...
```

## Goals

- Practice data structures and algorithms in a structured, consistent way
- Build clear, tested, and well-documented solutions
- Explore trade-offs in different approaches

## Languages

The solution are only in Python right now, but I might do them in a second,
lower-level language at some point.

## Running the tests

Make sure you have [pytest](https://docs.pytest.org/) installed. Then from the
root of the repository, run:

```bash
pytest
```

This will discover and run all `*_test.py` files under `src/`.

---

Feel free to follow along or use these as reference solutions. Feedback and
suggestions welcome!
