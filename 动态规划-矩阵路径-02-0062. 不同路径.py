class Solution(object):
    """
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
说明：m 和 n 的值均不超过 100。
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
输入: m = 7, n = 3
输出: 28
链接：https://leetcode-cn.com/problems/unique-paths
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        opt = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                # opt[j] = opt[j - 1] + opt[j]
                opt[j] += opt[j - 1]
        return opt[-1]


def main():
    m, n = 7, 3  # 28
    test = Solution()
    ret = test.uniquePaths(m, n)
    print(ret)


if __name__ == '__main__':
    main()
