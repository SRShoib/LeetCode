class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        l = len(s)
        for i in range(len(t)):
            if t[i] == s[j] and l != 0 and j < l:
                j +=1

        if j == len(s):
            return True
        return False