def C2_(n):
    if n == 2:
        return 1

    prod = 1
    for i in range(1, n + 1):
        prod *= i
        if i == n - 2:
            nk_fact = prod
        elif i == n:
            n_fact = prod

    return n_fact // (nk_fact * 2)

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Preprocess dominoes s.t. the lower value comes first
        for idx in range(len(dominoes)):
            if dominoes[idx][0] > dominoes[idx][1]:
                dominoes[idx][0], dominoes[idx][1] = dominoes[idx][1], dominoes[idx][0]

        # Process
        ret = 0
        domino_dict = {}
        for x, y in dominoes:
            if x not in domino_dict:
                domino_dict[x] = {}
            if y not in domino_dict[x]:
                domino_dict[x][y] = 0
            domino_dict[x][y] += 1
        
        for x, dict_x in domino_dict.items():
            for xy, val in dict_x.items():
                if val > 1: ret += C2_(val)
        
        return ret
        