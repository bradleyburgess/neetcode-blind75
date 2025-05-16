![test](https://github.com/bradleyburgess/neetcode-blind75/actions/workflows/test.yml/badge.svg)


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

---

## The Problems

- [01. Arrays & Hashing](./src/01_arrays_hashing/)
  - [Contains Duplicate](./src/01_arrays_hashing/01_contains_duplicate/)
  - [Valid Anagram](./src/01_arrays_hashing/02_valid_anagram/)
  - [Two Sum](./src/01_arrays_hashing/03_two_sum/)
  - [Group Anagrams](./src/01_arrays_hashing/04_group_anagrams/)
  - [Top K Frequency](./src/01_arrays_hashing/05_top_k_frequency/)
  - [String Encode & Decode](./src/01_arrays_hashing/06_string_encode_decode/)
  - [Product Except Self](./src/01_arrays_hashing/07_array_product_except_self/)
  - [Longest Consecutive Sequence](./src/01_arrays_hashing/08_longest_consecutive_sequence/)
- [02. Two Pointers](./src/02_two_pointers/)
  - [Valid Palindrome](./src/02_two_pointers/08_longest_consecutive_sequence/)
  - [Three Sum](./src/02_two_pointers/10_three_sum/)
  - [Container With Most Water](./src/02_two_pointers/11_container_with_most_water/)
- [03. Sliding Window](./src/03_sliding_window/)
  - [Best Time to Buy and Sell Stock](./src/03_sliding_window/12_best_time_to_buy_and_sell_stock/)
  - [Longest Substring Without Repeating
    Characters](./src/03_sliding_window/13_longest_substring_without_repeating_characters/)
  - [Longest Repeating Character
    Replacement](./src/03_sliding_window/14_longest_repeating_character_replacement/)
  - [Minimum Window Substring](./src/03_sliding_window/15_minimum_window_substring/)
- [04. Stack](./src/04_stack/)
  - [Valid Parentheses](./src/04_stack/16_valid_parentheses/)
- [05. Binary Search](./src/05_binary_search/)
  - [Find Minimum in Rotated Sorted Array](./src/05_binary_search/17_find_minimum_in_rotated_array/)
  - [Search in Rotated Sorted Array](./src/05_binary_search/18_search_in_rotated_sorted_array/)