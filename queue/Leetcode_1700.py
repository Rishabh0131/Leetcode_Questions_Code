from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        i = 0
        fails = 0

        while queue and fails < len(queue):
            if queue[0] == sandwiches[i]:
                queue.popleft()
                i += 1
                fails = 0
            else:
                queue.append(queue.popleft())
                fails += 1

        return len(queue)

    def countStudentsOptimised(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]

        for s in students:
            count[s] += 1

        for sandwiche in sandwiches:
            if count[sandwiche] == 0:
                break
            count[sandwiche] -= 1

        return count[0] + count[1]
