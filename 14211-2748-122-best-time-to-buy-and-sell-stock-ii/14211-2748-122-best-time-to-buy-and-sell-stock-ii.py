class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[j]:
                profit += prices[j]-prices[i]
            i+=1
            j+=1
        return profit
