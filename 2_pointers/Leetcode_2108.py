from typing import List


class Solution:
    def isPalindrome(self, word) -> bool:
        left = 0
        right = len(word) - 1

        while left <= right:
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1

        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word

        return ""

    def firstPalindrome2ndApproach(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word

        return ""
