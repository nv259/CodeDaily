class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_cnt, r_cnt = 0, 0
        for c in moves:
            l_cnt += 1 if c == 'L' else 0
            r_cnt += 1 if c == 'R' else 0

        return abs(l_cnt - r_cnt) + (len(moves) - l_cnt - r_cnt)