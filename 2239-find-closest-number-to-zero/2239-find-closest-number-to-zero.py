class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        sol = nums[0]

        for i in nums:
            if abs(i) < abs(sol):
                sol = i
            if abs(i) == abs(sol):
                if i < 0 and sol < 0:
                    sol = sol
                else:
                    sol = abs(sol)
        return sol
