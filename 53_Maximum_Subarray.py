class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        ans = -100000
        for i in range(len(nums)):
            sum = max(nums[i], sum+nums[i])
            ans = max(ans, sum)
        return ans
