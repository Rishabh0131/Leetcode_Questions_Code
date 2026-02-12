class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = []
        for word in words:
            i, j = 0, len(word) - 1
            chars = list(word)

            while i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
            res.append("".join(chars))

        return " ".join(res)

    def reverseWords2ndApproch(self, s: str) -> str:

        chars = list(s)
        left = 0

        for right in range(len(chars)):
            if chars[right] == " " or right == len(chars) - 1:
                tempL = left
                tempR = right - 1 if chars[right] == " " else right
                while tempL < tempR:
                    chars[tempL], chars[tempR] = chars[tempR], chars[tempL]
                    tempL += 1
                    tempR -= 1
                left = right + 1

        return "".join(chars)
