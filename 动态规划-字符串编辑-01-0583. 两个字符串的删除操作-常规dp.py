class Solution(object):
    """
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，
每步可以删除任意一个字符串中的一个字符。
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
给定单词的长度不超过500。
给定单词中的字符只含有小写字母。
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
    """
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1, n2 = len(word1), len(word2)
        opt = [[0] * (n2 + 1) for i in range(n1 + 1)]
        # word1 前 i 个与 word2 前 j 个相同的个数
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    opt[i][j] = opt[i - 1][j - 1] + 1
                else:
                    opt[i][j] = max(opt[i - 1][j], opt[i][j - 1])
        return n1 + n2 - 2 * opt[-1][-1]


def main():
    w1, w2 = "sea", "eat"
    test = Solution()
    ret = test.minDistance(w1, w2)
    print(ret)


if __name__ == '__main__':
    main()
