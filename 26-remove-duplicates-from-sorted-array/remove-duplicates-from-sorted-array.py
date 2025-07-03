class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # array nums sorted in non-decreasing order --> Ascending order --> Atleast traverse once -- O(N)
        # remove the duplicates 'in-place ' unique element appears only once -- poping -- O(1)
        # relative order -- > maintain order --> can't sort 
        # return the number of unique elements --> length of undate array -- inbuilt fun -- O(1)

        # 1. traverse through the list using a pointer not for loop bcz of pop fun()
        # 2. create a hash if ele already in hash pop it 
        # 3. else add it to hash 
        # 4. return the len of nums

        # l=0
        # hashy=set()
        # while l<len(nums):
        #     if nums[l] in hashy:
        #         nums.pop(l)
        #     else:
        #         hashy.add(nums[l])
        #         l+=1
        # return len(nums)


        # optimal Approach -> two pointers approach 

        i=0
        j=0
        while j<len(nums):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
            j+=1

        return i+1