class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        if s == "" and t == "":
            return True

        strStack_1 = []
        strStack_2 = []

        for ch in s:
            if ch != "#":
                strStack_1.append(ch)
            else:
                if strStack_1:
                    strStack_1.pop()

        for ch in t:
            if ch != "#":
                strStack_2.append(ch)
            else:
                if strStack_2:
                    strStack_2.pop()

        return strStack_1 == strStack_2
