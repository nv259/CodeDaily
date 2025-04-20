class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        n = len(answers)
        answers.append(float('inf'))
        ret, i = 0, 0
        while i < n:
            ret += answers[i] + 1
            j = i
            for j in range(i + 1, min(n, i + answers[i] + 1)):
                if answers[j] != answers[i]:
                    break
            if answers[i] == answers[j]: 
                j += 1 
            i = j

        return ret
