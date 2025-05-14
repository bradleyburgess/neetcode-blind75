from collections import deque


class Solution:
    @staticmethod
    def longest_substring_deque_window(s: str) -> int:
        n = len(s)
        max_length = 0
        substring = deque()
        for i in range(n):
            if s[i] not in substring:
                substring.append(s[i])
            else:
                max_length = max(max_length, len(substring))
                while s[i] in substring:
                    substring.popleft()
                substring.append(s[i])
        return max(max_length, len(substring))

    @staticmethod
    def longest_substring_hash_window(s: str) -> int:
        char_index = dict()
        left = 0
        max_length = 0
        for idx, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = idx
            max_length = max(max_length, idx - left + 1)
        return max_length
