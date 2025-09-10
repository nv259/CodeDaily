class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        f = [0] * (n + 1)
        modulo = int(1e9) + 7

        def recurse(k):
            if k > n: return 0
            if f[k]: return f[k]
            count = 0 if k <= n - forget else 1

            for i in range(k + delay, k + forget):
                count += recurse(i)
            f[k] = count % modulo

            return count % modulo

        return recurse(1) % modulo