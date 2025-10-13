class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def normalize(word):
            freq = {}
            for char in word:
                if char not in freq:
                    freq[char] = 0
                freq[char] += 1

            word = "" 
            for char in "qwertyuiopasdfghjklzxcvbnm":
                if char in freq:
                    word += char
                    word += str(freq[char])

            return word
    
        ans = []
        i, j = 0, 0
        while j < len(words):
            normalized_word_i = normalize(words[i])

            while j < len(words) and normalize(words[j]) == normalized_word_i:
                j += 1
            
            ans.append(words[i])
            i = j

        return ans