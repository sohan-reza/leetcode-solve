class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums)==1:
            if nums[0] == target:
                return 0
            else:
                return -1

        t = nums[0]
        break_point = -1
        for i in range(1, len(nums)):
            if nums[i] < t:
                break_point = i
                break
        
        start = 0
        if break_point == -1:
            end = len(nums)-1
        else:
            end = break_point-1
       # print(end)


        
        if target <= nums[end] and target >= nums[start]:
            
            while start <= end:
                mid = (start+end)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start = mid+1
                else:
                    end = mid-1
        else:
            i = break_point
            e = len(nums) - 1
            print(i, e)
            while i <= e:
                mid = (i+e) // 2
                # print(mid)
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    i = mid+1
                else:
                    e = mid-1
        return -1

