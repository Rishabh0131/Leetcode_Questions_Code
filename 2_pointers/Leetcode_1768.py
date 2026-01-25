class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Ptr = 0
        word2Ptr = 0

        resString = []

        while word1Ptr < len(word1) or word2Ptr < len(word2):
            if word1Ptr < len(word1):
                resString.append(word1[word1Ptr])

            if word2Ptr < len(word2):
                resString.append(word2[word2Ptr])

            word1Ptr += 1
            word2Ptr += 1
        return "".join(resString)


s = Solution()

print(s.mergeAlternately("ab", "pqrs"))
