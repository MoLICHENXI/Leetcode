#第一种是用二维数组dp的情况，遍历顺序有两种方式


# def bagproblem(bag_size, weight, value):
#     # 01背包问题 先创建一个二维数组
#     # 1、dp[i][j]表示当前第i个物品在容量为j的背包所能得到的最大价值
#     # 那么dp数组的大小就应该是len(items) * len(bag_size + 1) 也就是存在dp[i][0]表示背包空间大小为0
#     dp = [[0] * (bag_size + 1) for i in range(len(weight))]
#
#     #2、明确递推公式，dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i] if j >= weight[i])
#     #这个公式是说当前第i个物品在容量为j的大小所能获得的最大价值应该是：如果当前物品i 不能放进背包中，那就是前面i - 1个物品在容量为j的背包中所能得到的最大价值；如果能放进背包中，那就是现在第i个物品的价值加容量为
#     #j - weight[i]的背包中能放进的最大价值
#
#     #3、初始化，第一行在 j < weight[0]的时候都是0，因为当前背包放不下任何内容
#     for j in range(len(dp[0])):
#         if j >= weight[0]:
#             dp[0][j] = value[0]
#
#     #4、遍历顺序，按照每行从左至右遍历以及按照列从上至下遍历均可，因为我们要比较的数字都是在当前位置的左上方
#
#     for i in range(1, len(dp)):
#         for j in range(1, len(dp[0])):
#             if j >= weight[i]:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
#             else:
#                 dp[i][j] = dp[i - 1][j]
#
#     print(dp)


#第二种方法是使用一维的滚动数组

def bagproblem(bag_size, weight, value):
    # 由于是使用一维数组，前面所说的递推公式，dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i] if j >= weight[i])
    # 如果我们把每一行的数组浅拷贝到下一行，那么上述的公式就变为dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    # 明确一维数组dp的意义，i是物品，j是背包容量
    # 在一维dp数组中，dp[j]表示：容量为j的背包，所背的物品价值可以最大为dp[j]。
    # 注意遍历顺序 一维数组遍历顺序是从右至左，因为二维数组中我们从左至右遍历是因为我们需要左上角的值来更新
    # 而在一维数组中，我们如果还按照从左至右的遍历的顺序遍历会导致物品重复放置，，因为我们一维数组中是从本行的左边取，而二维数组是从上一行取，因此一维数组一行的值会不断变化，所以我们需要从右至左遍历保证前面的值不会变化

    #初始化全为0即可，因为我们是需要不断更新当前位置和前面位置的最大值，因此如果价格都是正整数的话我们就初始化全为0
    dp = [0] * (bag_size + 1)
    for i in range(len(weight)):
        for j in range(bag_size, -1, -1):
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
            else:
                dp[j] = dp[j]
    print(dp)

if __name__  == '__main__':
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagproblem(bag_size, weight, value)

