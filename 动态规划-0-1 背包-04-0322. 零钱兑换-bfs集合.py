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
硬币可以重复使用，因此这是一个完全背包问题。
链接：https://leetcode-cn.com/problems/coin-change
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        que, aux, count = {0}, set(), 0
        while que:
            x = que.pop()
            if x == amount:
                return count
            for t in coins:
                if x + t < amount:
                    # aux |= {x + t}
                    aux.add(x + t)  # 比上面的 aux |= {x + t} 快很多
                elif x + t == amount:
                    return count + 1
            if not que:
                que, aux = aux, que
                count += 1
        return -1
        # 2940 ms	13.7 MB


def main():
    coins, amount = [1, 2, 5], 11
    # coins, amount = [2, 4, 6], 11
    # coins, amount = [1], 0  # 0
    test = Solution()
    ret = test.coinChange(coins, amount)
    print(ret)


if __name__ == '__main__':
    main()
