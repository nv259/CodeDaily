class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(c for c in n))