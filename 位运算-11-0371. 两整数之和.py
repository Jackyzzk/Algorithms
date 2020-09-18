class Solution(object):
    """
不使用运算符 + 和 - ，计算两整数 a 、b 之和。
输入: a = 1, b = 2
输出: 3
输入: a = -2, b = 3
输出: 1
链接：https://leetcode-cn.com/problems/sum-of-two-integers
    """
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a < 0 < b < abs(a) or b < 0 < a < abs(b) or a * b > 0:
            mark = True
        else:
            mark = False
        while b & 0xffffffff:
            a, b = a ^ b, (a & b) << 1
        return a if mark else a & 0xffffffff


def main():
    a, b = 2, -1
    a, b = 2147483647, -2147483648
    test = Solution()
    ret = test.getSum(a, b)
    print(ret)


if __name__ == '__main__':
    main()
