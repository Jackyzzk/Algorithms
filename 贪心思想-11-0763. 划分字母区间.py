class Solution(object):
    """
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，
同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
输入: S = "ababcbacadefegdehijhklij"
输出: [9,7,8]
解释:
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
注意:
S的长度在[1, 500]之间。
S只包含小写字母'a'到'z'。
链接：https://leetcode-cn.com/problems/partition-labels/
    """
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        rec = [0] * 26  # 记录字母最后出现的坐标
        for i, x in enumerate(S):
            rec[ord(x) - 97] = i
        ret, start, end = [], 0, 0
        for i, x in enumerate(S):
            end = max(end, rec[ord(x) - 97])
            if i == end:
                ret.append(end - start + 1)
                start = i + 1
        return ret


def main():
    S = "ababcbacadefegdehijhklij"
    # S = ''
    test = Solution()
    ret = test.partitionLabels(S)
    print(ret)


if __name__ == '__main__':
    main()
