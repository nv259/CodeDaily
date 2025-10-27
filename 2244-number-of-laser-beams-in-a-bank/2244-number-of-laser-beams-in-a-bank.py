class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev_devices = 0
        for row in bank:
            current_devices = sum(1 if ele == '1' else 0 
                                    for ele in row)

            if current_devices == 0:
                continue 

            ans += prev_devices * current_devices
            prev_devices = current_devices

        return ans

