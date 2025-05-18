from typing import List, Tuple
from itertools import product

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7

        # Step 1: Generate valid single column colorings (no vertical repeats)
        def is_valid(col: Tuple[int]) -> bool:
            return all(col[i] != col[i+1] for i in range(m - 1))

        all_cols = [col for col in product(range(3), repeat=m) if is_valid(col)]

        # Step 2: Build adjacency (compatibility) map
        compatible = {}
        for c1 in all_cols:
            compatible[c1] = []
            for c2 in all_cols:
                if all(c1[i] != c2[i] for i in range(m)):  # No same color in same row (horizontal neighbors)
                    compatible[c1].append(c2)

        # Step 3: DP initialization
        dp = {col: 1 for col in all_cols}  # For column 1

        # Step 4: Fill DP for all n columns
        for _ in range(n - 1):
            new_dp = {col: 0 for col in all_cols}
            for curr_col in all_cols:
                for prev_col in compatible[curr_col]:
                    new_dp[curr_col] = (new_dp[curr_col] + dp[prev_col]) % mod
            dp = new_dp

        # Final result is sum of all dp values for last column
        return sum(dp.values()) % mod
