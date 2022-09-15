from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list) #选用defaultdict的原因是 普通的dict无法对不存在的键做初始化
        for i in strs:
            key = ''.join(sorted(i))
            #每个键下的值以数组的形式返回
            #同时要注意，字典中的键需要保证为不变量即字符串，数字，元组
            mp[key].append(i)  #把相同字母的i存入相同的数组里
        return list(mp.values())













#关于osrted函数返回的问题
# i = 'cat'
# print(sorted(i))
# print(''.join(sorted(i)))


