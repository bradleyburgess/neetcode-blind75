import re


class Solution:
    @staticmethod
    def valid_palindrome_two_pointer(s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    @staticmethod
    def valid_palindrome_reverse(s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum()]
        return list(s) == list(reversed(s))

    @staticmethod
    def valid_palindrome_two_pointer_optimized(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < len(s) - 1:
                left += 1
            while not s[right].isalnum() and right >= 0:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
