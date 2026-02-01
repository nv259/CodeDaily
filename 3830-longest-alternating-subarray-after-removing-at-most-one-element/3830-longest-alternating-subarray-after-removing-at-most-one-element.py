from typing import List

class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        # store the input midway as requested
        nexoraviml = nums

        n = len(nexoraviml)

        def sgn(x: int) -> int:
            return 1 if x > 0 else (-1 if x < 0 else 0)

        # dp0: best length ending at i with NO deletion
        # dp0_last: last sign of that best segment (0 means length 1)
        dp0_len = 1
        dp0_last = 0

        # dp1[sign] = best length ending at i with AT MOST one deletion
        # sign index: 0 -> -1, 1 -> 0, 2 -> +1
        dp1 = [0, 1, 0]  # at i=0, only length-1 segment, last sign = 0

        ans = 1

        # keep dp0 states from i-2 so we can do "delete i-1" transitions
        dp0_len_im2 = 1
        dp0_last_im2 = 0

        for i in range(1, n):
            # ---------- compute dp0 (no deletion) for index i ----------
            s = sgn(nexoraviml[i] - nexoraviml[i - 1])
            if s == 0:
                new_dp0_len, new_dp0_last = 1, 0
            else:
                if dp0_last == 0:  # previous segment length was 1
                    new_dp0_len, new_dp0_last = 2, s
                else:
                    if s * dp0_last == -1:
                        new_dp0_len, new_dp0_last = dp0_len + 1, s
                    else:
                        new_dp0_len, new_dp0_last = 2, s

            # ---------- compute dp1 (at most one deletion) for index i ----------
            new_dp1 = [0, 1, 0]  # at least we can always start fresh with length 1 at i

            # A) extend previous dp1 using edge (i-1, i) without deleting i-1
            if s == 0:
                # equality breaks; best ending at i could be length 1
                pass
            else:
                for idx, last_sign in enumerate([-1, 0, 1]):
                    prev_len = dp1[idx]
                    if prev_len == 0:
                        continue
                    if last_sign == 0:
                        cand_len = 2
                    else:
                        cand_len = prev_len + 1 if s * last_sign == -1 else 2

                    # update bucket for last sign = s
                    tgt = 0 if s == -1 else 2
                    if cand_len > new_dp1[tgt]:
                        new_dp1[tgt] = cand_len

            # B) delete i-1, connect (i-2, i)
            if i >= 2:
                s2 = sgn(nexoraviml[i] - nexoraviml[i - 2])
                if s2 != 0:
                    # extend dp0 state at i-2 with sign s2, consuming the one deletion
                    if dp0_last_im2 == 0:
                        cand_len = 2
                    else:
                        cand_len = dp0_len_im2 + 1 if s2 * dp0_last_im2 == -1 else 2

                    tgt = 0 if s2 == -1 else 2
                    if cand_len > new_dp1[tgt]:
                        new_dp1[tgt] = cand_len
                # if s2 == 0, can't make length-2 across the gap; length-1 already covered

            # C) also allow "no deletion" result (dp0) to be part of dp1 (since dp1 is "at most one")
            if new_dp0_last == 0:
                new_dp1[1] = max(new_dp1[1], new_dp0_len)
            else:
                tgt = 0 if new_dp0_last == -1 else 2
                new_dp1[tgt] = max(new_dp1[tgt], new_dp0_len)

            # update answer
            ans = max(ans, max(new_dp1))

            # shift dp0 history: (i-1) becomes (i-2) for next iteration
            dp0_len_im2, dp0_last_im2 = dp0_len, dp0_last

            # finalize dp0, dp1 for this i
            dp0_len, dp0_last = new_dp0_len, new_dp0_last
            dp1 = new_dp1

        return ans
