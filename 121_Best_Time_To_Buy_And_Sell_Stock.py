class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 10000000
        sell = 0
      
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            sell = max(sell, prices[i]-buy)
        return sell


