from typing import List


class Solution:

    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        inDegree = [0] * n

        for _, v in edges:

            inDegree[v] += 1

        champion = -1

        for i in range(n):

            if inDegree[i] == 0:
                if champion != -1:
                    return -1

                champion = i

        return champion
