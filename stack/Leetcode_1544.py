class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for ch in s:
            if stack:
                if stack[-1].lower() == ch.lower():
                    if stack[-1].isupper() != ch.isupper():
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        return "".join(stack)
