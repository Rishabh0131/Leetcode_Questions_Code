class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return False

        stack = []
        closeOption = {")": "(", "}": "{", "]": "["}
        elements_in_stack = 0

        for i in range(len(s)):
            if s[i] not in closeOption.keys():
                stack.append(s[i])
                elements_in_stack += 1
            else:
                if not stack:
                    return False
                if closeOption.get(s[i]) != stack[elements_in_stack - 1]:
                    return False
                else:
                    stack.pop(elements_in_stack - 1)
                    elements_in_stack -= 1

        if stack:
            return False

        return True
