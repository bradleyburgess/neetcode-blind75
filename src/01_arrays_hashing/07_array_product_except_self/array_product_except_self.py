from typing import List


class Solution:
    @staticmethod
    def product_except_self_zero_index(nums: List[int]) -> List[int]:
        product = 1
        zero_index = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_index != None:
                    return [0 for _ in range(len(nums))]
                zero_index = i
            else:
                product *= nums[i]

        result = []
        for i in range(len(nums)):
            if zero_index != None:
                if i == zero_index:
                    num = product
                else:
                    num = 0
            else:
                num = int(product / nums[i])
            result.append(num)
        return result

    @staticmethod
    def product_except_self_prefix_suffix(nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_products = [1] * n
        prefix_products = [1] * n
        for i in range(1, n):
            suffix_products[i] = suffix_products[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            prefix_products[i] = prefix_products[i + 1] * nums[i + 1]
        return [prefix_products[i] * suffix_products[i] for i in range(n)]
    
    @staticmethod
    def product_except_self_prefix_suffix_optimized(nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result

