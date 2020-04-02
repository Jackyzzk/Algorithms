class Solution(object):
    """
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
尽可能多地分解出 3 这个加法因子，就能够使得最终的乘积得到最大。
链接：https://leetcode-cn.com/problems/integer-break
    """
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [0] * (n + 1)
        opt[1], opt[2] = 0, 1
        for i in range(3, n + 1):
            opt[i] = max(opt[i - 1], opt[i - 2] * 2, opt[i - 3] * 3, i - 1, (i - 2) * 2, (i - 3) * 3)
            # 如果opt[i - 3]不大于i - 3的话就不要拆分了
        return opt[n]


def main():
    # n = 8  # 18
    n = 25  # 8748
    test = Solution()
    ret = test.integerBreak(n)
    print(ret)


if __name__ == '__main__':
    main()
