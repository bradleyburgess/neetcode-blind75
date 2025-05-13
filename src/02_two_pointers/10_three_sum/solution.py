from typing import List


class Solution:
    @staticmethod
    def three_sum_brute(nums: List[int]) -> List[List[int]]:
        results = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        _result = list(sorted([nums[i], nums[k], nums[j]]))
                        add = True
                        for item in results:
                            if all(item[x] == _result[x] for x in range(3)):
                                add = False
                        if add:
                            results.append(_result)
        return results

    @staticmethod
    def three_sum_two_pointers(nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return results
