from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []

        def raj(i, res):
            # If length becomes n, store the string
            if i == n:
                result.append("".join(res))
                return
            
            # Always allowed to add '1'
            res.append('1')
            raj(i + 1, res)
            res.pop()
            
            # Add '0' only if previous was not '0'
            if not res or res[-1] != '0':
                res.append('0')
                raj(i + 1, res)
                res.pop()

        raj(0, [])
        return result