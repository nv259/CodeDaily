class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        N = len(s1)

        def is_same(list1, list2):
            list1.sort()
            list2.sort()

            for c1, c2 in zip(list1, list2):
                if c1 != c2: return False
            
            return True

        return is_same(
            [s1[i] for i in range(0, N, 2)],
            [s2[i] for i in range(0, N, 2)],
        ) and is_same(
            [s1[i] for i in range(1, N, 2)],
            [s2[i] for i in range(1, N, 2)],
        )


