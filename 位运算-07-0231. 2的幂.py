class Solution(object):
    """
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
输入: 1
输出: true
解释: 2 ** 0 = 1
输入: 16
输出: true
解释: 2 ** 4 = 16
输入: 218
输出: false
链接：https://leetcode-cn.com/problems/power-of-two
    """
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 or n & (n - 1):
            return False
        return True


def main():
    n = 2
    test = Solution()
    ret = test.isPowerOfTwo(n)
    print(ret)


if __name__ == '__main__':
    main()
