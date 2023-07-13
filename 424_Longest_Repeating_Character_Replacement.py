class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(int)
        l = 0
        dic[s[0]] = 1
        ans = 1

        for i in range(1, len(s)):
            dic[s[i]] +=1
            win = 0
            for key, value in dic.items():
                win = max(win, value)
            if (i-l+1)-win <= k:
                ans = max(ans, (i-l+1))
            else:
                dic[s[l]] -=1
                l+=1
        return ans

        
            


