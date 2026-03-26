class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        nge = [-1] * n
        mono = []

        # Build NGE array
        for i in range(n - 1, -1, -1):
            while mono and mono[-1] <= nums2[i]:
                mono.pop()

            if mono:
                nge[i] = mono[-1]

            mono.append(nums2[i])

        # Find results for nums1
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.append(nge[j])
                    break

        return res