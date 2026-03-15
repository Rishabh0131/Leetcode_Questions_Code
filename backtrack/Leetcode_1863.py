from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(start, path):
            nonlocal res

            xor = 0

            for n in path:
                xor ^= n

            res += xor

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res

    def subsetXORSumOptimal(self, nums: List[int]) -> int:

        res = 0
        for num in nums:
            res |= num
        return res << (len(nums) - 1)
