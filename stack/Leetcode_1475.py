from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        result = prices[:]
        stack = []

        for i in range(len(prices)):

            while stack and prices[stack[-1]] >= prices[i]:
                discountIdx = stack.pop()
                result[discountIdx] = prices[discountIdx] - prices[i]
            stack.append(i)

        return result
