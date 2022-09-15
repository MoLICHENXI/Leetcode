class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        result = 0
        minPrice = prices[0] + fee
        for i in range(1, len(prices)):
            if prices[i] + fee < minPrice:
                minPrice = prices[i] + fee
            elif prices[i] > minPrice:
                result += prices[i] - minPrice
                minPrice = prices[i]
        return result

X = Solution()
print(X.maxProfit([1,5,8,9],2))


