class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        res_stack = []
        depth = 0

        for ch in s:
            if ch == "(":
                if depth > 0:
                    res_stack.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res_stack.append(ch)

        return "".join(res_stack)
