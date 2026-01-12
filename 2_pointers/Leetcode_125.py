class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1
        while right > left:

            while right > left and not s[right].isalnum():
                right -= 1

            while right > left and not s[left].isalnum():
                left += 1

            if s[left].lower() != s[right].lower():
                return False

            right -= 1
            left += 1

        return True


a = Solution()

print(a.isPalindrome("A man, a plan, a canal: Panama"))
