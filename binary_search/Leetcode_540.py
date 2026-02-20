from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        L = 0
        R = len(nums) - 1

        while L <= R:
            M = L + ((R - L) // 2)

            if (M - 1 < 0 or nums[M - 1] != nums[M]) and (
                M + 1 == len(nums) or nums[M + 1] != nums[M]
            ):
                return nums[M]

            leftsize = M - 1 if nums[M - 1] == nums[M] else M

            if leftsize % 2:
                R = M - 1
            else:
                L = M + 1

        return -1
