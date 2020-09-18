class Solution(object):
    """
给定一个整数 n，返回 n! 结果尾数中零的数量。
输入: 3  输出: 0  解释: 3! = 6, 尾数中没有零。
输入: 5  输出: 1  解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes/
    """
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n = n // 5
            count += n
        return count


def main():
    # n = 200  # 49
    n = 15
    test = Solution()
    ret = test.trailingZeroes(n)
    print(ret)


if __name__ == '__main__':
    main()
