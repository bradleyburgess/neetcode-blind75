import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("racecar", True),
    ("No lemon, no melon", True),
    ("Was it a car or a cat I saw?", True),
    ("hello", False),
    ("", True),
    (" ", True),
    (".,", True),
    ("Able was I ere I saw Elba", True),
    ("Madam In Eden, I’m Adam", True),
    ("Red rum, sir, is murder", True),
    ("Eva, can I see bees in a cave?", True),
    ("12321", True),
    ("1231", False),
    ("0P", False),
]


methods = [
    ("two_pointer", Solution.valid_palindrome_two_pointer),
    ("reverse", Solution.valid_palindrome_reverse),
    ("two_pointer_optimized", Solution.valid_palindrome_two_pointer_optimized),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("s,expected", test_cases)
def test_solution(name, fn, s, expected):
    result = fn(s)
    assert result == expected, f"{name} failed for input {s}"
