from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        look_up = defaultdict(int)
        
        j=0
        mx=0
        for i in range(len(s)):
            if(look_up[s[i]] > 0):
                j = max(j, look_up[s[i]])
            look_up[s[i]] = i+1
            mx = max(mx, i-j+1)
        return mx
