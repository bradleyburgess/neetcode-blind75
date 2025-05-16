from typing import List


class Solution:
    @staticmethod
    def find_in_rotated_binary_search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target: return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target < nums[mid] or target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1