from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        sum = 0
        res = 0

        n = len(arr)

        for right in range(n):
            sum += arr[right]
            if right - left + 1 == k:
                if sum >= k * threshold:
                    res += 1

                sum = sum - arr[left]
                left += 1

        return res
