import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear=re.sub(r'[^a-zA-Z0-9]','',s)
        clear=clear.lower()
        if clear==clear[::-1]:
            return True 
        return False