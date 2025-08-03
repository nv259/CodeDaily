class Solution:
    def compress(self, chars: List[str]) -> int:
        i, k = 0, 0

        while k < len(chars):
            j = k + 1
            while j < len(chars) and chars[k] == chars[j]:
                j += 1
            
            chars[i] = chars[k]
            count = j - k
            k = j
            i += 1
            if count > 1:
                count = str(count)
                for number in count:
                    chars[i] = number
                    i += 1
        
        return i
