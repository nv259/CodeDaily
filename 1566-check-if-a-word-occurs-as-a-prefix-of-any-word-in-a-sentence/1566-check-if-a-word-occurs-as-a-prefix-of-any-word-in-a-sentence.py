import re


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        pattern = rf"\b({searchWord}\w*)"
        result = re.search(pattern, sentence)

        if not result: return -1

        return sentence.split().index(result.group(0)) + 1