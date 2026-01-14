from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        posStack = []
        for log in logs:
            if log == "../":
                if posStack:
                    posStack.pop()
            elif log == "./":
                continue
            else:
                posStack.append(log)

        return len(posStack)
