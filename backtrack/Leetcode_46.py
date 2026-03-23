from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(used, subset):

            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for i in nums:

                if i in used:
                    continue

                used.add(i)
                subset.append(i)
                backtrack(used, subset)

                subset.pop()
                used.remove(i)

        backtrack(set(), [])
        return res
