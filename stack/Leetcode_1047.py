class Solution:
    def removeDuplicates(self, s: str) -> str:

        res_stack = []

        for ch in s:
            if res_stack:
                if ch == res_stack[-1]:
                    res_stack.pop()
                else:
                    res_stack.append(ch)
            else:
                res_stack.append(ch)

        return "".join(res_stack)
