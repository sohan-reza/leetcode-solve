class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_right = []
        right_left = []

        left_right.append(nums[0])
        right_left.append(nums[len(nums)-1])

        for i in range(1, len(nums)):
            left_right.append(left_right[i-1]*nums[i])

        j = 0
        for i in range(len(nums)-2, -1, -1):
            right_left.append(right_left[j]*nums[i])
            j+=1
        
        ans = []
        n = len(nums)
        ans.append(right_left[n-2])
        
        l_p = 0
        r_p = n-3
        for i in range(1, n-1):
            ans.append(left_right[l_p]*right_left[r_p])
            l_p+=1
            r_p-=1
        ans.append(left_right[n-2])
        return ans
