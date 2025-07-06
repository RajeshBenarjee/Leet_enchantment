
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1[:]
        self.nums2 = nums2[:]
        self.counter2 = Counter(self.nums2)  
    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.counter2[old_val] -= 1 
        if self.counter2[old_val] == 0:
            del self.counter2[old_val] 
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.counter2[new_val] += 1

    def count(self, tot: int) -> int:
        cnt = 0
        for num in self.nums1:
            complement = tot - num
            cnt += self.counter2.get(complement, 0)  
        return cnt
