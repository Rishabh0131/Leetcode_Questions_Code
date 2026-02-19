class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}

        res = left = 0

        for right in range(len(s)):
            charCount[s[right]] = 1 + charCount.get(s[right], 0)

            while (right - left + 1) - max(charCount.values()) > k:
                charCount[s[left]] -= 1
                left += 1

            res = max(res, (right - left + 1))

        return res
