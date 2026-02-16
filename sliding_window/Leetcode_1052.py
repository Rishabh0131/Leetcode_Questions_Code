from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:

        left = 0

        satisfied = unsatified = moreSatisfied = 0
        n = len(customers)

        for idx in range(n):
            if not grumpy[idx]:
                satisfied += customers[idx]

        for right in range(n):
            if grumpy[right]:
                unsatified += customers[right]

            if right - left + 1 == minutes:
                moreSatisfied = max(moreSatisfied, unsatified)

                if grumpy[left]:
                    unsatified -= customers[left]

                left += 1

        return satisfied + moreSatisfied
