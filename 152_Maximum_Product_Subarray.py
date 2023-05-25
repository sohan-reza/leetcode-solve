class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        l = r = 1

        for i in range(0, len(nums)):
            if l==0:
                l=1
            if r==0:
                r=1

            l *= nums[i]
            r *= nums[len(nums)-1-i]

            ans = max(ans, max(l, r)) 

        return ans
