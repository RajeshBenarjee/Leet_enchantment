from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
       s=Counter(s)
       sl=list(s.values())
       return all(x==sl[0] for x in sl) 