class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a.sort()==b.sort() --> nlogn
        # using dict one will add count aother will delete count if at last the hash is empty it will be anagram else false --> O(2N) --> O(2N)
        hashy={}
        for i in s:
            if i in hashy:
                hashy[i]+=1
            else:
                hashy[i]=1
        

        for i in t:
            if i not in hashy:
                return False
            else:
                if hashy[i]==1:
                    del hashy[i]
                else:
                    hashy[i]-=1
        return not(hashy)
                    