from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        n = len(nums)
        res = nums[n] - nums[left]
        for right in range(n):
            if right - left + 1 == k:
                score = nums[right] - nums[left]
                res = min(res, score)
                left += 1

        return res
