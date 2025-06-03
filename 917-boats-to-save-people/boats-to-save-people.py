class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # T(N)=O(N) and S(N)=O(1)
        people.sort() 
        lo, hi = 0, len(people) - 1
        boats = 0
        
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            hi -= 1
            boats += 1
        
        return boats