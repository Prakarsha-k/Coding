class Solution(object):
    def maxProfit(self, prices):
        maxprofit=0
        min_price=max(prices)
        if len(prices)==0:
            return 0
        for price in prices:
            if price<min_price:
                min_price=price     
            elif price-min_price>maxprofit:
                maxprofit=price-min_price
        return maxprofit