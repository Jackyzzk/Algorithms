class Solution(object):
    """
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n, m = len(prices), float('-inf')
        hold, sold, rest = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        # rest -> hold -> sold -> rest -> hold，sold 的存在就阻止了 hold -> rest -> hold
        hold[0], sold[0], rest[0] = m, m, 0
        for i in range(1, n + 1):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i - 1])
            sold[i] = hold[i - 1] + prices[i - 1]
            rest[i] = max(rest[i - 1], sold[i - 1])
        return max(sold[-1], rest[-1])


def main():
    prices = [1, 2, 3, 0, 2]
    test = Solution()
    ret = test.maxProfit(prices)
    print(ret)


if __name__ == '__main__':
    main()
