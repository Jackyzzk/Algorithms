class Solution(object):
    """
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # rest0 -> hold1 -> rest1 -> hold2 -> rest2
        rest0 = 0
        hold1 = rest1 = hold2 = rest2 = float('-inf')
        for x in prices:
            hold1, rest1, hold2, rest2 = max(hold1, rest0 - x), max(rest1, hold1 + x), \
                                         max(hold2, rest1 - x), max(rest2, hold2 + x)
        return max(0, rest1, rest2)


def main():
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    prices = [1, 2, 3]
    # prices = [0]
    # prices = [7, 6, 4, 3, 1]
    # prices = [6, 1, 3, 2, 4, 7]  # 7
    # prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]  # 13
    test = Solution()
    ret = test.maxProfit(prices)
    print(ret)
    # for x in ret:
    #     print(x)

if __name__ == '__main__':
    main()
