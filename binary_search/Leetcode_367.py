class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        L = 1
        R = num

        while L <= R:
            M = L + ((R - L) // 2)

            sq = M * M

            if sq == num:
                return True
            elif sq > num:
                R = M - 1
            else:
                L = M + 1

        return False
