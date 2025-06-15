class Solution:
    def generateTag(self, caption: str) -> str:
        res = '#'
        flag = False
        for ch in caption.strip():
            if ch == ' ':
                flag = True
            elif flag:
                res += ch.upper()
                flag = False
            else:
                res += ch.lower()
        return res[:100]
