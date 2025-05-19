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
|-- 01_arrays_hashing/
    |-- 01_contains_duplicate/
        |-- solution.py
        |-- test.py
        |-- README.md
    |-- 02_valid_anagram/
        |-- ...
|-- 02_two_pointers/
    |-- ...
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
make test # or
pytest    # if you have it installed globally
```

This will discover and run all `test.py` files under `src/`.

---

Feel free to follow along or use these as reference solutions. Feedback and
suggestions welcome!

---

## The Problems

- [I. Arrays & Hashing](./src/01_arrays_hashing/)
  - [01. Contains Duplicate](./src/01_arrays_hashing/01_contains_duplicate/README.md)
  - [02. Valid Anagram](./src/01_arrays_hashing/02_valid_anagram/README.md)
  - [03. Two Sum](./src/01_arrays_hashing/03_two_sum/README.md)
  - [04. Group Anagrams](./src/01_arrays_hashing/04_group_anagrams/README.md)
  - [05. Top K Frequency](./src/01_arrays_hashing/05_top_k_frequency/README.md)
  - [06. String Encode &
    Decode](./src/01_arrays_hashing/06_string_encode_decode/README.md)
  - [07. Product Except Self](./src/01_arrays_hashing/07_array_product_except_self/README.md)
  - [08. Longest Consecutive Sequence](./src/01_arrays_hashing/08_longest_consecutive_sequence/README.md)
- [II. Two Pointers](./src/02_two_pointers/)
  - [09. Valid Palindrome](./src/02_two_pointers/08_longest_consecutive_sequence/README.md)
  - [10. Three Sum](./src/02_two_pointers/10_three_sum/README.md)
  - [11. Container With Most Water](./src/02_two_pointers/11_container_with_most_water/README.md)
- [III. Sliding Window](./src/03_sliding_window/)
  - [12. Best Time to Buy and Sell Stock](./src/03_sliding_window/12_best_time_to_buy_and_sell_stock/README.md)
  - [13. Longest Substring Without Repeating Characters](./src/03_sliding_window/13_longest_substring_without_repeating_characters/README.md)
  - [14. Longest Repeating Character Replacement](./src/03_sliding_window/14_longest_repeating_character_replacement/README.md)
  - [15. Minimum Window Substring](./src/03_sliding_window/15_minimum_window_substring/README.md)
- [IV. Stack](./src/04_stack/)
  - [16. Valid Parentheses](./src/04_stack/16_valid_parentheses/README.md)
- [V. Binary Search](./src/05_binary_search/)
  - [17. Find Minimum in Rotated Sorted Array](./src/05_binary_search/17_find_minimum_in_rotated_array/README.md)
  - [18. Search in Rotated Sorted Array](./src/05_binary_search/18_search_in_rotated_sorted_array/README.md)
- [VI. Linked List](./src/06_linked_list/)
  - [19. Reverse Linked List](./src/06_linked_list/19_reverse_linked_list/README.md)
  - [20. Merge Two Sorted Linked Lists](./src/06_linked_list/20_merge_two_sorted_linked_lists/README.md)
  - [21. Linked List Cycle Detection](./src/06_linked_list/21_linked_list_cycle_detection/README.md)
  - [22. Reorder Linked List](./src/06_linked_list/22_reorder_linked_list/README.md)
  - [23. Remove Nth Node From End of List](./src/06_linked_list/23_remove_nth_node_from_end_of_list/README.md)
  - [24. Merge K Sorted Lists](./src/06_linked_list/24_merge_k_sorted_lists/README.md)
- [VII. Trees](./src/07_trees/)
  - [25. Invert Binary Tree](./src/07_trees/25_invert_binary_tree/README.md)

