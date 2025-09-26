import random
from bisect import bisect_left
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        # Build prefix sums
        self.prefix = []
        running_sum = 0
        for weight in w:
            running_sum += weight
            self.prefix.append(running_sum)
        self.total = running_sum

    def pickIndex(self) -> int:
        # Pick a random number from 1 to total
        target = random.randint(1, self.total)
        # Binary search for first prefix >= target
        return bisect_left(self.prefix, target)
