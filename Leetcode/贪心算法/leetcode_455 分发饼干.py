class Solution:
    def findContentChildren(self, g, s) -> int:
        #先排序
        g.sort()
        s.sort()
        cnt = 0

        #从后往前看
        i = len(g) - 1 #最后一个小孩子 胃口最大
        j = len(s) - 1 #最后一块最大的饼干
        while j >=0 and i >= 0:
            if s[j] >= g[i]:
                cnt += 1
                j -= 1
                i -= 1
            else:
                i -= 1
        return cnt

X = Solution()
print((X.findContentChildren([1,2],[1,2,3])))