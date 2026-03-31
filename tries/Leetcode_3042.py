from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                W1, W2 = words[i], words[j]
                L = len(W1)

                if W1 == W2[:L] and W1 == W2[-L:]:
                    res += 1

        return res
