class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        st = []
        for i in range(len(nums2) - 1, -1, -1):
            while st and st[-1] < nums2[i]:
                st.pop()
            d1[nums2[i]] = st[-1] if st else -1
            st.append(nums2[i])
        return [d1[i] for i in nums1]
