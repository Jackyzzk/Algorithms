class Solution(object):
    """
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
链接：https://leetcode-cn.com/problems/edit-distance
    """
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # diagonal  up
        #   left   cur
        n1, n2 = len(word1), len(word2)
        opt = [i for i in range(n1 + 1)]
        diagonal = 0
        for x in word2:
            for i in range(n1 + 1):
                if i == 0:
                    opt[i], diagonal = opt[i] + 1, opt[i]
                elif word1[i - 1] == x:
                    opt[i], diagonal = diagonal, opt[i]
                else:
                    opt[i], diagonal = min(opt[i], opt[i - 1], diagonal) + 1, opt[i]  # 插入，删除，替换
        return opt[-1]


def main():
    w1 = "intention"
    w2 = "execution"
    # w1 = "inten"
    # w2 = "e"
    # w1 = "horse"
    # w2 = "ros"
    test = Solution()
    ret = test.minDistance(w1, w2)
    print(ret)


if __name__ == '__main__':
    main()
