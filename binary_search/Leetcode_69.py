class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        L = 1
        R = x

        while L <= R:
            M = L + ((R - L) // 2)

            sq = M * M

            if sq == x:
                return M
            elif sq > x:
                R = M - 1
            else:
                L = M + 1

        return R
