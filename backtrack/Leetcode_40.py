from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def backtrack(start, subset, total):

            if total == target:
                res.append(subset[:])
                return

            if start >= len(candidates) or total > target:
                return

            # Included Canaidate Branch
            subset.append(candidates[start])
            backtrack(start + 1, subset, total + candidates[start])
            subset.pop()

            # Excluded Canaidate Branch
            while (
                start + 1 < len(candidates)
                and candidates[start] == candidates[start + 1]
            ):
                start += 1

            backtrack(start + 1, subset, total)

        backtrack(0, [], 0)

        return res
