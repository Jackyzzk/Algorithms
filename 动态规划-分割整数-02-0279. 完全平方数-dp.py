class Solution(object):
    """
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
链接：https://leetcode-cn.com/problems/perfect-squares
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [min(i, 4) for i in range(n + 1)]
        root = int(n ** 0.5)
        for i in range(4, n + 1):
            for j in range(1, root + 1):
                if i <= 3 * j * j:
                    opt[i] = min(opt[i], opt[i - j * j] + 1)
                    # 第二项的意思是 i 可以表示为 j * j + (i - j * j)，后面的 1 是 j * j 的那一个
        return opt[n]


def main():
    n = 12
    test = Solution()
    ret = test.numSquares(n)
    print(ret)


if __name__ == '__main__':
    main()
