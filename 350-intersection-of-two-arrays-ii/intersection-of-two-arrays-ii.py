class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        l1=0
        l2=0
        res=[]
        n1=len(nums1)
        n2=len(nums2)

        while l1<n1 and l2<n2:
            if nums1[l1]==nums2[l2]:
                res.append(nums1[l1])
                l1+=1
                l2+=1
            elif nums1[l1]<nums2[l2]:
                l1+=1
            elif nums1[l1]>nums2[l2]:
                l2+=1
        
        return res