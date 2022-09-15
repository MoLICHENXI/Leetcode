class Solution:
    def partitionLabels(self, s: str):
        record = [0] * 26
        # 记录每个字母最后出现的位置
        for idx, i in enumerate(s):
            record[ord(i) - ord('a')] = idx

        res = []
        start, end = 0, 0
        for idx, i in enumerate(s):
            end = max(end, record[ord(i) - ord('a')])
            if idx == end:
                res.append(end - start + 1)
                start = end + 1
        return res
X = Solution()
print(X.partitionLabels("ababcbacadefegdehijhklij"))