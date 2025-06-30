import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(l, r):
            if l >= r:
                return True
            if not s[l].isalnum():
                return helper(l + 1, r)
            if not s[r].isalnum():
                return helper(l, r - 1)
            if s[l].lower() != s[r].lower():
                return False
            return helper(l + 1, r - 1)

        return helper(0, len(s) - 1)