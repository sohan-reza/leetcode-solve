class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""

        ans = ""
        j=0
        loop=True
        mn = len(min(strs))
        while loop:
            for i in range(len(strs)-1):
                if len(strs[i])==0 or len(strs[i+1])==0:
                    return ""
                if strs[i][j]!=strs[i+1][j]:
                    loop=False
                    break
                
            if loop:
                if len(strs[0])>0:
                    ans+=strs[0][j]
                j+=1
            if j>=mn:
                break
        return ans
                

