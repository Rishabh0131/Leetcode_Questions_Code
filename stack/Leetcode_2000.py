class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        foundit = False
        foundIdx = 0

        res = list(word)
        for char in word:
            if char != ch:
                stack.append(char)
                foundIdx += 1
            else:
                stack.append(char)
                foundIdx += 1
                foundit = True
                break
        if foundit:
            i = 0

            while foundIdx > i:
                res[i] = stack.pop()
                i += 1

        return "".join(res)

    def reversePrefixTwoPointer(self, word: str, ch: str) -> str:
        res = list(word)
        left = 0

        for right, char in enumerate(res):
            if char == ch:
                while left < right:
                    res[left], res[right] = res[right], res[left]
                    left += 1
                    right -= 1
                break

        return "".join(res)
