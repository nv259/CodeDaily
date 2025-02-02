class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = {}
        for num in arr:
            if num not in occur:
                occur[num] = 0
            occur[num] += 1

        return len(occur.keys()) == len(set(occur.values())) 