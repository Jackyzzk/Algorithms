class Solution(object):
    """
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
    """
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # rest[0] -> hold[1] -> rest[1] -> ... -> hold[k - 1] -> rest[k - 1] -> hold[k] -> rest[k]
        n = len(prices)
        if 2 * k < n:
            rest = [float('-inf')] * (k + 1)
            hold = [float('-inf')] * (k + 1)
            rest[0] = 0
            for x in prices:
                for t in range(1, k + 1):
                    hold[t], rest[t] = max(hold[t], rest[t - 1] - x), max(rest[t], hold[t] + x)
            return max(rest)
        else:
            rest, hold = 0, float('-inf')
            for x in prices:
                hold, rest = max(hold, rest - x), max(rest, hold + x)
            return rest


def main():
    # prices, k = [3, 2, 6, 5, 0, 3], 2
    prices, k = [2, 4, 1], 20
    test = Solution()
    ret = test.maxProfit(k, prices)
    print(ret)


if __name__ == '__main__':
    main()
