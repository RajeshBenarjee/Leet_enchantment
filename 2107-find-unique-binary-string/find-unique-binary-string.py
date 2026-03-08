class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        j=0
        res=""
        for i in nums:
            x=int(i[j])
            if x:
                res+='0'
            else:
                res+='1'
            j+=1
        return res