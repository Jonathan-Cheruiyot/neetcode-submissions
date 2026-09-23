class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Choose a day where the prices of the coin is going to give you the max result
        # If there is no day that seems profitable to you, you can choose not to get any profit
        maxProfit = 0
        minPrice = prices[0]

        for sell in prices: 
            maxProfit = max(maxProfit, sell - minPrice)
            minPrice = min(minPrice, sell)
        return maxProfit
