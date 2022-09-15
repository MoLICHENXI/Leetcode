class Solution:
    def candy(self, ratings) -> int:
        candy = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candy[i + 1] = candy[i] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(ratings[i + 1] + 1, candy[i])
        return sum(candy)
X = Solution()
print(X.candy([1,0,2]))