import pytest
from group_anagrams import (
    group_anagrams_sorted,
    group_anagrams_char_count,
)


# Helper to normalize output (sort groups and contents)
def normalize(result):
    return sorted([sorted(group) for group in result])


test_cases = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    (
        ["abc", "cab", "bca", "acb", "cba", "bac"],
        [["abc", "acb", "bac", "bca", "cab", "cba"]],
    ),
    (["one", "two", "three"], [["one"], ["three"], ["two"]]),
    ([""], [[""]]),
    ([], []),
    (["a"], [["a"]]),
    (["", "", "a", "a", "b"], [["", ""], ["a", "a"], ["b"]]),
]

methods = [
    ("sorted", group_anagrams_sorted),
    ("char_count", group_anagrams_char_count),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("input_strs,expected", test_cases)
def test_solutions(name, fn, input_strs, expected):
    result = fn(input_strs)
    assert normalize(result) == normalize(
        expected
    ), f"{name} failed for input {input_strs}"
