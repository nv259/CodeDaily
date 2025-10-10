class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy = energy[::-1]
        ans = -float('inf')
        prefix_sum = [0] * len(energy)

        for i in range(len(energy)):
            if i < k:
                prefix_sum[i] = energy[i]
            else:
                prefix_sum[i] = energy[i] + prefix_sum[i - k]

            ans = max(ans, prefix_sum[i])

        return ans