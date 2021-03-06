class Solution(object):
    """
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
    """
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        rest, hold = 0, float('-inf')
        for x in prices:
            rest, hold = max(rest, hold + x - fee), max(hold, rest - x)
        return rest  # 最大利润的情况一定不是在hold情况下取得


def main():
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    test = Solution()
    ret = test.maxProfit(prices, fee)
    print(ret)


if __name__ == '__main__':
    main()
