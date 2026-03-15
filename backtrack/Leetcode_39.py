from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(start, subset, total):

            if total == target:
                res.append(subset[:])
                return

            if start >= len(candidates) or total > target:
                return

            subset.append(candidates[start])
            backtrack(start, subset, total + candidates[start])

            subset.pop()

            backtrack(start + 1, subset, total)

        backtrack(0, [], 0)

        return res
