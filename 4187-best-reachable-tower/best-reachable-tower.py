mn = lambda x, y: x if x < y else y

class Solution:
    def bestTower(self, towers: List[List[int]], 
                  center: List[int], radius: int) -> List[int]:

        (cx, cy), ans = center, [1, -1, -1]

        for x, y, q in towers:
            if abs(cx - x) + abs(cy - y) <= radius:  # <-- radius criterion
                ans = mn(ans, [-q, x, y])            # <-- determine the minimum 

        return ans[1:3]                 