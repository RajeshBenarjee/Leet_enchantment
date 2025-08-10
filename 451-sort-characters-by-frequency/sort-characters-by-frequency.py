from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        res = ''
        for char, freq in sorted_counts:
            res += char * freq
        return res