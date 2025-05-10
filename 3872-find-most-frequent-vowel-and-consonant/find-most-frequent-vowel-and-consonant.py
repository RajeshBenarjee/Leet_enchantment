from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        con_f=vow_f=0
        counti=Counter(s)
        Count=dict(sorted(counti.items(),key=lambda x:x[1],reverse=True))
        vowels='aeiou'
        for i,j in Count.items():
            if con_f!=0 and vow_f!=0:
                break
            if i not in vowels and con_f==0:
                # print(i)
                # print(Count[i])
                con_f=Count[i]
            elif i in vowels and vow_f==0:
                # print(i)
                # print(Count[i])
                vow_f=Count[i]
        
        return vow_f+con_f