class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        type_dict = {}
        res = 0
        i, j = 0, 0

        while j < len(fruits):
            # expand as much as possible
            if fruits[j] not in type_dict:
                if len(type_dict) < 2:
                    type_dict[fruits[j]] = 1
                else:
                    while len(type_dict) == 2:
                        type_dict[fruits[i]] -= 1
                        if type_dict[fruits[i]] == 0: del type_dict[fruits[i]]
                        i += 1
                    type_dict[fruits[j]] = 1
            else:
                type_dict[fruits[j]] += 1

            res = max(res, j - i + 1) 
            j += 1
        
        return res