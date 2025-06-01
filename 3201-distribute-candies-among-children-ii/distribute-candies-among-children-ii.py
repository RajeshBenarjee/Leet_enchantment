class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def count_ways(n):
            if n < 0:
                return 0
            return (n + 1) * (n + 2) // 2
        
        total_ways = count_ways(n)
        
        for i in range(3):
            total_ways -= count_ways(n - (limit + 1))
        
        for i in range(3):
            total_ways += count_ways(n - 2 * (limit + 1))
        total_ways -= count_ways(n - 3 * (limit + 1))
        
        return total_ways
