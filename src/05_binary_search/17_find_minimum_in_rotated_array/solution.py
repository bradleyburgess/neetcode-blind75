import math
from typing import List


class Solution:
    @staticmethod
    def find_min_verbose_direction(nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        min_val = nums[0]
        left = 0
        right = len(nums)

        prev = 0
        direction = "right"

        while True:
            if direction == "right":
                current = prev + math.ceil((right - prev) / 2)
                if current == right:
                    break
                if nums[current] > nums[prev]:
                    left = current
                else:
                    direction = "left"
                    right = current
                    min_val = min(nums[current], min_val)
                prev = current
            else:
                current = prev - math.ceil((prev - left) / 2)
                if current == left:
                    break
                if nums[current] < nums[prev]:
                    right = current
                    min_val = min(nums[current], min_val)
                else:
                    direction = "right"
                    left = current
                prev = current
        return min_val

    @staticmethod
    def find_min_binary_search(nums: List[int]) -> int:
        if not nums: raise ValueError

        left, right = 0, len(nums) - 1
        result = nums[left]

        while left <= right:
            mid = (right + left) // 2
            if nums[left] <= nums[right]:
                result = min(result, nums[left])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid - 1
        
        return result