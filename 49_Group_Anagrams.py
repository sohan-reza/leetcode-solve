class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        from collections import defaultdict
        mp = defaultdict(int)
        for x in strs:
            tmp = str(sorted(x))
            if mp[tmp] is 0:
                mp[tmp] = [x]
            else:
                mp[tmp].append(x)

        for key in mp:
            ans.append(mp[key])
        return ans

