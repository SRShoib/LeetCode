class Solution:
    def romanToInt(self, s: str) -> int:
        v={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        value = v[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if v[s[i]] < v[s[i+1]]:
                value -= v[s[i]]
            else:
                value += v[s[i]]
        return value