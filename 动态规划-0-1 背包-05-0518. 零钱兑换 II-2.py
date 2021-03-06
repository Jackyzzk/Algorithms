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
        opt = [0] * (amount + 1)
        opt[0] = 1  # opt 表示该硬币以及之前的所有硬币，在 i 空间下的选法总数
        for x in coins:
            for i in range(amount + 1):
                if i >= x:
                    # opt[i] = opt[i] + opt[i - x]
                    opt[i] += opt[i - x]  # 比上面快很多
        return opt[-1]
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
