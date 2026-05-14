class Solution:
    @staticmethod
    def two_sum_brute(nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    @staticmethod
    def two_sum_hashmap(nums: list[int], target: int) -> list[int]:
        hash = dict()
        for index, value in enumerate(nums):
            hash[value] = index
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                complement_index = hash[complement]
                if index != complement_index:
                    return [index, hash[complement]]

    @staticmethod
    def two_sum_hashmap_one_pass(nums: list[int], target: int) -> list[int]:
        hash = dict()
        for index, value in enumerate(nums):
            complement = target - value
            if complement in hash:
                return [hash[complement], index]
            hash[value] = index
        return []
