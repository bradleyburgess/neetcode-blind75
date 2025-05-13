from typing import List


class Solution:
    @staticmethod
    def max_profit_brute(prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        return max_profit

    @staticmethod
    def max_profit_sliding_window(prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_left = None
        for i in range(n):
            if i == 0:
                min_left = prices[i]
                continue
            profit = prices[i] - min_left
            max_profit = max(profit, max_profit)
            if prices[i] < min_left:
                min_left = prices[i]
        return max_profit
