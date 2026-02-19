class Solution:
    def arrangeCoins(self, n: int) -> int:
        L = 1
        R = n

        res = 0

        while L <= R:
            M = L + ((R - L) // 2)

            coins = M * (1 + M) // 2

            if coins > n:
                R = M - 1
            else:
                L = M + 1
                res = max(res, M)

        return res
