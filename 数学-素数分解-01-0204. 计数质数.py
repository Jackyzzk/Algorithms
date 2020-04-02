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
        # 最小的质数是 2
        if n < 2:
            return 0
        x = [1] * n  # 比 x = [1 for i in range(n)] 使用了for更快
        x[0] = x[1] = 0
        for i in range(2, int(n ** 0.5) + 1):  # 避免了使用sqrt
            if x[i]:
                x[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)  # 从i^2到(n-1)间隔为i有几个数，(末-首)/步长 + 1
                # 切片不是生成新的列表，而是构建原列表的引用
                # len(x[i * i: n: i])用这个求个数也可以
        return sum(x)


def main():
    n = 10
    test = Solution()
    ret = test.countPrimes(n)
    print(ret)


if __name__ == '__main__':
    main()
