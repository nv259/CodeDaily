class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        powers = []

        freq = {}
        for power_ in power:
            if power_ not in freq:
                freq[power_] = 0
                powers.append(power_)
            freq[power_] += 1

        print(powers)
        print(freq)

        n = len(powers)
        dp = [0] * n
        dp[0] = powers[0] * freq[powers[0]]
        
        for i in range(n):
            if i == 0: continue

            power = powers[i]

            # skip i-th spell
            dp[i] = dp[i - 1]

            # pick i-th spell
            max_prev_damage = 0
            for j in range(i - 3, i):
                if j < 0: continue

                if power - powers[j] > 2:
                    max_prev_damage = max(
                        max_prev_damage,
                        dp[j]
                    )
            dp[i] = max(dp[i], max_prev_damage + power * freq[power])

        return dp[-1]
            