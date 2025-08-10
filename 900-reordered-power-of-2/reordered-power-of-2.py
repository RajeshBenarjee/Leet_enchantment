class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter
        
        count_n = Counter(str(n))
        
        for i in range(31): 
            if count_n == Counter(str(1 << i)):
                return True
        
        return False
