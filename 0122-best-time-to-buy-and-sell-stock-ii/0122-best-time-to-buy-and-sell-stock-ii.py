class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        max_profit=0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
               cur_profit=prices[i]-prices[i-1]
               max_profit+=cur_profit
        return max_profit 
        