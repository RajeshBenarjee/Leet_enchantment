class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        profit=0
        n=len(prices)
        for i in range(1,n):
            buy=prices[i]
            curr=buy-min_price
            profit=max(profit,curr)
            min_price=min(min_price,buy)
        return profit