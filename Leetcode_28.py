class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return -1
        left = 0
        right = left + (len(needle) - 1)

        while right < len(haystack):

            if haystack[left : right + 1] == needle:
                return left

            left += 1
            right = left + (len(needle) - 1)

        return -1
