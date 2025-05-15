import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("(", False),
    (")", False),
    ("[", False),
    ("([])", True),
    ("(([]){})", True),
    ("(([]){})[", False),
    ("({[({})]})", True),
    ("({[({})]}})", False),
    ("[({})](]", False),
    ("(((((((((())))))))))", True),
    ("(((((((((()))))))))))", False),
    ("{[()]}{[()]}", True),
    ("{[()]}}", False),
    ("{[{({({({({})})})})}]}", True),
    # With alphanumeric characters
    ("a(b)c", True),
    ("a(b[c]{d}e)f", True),
    ("a(b[c]{d}e)f)", False),
    ("1 + (2 * 3) - {4 / [5 + (6 - 7)]}", True),
    ("[a + b * (c + d)] - e", True),
    ("[a + b * (c + d]) - e", False),
    ("x(y{z}w)v", True),
    ("x(y{z]w)v", False),
    ("(user[input])", True),
    ("(user[input)]", False),
]


methods = [
    ("stack", Solution.valid_parentheses_stack),
    ("stack_optimized", Solution.valid_parentheses_stack_optimized),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("s,expected", test_cases)
def test_solutions(name, fn, s, expected):
    result = fn(s)
    assert result == expected, f"{name} failed for input {s}"
