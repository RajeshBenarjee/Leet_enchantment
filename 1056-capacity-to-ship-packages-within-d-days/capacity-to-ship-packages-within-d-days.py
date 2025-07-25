class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(arr,w,d):
            day_count = 1
            current_load = 0
            for weight in weights:
                if current_load + weight > w:
                    day_count += 1
                    current_load = 0
                current_load += weight
            return day_count <= days
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=low+(high-low)//2
            if possible(weights,mid,days):
                high=mid-1
            else:
                low=mid+1
        return low