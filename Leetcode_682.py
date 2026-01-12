from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:

        scoreStack = []

        for ele in operations:

            if ele == "+":
                score1 = scoreStack.pop()
                score2 = scoreStack.pop()
                sum = score1 + score2

                scoreStack.append(score2)
                scoreStack.append(score1)
                scoreStack.append(sum)

            elif ele == "D":
                topScore = scoreStack.pop()
                newScore = topScore * 2

                scoreStack.append(topScore)
                scoreStack.append(newScore)

            elif ele == "C":
                scoreStack.pop()

            else:
                scoreStack.append(int(ele))

        sum = 0

        for score in scoreStack:
            sum += score

        return sum


s = Solution()
print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
