class Solution(object):
    """
统计所有小于非负整数 n 的质数的数量。
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
链接：https://leetcode-cn.com/problems/count-primes/
    """
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        x = [1 for i in range(n)]  # 标记，1就是质数
        x[0] = x[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if x[i]:
                for j in range(i, (n - 1) // i + 1):
                    x[i * j] = 0
        return sum(x)


def main():
    n = 8
    test = Solution()
    ret = test.countPrimes(n)
    print(ret)


if __name__ == '__main__':
    main()
