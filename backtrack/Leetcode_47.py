from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        used = [False] * len(nums)
        nums.sort()

        res = []

        def backtrack(used, subset):

            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for i in range(0, len(nums)):

                if used[i]:
                    continue

                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue

                used[i] = True
                subset.append(nums[i])
                backtrack(used, subset)
                subset.pop()
                used[i] = False

        backtrack(used, [])

        return res
