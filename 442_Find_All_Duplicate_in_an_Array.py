class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        list_count = [0 for i in range(len(nums)+1)]
        count_duplicate = 0
        for i in nums:
            if(list_count[i]>0):
                count_duplicate+=1
            list_count[i]+=1
        c = 0
        ans = [0 for i in range(count_duplicate)]
        for i in range(len(list_count)):
            if list_count[i] >1 :
                ans[c] = i
                c+=1
        return ans
        
        
