from collections import Counter 

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # half=set(s)
        # half=list(half)
        # stringi="".join(i for i in half)
        # return stringi+stringi[::-1]

        s=Counter(s)
        mid=""
        half=[]
        for i in sorted(s.keys()):
            freq=s[i]
            half.append(i*(freq//2))
            if freq%2==1:
                mid=i
        half_str=''.join(half)
        return half_str+mid+half_str[::-1]
        
        