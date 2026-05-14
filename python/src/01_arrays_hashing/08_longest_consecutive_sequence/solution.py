from typing import List


class Solution:
    @staticmethod
    def longest_consecutive_brute(nums: List[int]) -> int:
        longest = 0
        lookup = set()
        for num in nums:
            chain_start = num
            chain_end = num
            lookup.add(num)
            while chain_start - 1 in lookup:
                chain_start -= 1
            while chain_end + 1 in lookup:
                chain_end += 1
            _longest = chain_end - chain_start + 1
            if _longest > longest:
                longest = _longest
        return longest

    @staticmethod
    def longest_consecutive_chain_start(nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                length = 1
                while current + 1 in nums_set:
                    length += 1
                    current += 1
                longest = max(longest, length)
        return longest
