# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
#
class Solution:
    def guess(self, int) -> bool:
        return False

    def guessNumber(self, n: int) -> int:
        L = 1
        R = n

        while L <= R:
            M = L + ((R - L) // 2)
            if self.guess(M) == 0:
                return M
            elif self.guess(M) == -1:
                R = M - 1
            else:
                L = M + 1

        return -1
