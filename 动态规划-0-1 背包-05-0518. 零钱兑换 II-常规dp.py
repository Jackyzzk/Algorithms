class Solution(object):
    """
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
输入: amount = 10, coins = [10]
输出: 1
你可以假设：
0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
链接：https://leetcode-cn.com/problems/coin-change-2
    """
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        opt = [[0] * (amount + 1) for i in range(n + 1)]  # 前 i 种硬币，构成金额为 j 的种数
        opt[0][0] = 1
        for i in range(1, n + 1):
            x = coins[i - 1]
            for j in range(amount + 1):
                if j >= x:
                    opt[i][j] = opt[i - 1][j] + opt[i][j - x]
                else:
                    opt[i][j] = opt[i - 1][j]
        return opt[-1][-1]
        # return opt


def main():
    # amount, coins = 5, [1, 2, 5]
    # amount, coins = 3, [2]
    # amount, coins = 10, [10]
    # amount, coins = 3, [1, 2]
    amount, coins = 500, [1, 2, 5]  # 12701
    test = Solution()
    ret = test.change(amount, coins)
    print(ret)


if __name__ == '__main__':
    main()
