class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        st = ""
        a = len(word1)
        b = len(word2)
        n = a+b
        for i in range(n):
            if i<a:
                st += word1[i]
            if i<b:
                st += word2[i]
        return st