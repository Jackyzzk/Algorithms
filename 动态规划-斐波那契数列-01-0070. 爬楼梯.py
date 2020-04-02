class Solution(object):
    """
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
链接：https://leetcode-cn.com/problems/climbing-stairs
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [0] * (n + 1)
        opt[0] = opt[1] = 1
        for i in range(2, n + 1):
            opt[i] = opt[i - 2] + opt[i - 1]
        return opt[n]


def main():
    n = 4
    test = Solution()
    ret = test.climbStairs(n)
    print(ret)


if __name__ == '__main__':
    main()
