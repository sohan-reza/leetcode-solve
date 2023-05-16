class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        from collections import defaultdict
        mp = defaultdict(int)

        for i in range(len(nums)):
            if mp[target-nums[i]] != 0:
                ans.append(i)
                ans.append(mp[target-nums[i]]-1)
                break
            mp[nums[i]] = i+1
        return ans
