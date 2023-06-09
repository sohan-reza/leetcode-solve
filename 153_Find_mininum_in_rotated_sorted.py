class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = 10000000000
        while l < r:


            mid = (l+r)//2

            if nums[mid] < nums[r]:
                r=mid-1
            elif nums[mid] > nums[r]:
                l = mid+1
            ans = min(ans, nums[mid])
        return min(ans, nums[l])
