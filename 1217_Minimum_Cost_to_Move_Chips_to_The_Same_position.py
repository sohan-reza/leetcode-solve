class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Time complexity O(N) Space complexity is O(1)
        
        oddCount=0
        evenCount=0
        for i in position:
            if i%2 == 0:
                evenCount +=1
            else:
                oddCount +=1
        return min(oddCount, evenCount)
        '''
        ans =0
        targetIndex=0
        if oddCount>evenCount:
            targetIndex=1

        for i in position:
            
            if targetIndex%2==0:
                if i%2 !=0:
                    ans+=1
            else:
                print(i)
                if i%2 != 1:
                    ans+=1
        return ans
        '''
        
