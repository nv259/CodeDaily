class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        # Initialize window of size k
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        
        max_vowel_letters = vowel_count

        # Slide the window to the right
        for i in range(k, len(s)):
            if s[i] in vowels:
                vowel_count += 1
            if s[i - k] in vowels:
                vowel_count -= 1 
            max_vowel_letters = max(max_vowel_letters, vowel_count)

        return max_vowel_letters
