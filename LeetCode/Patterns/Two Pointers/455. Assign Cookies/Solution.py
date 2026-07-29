class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        i = j = 0
        cnt = 0

        n1, n2 = len(g), len(s)

        while j < n1 and i < n2:
            if g[j] <= s[i]:
                cnt += 1
                i += 1
                j += 1
            else:
                j += 1

        return cnt