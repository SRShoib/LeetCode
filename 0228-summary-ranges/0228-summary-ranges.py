class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans
        if len(nums) == 1:
            ans.append(str(nums[0]))
            return ans

        a = nums[0]
        t = 1
        if (nums[1] - nums[0] != 1):
            ans.append(str(nums[0]))
            a = nums[1]; t=2
        
        for i in range(t, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if a == nums[i-1]:
                    ans.append(str(a))
                else:
                    ans.append(f"{a}->{nums[i-1]}")
                a = nums[i]

        if a == nums[-1]:
            ans.append(str(a))
        else:
            ans.append(f"{a}->{nums[-1]}")

        return ans
        
            