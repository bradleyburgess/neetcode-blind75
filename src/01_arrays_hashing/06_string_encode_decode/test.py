import pytest
from .solution import Solution


test_cases = [
    ["hello", "world"],
    [""],
    ["", ""],
    ["a", "b", "c"],
    ["abc", "def", "ghi"],
    ["this is a sentence", "with spaces"],
    ["1", "2", "3", "4", "5"],
    ["#", "@", "$", "%", "^", "&"],
    ["[delim]", "[[break]]", "[[[stuff]]]"],
    ["long string " * 100, "short", "tiny"],
    ["#", "with", "\n", "special", "\t", "#", "characters"],
    [],
]

methods = [("json", Solution.Json), ("length_delimited", Solution.LengthDelimited)]


@pytest.mark.parametrize("name,sln", methods)
@pytest.mark.parametrize("strs", test_cases)
def test_solutions(name, sln, strs):
    encoded = sln.encode(strs)
    decoded = sln.decode(encoded)
    assert decoded == strs, f"{name} failed for input {strs}"
