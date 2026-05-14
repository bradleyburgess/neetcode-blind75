from collections import defaultdict


class Solution:
    @staticmethod
    def longest_repeating_hash_count_window(s: str, k: int) -> int:
        max_length = 0
        left = 0
        char_count = defaultdict(int)
        for right in range(len(s)):
            char_count[s[right]] += 1
            freq_char_count = 0
            for char, count in char_count.items():
                if count > freq_char_count:
                    freq_char_count = count
            while (right - left + 1) - freq_char_count > k:
                char_count[s[left]] -= 1
                left += 1
            max_length = max(max_length, (right - left + 1))
        return max_length

    @staticmethod
    def longest_repeating_max_freq_window(s: str, k: int) -> int:
        max_length = 0
        left = 0
        max_freq = 0
        char_count = defaultdict(int)
        for right in range(len(s)):
            char_count[s[right]] += 1
            if char_count[s[right]] > max_freq:
                max_freq = char_count[s[right]]
            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            max_length = max(max_length, (right - left + 1))
        return max_length
