class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        def record(cnt, c):
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1

        cnt_s = {}
        cnt_t = {}
        for c in s: record(cnt_s, c)
        for c in t: record(cnt_t, c)

        for c in cnt_s.keys():
            if c not in cnt_t: return False
            if cnt_s[c] != cnt_t[c]: return False
        
        return True
        