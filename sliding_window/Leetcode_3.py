class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mapPrev = {}
        res = left = 0

        for right in range(len(s)):
            if s[right] in mapPrev:
                left = max(mapPrev[s[right]], left)

            mapPrev[s[right]] = right

            res = max(res, (right - left + 1))

        return res
