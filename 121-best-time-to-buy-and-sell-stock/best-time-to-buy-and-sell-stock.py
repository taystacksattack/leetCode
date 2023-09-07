class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minPrice = float('inf')
        # minPriceIdx = 0

        # for i in range(len(prices)):
        #     if prices[i] < minPrice: 
        #         minPrice = prices[i]
        #         minPriceIdx = i

        # maxPrice = 0
        # for i in range(minPriceIdx, len(prices)):
        #     if prices[i] > maxPrice: maxPrice = prices[i]

        # return maxPrice - minPrice

        maxNum = 0  

        lp, rp = 0,1

        while rp < len(prices):
            if prices[lp] > prices[rp]:
                lp = rp
            diff = prices[rp] - prices[lp]
            if maxNum < diff: maxNum = diff
            rp += 1

        return maxNum