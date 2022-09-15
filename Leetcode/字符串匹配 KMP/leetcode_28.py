# '''
# def strStr(haystack, needle):   #使用的是动态规划的思想，但时间复杂度理论上与暴力解法是一样的
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     List1 = [[0 for i in range(len(haystack))] for j in range(len(needle))]   #创建一个空的二维数组
#     j = 0
#     if len(needle) == None:
#         return 0
#     for j in range(len(haystack)):
#         if haystack[j] == needle[0]:
#             List1[0][j] = 1
#         else:
#             List1[0][j] = 0
#     for i in range(1, len(needle)):
#         if haystack[0] == needle[i]:
#             List1[i][0] = 1
#         for j in range(1, len(haystack)):
#             if haystack[j] == needle[i]:
#                 List1[i][j] = 1 + List1[i - 1][j - 1]
#             else:
#                 List1[i][j] = 0
#     for i in range(len(needle)):
#         for j in range(len(haystack)):
#             #     print(List1[i][j],end='')
#             # print('\n')
#             if List1[i][j] != len(needle):
#                 continue
#             else:
#                 return j - len(needle) + 1
#     return -1
# '''

'''
# 解法二 暴力解法
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if len(needle) == None:
#             return 0
#         for i in range(len(haystack)):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#         return -1
#
# # print([[0 for i in range(5)]for j in range(4)])
# X =Solution()
# haystack = "mississippi"
# needle = "issip"
# X.strStr(haystack,needle)
# print(X.strStr(haystack,needle))
#
#
'''


# '''
#解法三：KMP算法
def next_search(a,needle):  #构造前缀表
    next = ['' for i in range(a)]  #创建一个空的list
    i = 1   #i始终指向needle的后缀部分
    j = 0   #j始终指向needle的前缀部分
    next[0] = 0 #初始化next序列中，第1个位置(index = 0)的最大相同前后缀长度为0
    for i in range(1,len(needle)):
        while j > 0 and needle[i] != needle[j]:   #首先，必须保证j 是大于0的，因为后面是需要用到j的前一位j-1对应的最长前后缀长度
            j = next[j - 1]    #如果当前位置是不相同的，根据KMP思想，就把回到前面匹配好的前缀部分，也就是回到j -1 位的next数组中记录的对应位置的最长前缀长度
                               #回到该位置后，以ababacab为例   i = 5 的时候对应位置为'c'，此时j = 3，对应为'b'，因为此时不相等，开始回到j = 2，也就是前一位记录的最长前后缀长度
                               #next[2] = 1，表示 aba中，最长的前后缀为a,所以abac当比较到'abac'的c时，可以从第一个'a'(记录的前缀)开始再次比较，发现'ab'与'ac'还是不一样，那么再往前继续回溯
                               #只到j=0,表示就是没有相同的前缀了，那么可以放弃此时的i 值 表示前面没有与之类似的，从i + 1继续开始重新比较
        if needle[i] == needle[j]:  #这里已经包含了i = 1, j = 0相同的时候
            j += 1          #如果当前位置的后缀和前缀是相同的，就把指向前缀的j也向后移位
            next[i] = j     #j在这里就正好是前面相同部分的长度  #因此在这里就把记录needle中i位置的部分填上相同的长度 (j)
        next[i] = j         #这里考虑的就是i=1 ,j=0且不相同的情况，例如abac串，next[1]是需要标记为0的
    return next

# print(next_search(8,'ababacab'))
def strStr(haystack,needle):
    a = len(needle)
    if a == 0:
        return 0
    next = next_search(a,needle) #先找到needle的前缀表,即NEXT
    # print(next)
    #找到前缀表后，开始对本问题进行求解，无非就是跟前缀表思路类似，发现不匹配的时候，利用前缀表回溯，只到前缀表指向的j = 0，表示没有前缀，结束通过j是否达到needle的长度来判断
    j = 0 #needle的标志
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]: #与next里面类似，j大于0 要求是因为j-1必须有意义
            j = next[j - 1]    #回到上一位前缀表指向的最长前缀位置
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - j + 1
    return -1

haystack = "mississippi"
needle = "issip"
print(strStr(haystack,needle))


# '''

