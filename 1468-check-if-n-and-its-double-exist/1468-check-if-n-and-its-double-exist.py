class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        exist = defaultdict(bool)
        for num in arr:
            if exist[num * 2]:
                return True
            if exist[num / 2]:
                return True
            exist[num] = True
        
        return False