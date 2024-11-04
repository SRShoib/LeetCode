class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prod = 1; temp = 1; t=0
        for i in nums:
            if i == 0:
                t += 1
            if t > 1:
                temp = 0
            if i != 0:
                temp *= i
            prod *= i

        for i in nums:
            if i == 0:
                ans.append(temp)
            else:
                ans.append(int(prod/i))
        return ans