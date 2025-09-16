from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            # keep merging while top two numbers are not coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g == 1:
                    break
                # replace them with their lcm
                lcm = a * b // g
                stack.pop()
                stack[-1] = lcm
        return stack
