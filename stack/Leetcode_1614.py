class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        stack = []

        res = 0

        for ch in s:
            if ch == "(":
                stack.append(ch)
                depth += 1
            elif ch == ")":
                stack.pop()
                if depth > res:
                    res = depth
                depth -= 1
            else:
                continue

        return res
