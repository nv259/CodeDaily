class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for str in strs:
            sorted_strs.append([''.join(sorted([c for c in str])), str])

        sorted_strs.sort()
        ans = {}
        for sorted_str, str in sorted_strs:
            if sorted_str not in ans:
                ans[sorted_str] = []
            ans[sorted_str].append(str)

        return list(ans.values())
        