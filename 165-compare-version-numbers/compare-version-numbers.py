class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split versions into parts and convert to integers
        v1_parts = [int(x) for x in version1.split('.')]
        v2_parts = [int(x) for x in version2.split('.')]

        # Make lengths equal by padding with zeros
        max_len = max(len(v1_parts), len(v2_parts))
        v1_parts.extend([0] * (max_len - len(v1_parts)))
        v2_parts.extend([0] * (max_len - len(v2_parts)))

        # Compare each component
        for a, b in zip(v1_parts, v2_parts):
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
