class Solution:
    def findAnagrams(self, s: str, p: str):
        record = [0] * 26
        lst = list()
        for i in p:
            record[ord(i) - ord('a')] += 1
        slow, fast = 0, 0
        for slow in range(len(s)):
            flag = record[:]    #复制一个新的数组
            for fast in s[slow:slow+len(p)]:
                flag[ord(fast) - ord('a')] -= 1
            if flag == [0] *26:
                lst.append(slow)
        return lst

