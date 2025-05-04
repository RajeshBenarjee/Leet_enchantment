from collections import Counter 
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        normalized = [tuple(sorted(domino)) for domino in dominoes]
        pairs=0
        s = Counter(normalized)
        for i in s.values():
            pairs+=i*(i-1)//2
        return pairs