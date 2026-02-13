from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        n = len(nums)
        window = set()

        for j in range(n):
            if j - i > k:
                window.remove(nums[i])
                i += 1

            if nums[j] in window:
                return True

            window.add(nums[j])

        return False
