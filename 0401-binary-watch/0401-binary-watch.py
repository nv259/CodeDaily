class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        nums = [8, 4, 2, 1] + [32, 16, 8, 4, 2, 1]
        turned_on = [-1] * 10
        ans = []

        def is_valid(hour, mins):
            return 0 <= hour <= 11 and 0 <= mins <= 59

        def to_digital(hour, mins):
            hour = str(hour)
            mins = str(mins) 
            if len(mins) < 2:
                mins = '0' + mins

            return hour + ':' + mins

        def backtrack(i):
            # prune impossible solutions 
            if sum(turned_on[:i]) + (10 - i) < turnedOn:
                return

            if i == 10:
                # double check hehe
                if sum(turned_on) != turnedOn: return

                hour = sum(nums[i] * turned_on[i] for i in range(4))
                mins = sum(nums[i] * turned_on[i] for i in range(4, 10))

                if is_valid(hour, mins):
                    ans.append(to_digital(hour, mins))
            
                return
            
            # try to turn off
            turned_on[i] = 0
            backtrack(i + 1)

            # try to turn on
            turned_on[i] = 1
            backtrack(i + 1)

            # unset 
            turned_on[i] = -1
            return


        backtrack(0)

        return list(set(ans))
        
