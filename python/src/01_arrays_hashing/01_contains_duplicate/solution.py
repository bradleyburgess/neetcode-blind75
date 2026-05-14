class Solution:
    @staticmethod
    def contains_duplicate_brute(arr: list[int]) -> bool:
        result = False
        for i in range(len(arr)):
            if result:
                break
            for j in range(len(arr)):
                if j == i:
                    continue
                if arr[i] == arr[j]:
                    result = True
                    break
        return result

    @staticmethod
    def contains_duplicate_hashmap(arr: list[int]) -> bool:
        hash = dict()
        for item in arr:
            if item in hash:
                return True
            hash[item] = True
        return False

    @staticmethod
    def contains_duplicate_sorted(arr: list[int]) -> bool:
        arr = sorted(arr)
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return True
        return False
