class Solution(object):
    def maxProfit(self, prices):
        
       
        minp = prices[0]
        maxp = 0

        for price in prices:
            if price < minp:
                minp = price
            else:
                profit = price - minp
                if profit > maxp:
                    maxp = profit

        return maxp
    