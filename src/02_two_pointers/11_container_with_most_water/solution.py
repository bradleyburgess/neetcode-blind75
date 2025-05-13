from typing import List


class Solution:
    @staticmethod
    def container_most_water_brute(heights: List[int]) -> List[List[int]]:
        n = len(heights)
        max_area = 0
        for left in range(n - 1):
            for right in range(left + 1, n):
                area = min(heights[left], heights[right]) * (right - left)
                max_area = max(area, max_area)
        return max_area

    @staticmethod
    def container_most_water_two_pointer(heights: List[int]) -> List[List[int]]:
        n = len(heights)
        max_area = 0
        left, right = 0, n - 1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(area, max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
