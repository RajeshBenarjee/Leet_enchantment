class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        
        res = []
        for word in words:
            w = set(word.lower())  # convert to lowercase and set to check membership
            if w.issubset(first) or w.issubset(second) or w.issubset(third):
                res.append(word)
        return res