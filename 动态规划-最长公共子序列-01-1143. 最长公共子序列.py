class Solution(object):
    """
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下
删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
若这两个字符串没有公共子序列，则返回 0。
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。
1 <= text1.length <= 1000
1 <= text2.length <= 1000
输入的字符串只含有小写英文字符。
链接：https://leetcode-cn.com/problems/longest-common-subsequence
    """
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1) + 1, len(text2) + 1  # 二维动态规划，第一行第一列代表空
        opt = [[0] * m for i in range(n)]
        # opt[i][j] 代表 text2 以 i-1 结尾的字符串与 text1 以 j-1 结尾的字符串最长公共子序列，属于subproblem
        for i in range(1, n):
            for j in range(1, m):
                if text1[j - 1] == text2[i - 1]:
                    opt[i][j] = 1 + opt[i - 1][j - 1]  # 两个同时去掉相同的最后一位，变成一个已经处理过的子问题
                else:
                    opt[i][j] = max(opt[i - 1][j], opt[i][j - 1])  # 分别去掉最后一位
        return opt[-1][-1]
        # return opt


def main():
    text1, text2 = "abc", "abc"
    # text1, text2 = "bsbininm", "jmjkbkjkv"  # 1
    test = Solution()
    ret = test.longestCommonSubsequence(text1, text2)
    print(ret)
    # for x in ret:
    #     print(x)


if __name__ == '__main__':
    main()
