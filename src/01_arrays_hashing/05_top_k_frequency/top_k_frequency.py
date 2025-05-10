from heapq import heappush, heappop
from collections import defaultdict, Counter
from typing import List


def top_k_frequency_hashmap(nums: List[int], k: int) -> List[int]:
    freq_hashmap = Counter(nums)
    freq_list = list()
    for num, freq in freq_hashmap.items():
        freq_list.append({"num": num, "freq": freq})
    return [
        x["num"] for x in sorted(freq_list, key=lambda i: i["freq"], reverse=True)[:k]
    ]


def top_k_frequency_heapq(nums: List[int], k: int) -> List[int]:
    freq_hashmap = Counter(nums)
    heap = []
    for num in freq_hashmap:
        heappush(heap, (freq_hashmap[num], num))
        if len(heap) > k:
            heappop(heap)
    top_k = [heappop(heap)[1] for _ in range(len(heap))]
    return top_k[::-1]


def top_k_frequency_buckets(nums: List[int], k: int) -> List[int]:
    freq_hashmap = Counter(nums)
    freq_buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_hashmap.items():
        freq_buckets[freq].append(num)
    top_k = []
    for i in range(len(freq_buckets) - 1, 0, -1):
        if len(top_k) == k:
            return top_k
        for num in freq_buckets[i]:
            top_k.append(num)
    return top_k