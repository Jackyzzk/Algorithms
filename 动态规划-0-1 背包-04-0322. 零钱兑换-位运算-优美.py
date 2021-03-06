class Solution(object):
    """
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
输入: coins = [2], amount = 3
输出: -1
你可以认为每种硬币的数量是无限的。
链接：https://leetcode-cn.com/problems/coin-change
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        mark, count = 1 << amount, 0
        while mark:
            if mark & 1:
                return count
            aux = 0
            for x in coins:
                aux |= mark >> x
            mark = aux
            count += 1
        return -1


def main():
    coins, amount = [1, 2, 5], 11
    # coins, amount = [2, 4, 6], 11
    # coins, amount = [1], 0  # 0
    test = Solution()
    ret = test.coinChange(coins, amount)
    print(ret)


if __name__ == '__main__':
    main()
