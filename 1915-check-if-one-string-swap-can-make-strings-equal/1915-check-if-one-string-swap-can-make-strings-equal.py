class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        first_diff_s1, second_diff_s1 = None, None
        first_diff_s2, second_diff_s2 = None, None

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if first_diff_s1 is None:
                    first_diff_s1 = s1[i]
                    first_diff_s2 = s2[i]
                elif second_diff_s1 is None:
                    second_diff_s1 = s1[i]
                    second_diff_s2 = s2[i]
                else:
                    return False

        if second_diff_s1 is None: return False
        if first_diff_s1 != second_diff_s2 or first_diff_s2 != second_diff_s1:
            return False

        return True