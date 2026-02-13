from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_ptr = 0  # Left
        sell_ptr = 1  # Right

        n = len(prices)
        maxP = 0

        for sell_ptr in range(n):
            if prices[buy_ptr] > prices[sell_ptr]:
                buy_ptr = sell_ptr

            maxP = max(maxP, (prices[sell_ptr] - prices[buy_ptr]))

        return maxP
