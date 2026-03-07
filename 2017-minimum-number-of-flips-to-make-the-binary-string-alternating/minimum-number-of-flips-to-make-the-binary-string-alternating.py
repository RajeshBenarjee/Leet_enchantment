class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        _10, _01 = 0, 0
        res = float('inf')
        l = 0
        
        for r in range(len(s)):
            
            # pattern 0101...
            if s[r] != str(r % 2):
                _01 += 1
            
            # pattern 1010...
            if s[r] != str((r + 1) % 2):
                _10 += 1
            
            # maintain window size n
            if r - l + 1 > n:
                if s[l] != str(l % 2):
                    _01 -= 1
                if s[l] != str((l + 1) % 2):
                    _10 -= 1
                l += 1
            
            # update result
            if r - l + 1 == n:
                res = min(res, _01, _10)
        
        return res