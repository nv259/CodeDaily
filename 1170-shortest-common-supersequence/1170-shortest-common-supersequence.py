class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        prev = [str2[j: ] for j in range(m)]
        prev.append("")

        for i in reversed(range(n)):
            curr = [""] * m
            curr.append(str1[i:])

            for j in reversed(range(m)):
                if str1[i] == str2[j]:
                    curr[j] = str1[i] + prev[j + 1]
                else:
                    res1 = str1[i] + prev[j]
                    res2 = str2[j] + curr[j + 1]

                    if len(res1) < len(res2):
                        curr[j] = res1
                    else:
                        curr[j] = res2
                    
            prev = curr

        return curr[0]