class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt=0
        filtered = [nums[0]]
        for num in nums[1:]:
            if num != filtered[-1]:
                filtered.append(num)
        n=len(filtered)
        for i in range(1,n-1):
            if filtered[i-1]>filtered[i]<filtered[i+1]:
                cnt+=1
            elif filtered[i-1]<filtered[i]>filtered[i+1]:
                cnt+=1
        return cnt