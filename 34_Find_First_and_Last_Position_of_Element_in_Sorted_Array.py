class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:

     
        def findFirst(l, r, target):
            index = -1
            while l <= r:
                mid = l+(r-l)//2

                if nums[mid] == target:
                    index = mid
                if nums[mid] < target:
                    l = mid+1
                if nums[mid] >= target:
                    r = mid-1
            return index
        
        def findLast(l, r, target):
            index = -1
            while l <= r:
                mid = l+(r-l)//2

                if nums[mid] == target:
                    index = mid
                if nums[mid] <= target:
                    l = mid+1
                if nums[mid] > target:
                    r = mid-1
            return index

        l = 0
        r = len(nums) - 1

        ans = []
        ans.append(findFirst(l, r, target))
        ans.append(findLast(l,r, target))

        return ans        

        
            
    
