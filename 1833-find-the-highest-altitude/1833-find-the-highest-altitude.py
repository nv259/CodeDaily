class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0] * (len(gain) + 1)
        for idx, altitude_gain in enumerate(gain):
            altitude[idx + 1] = altitude[idx] + altitude_gain

        return max(altitude) 