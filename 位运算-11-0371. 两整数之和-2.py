class Solution(object):
    """
不使用运算符 + 和 - ，计算两整数 a 、b 之和。
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
        a &= 0xff
        b &= 0xff
        while b:
            carry = a & b
            a ^= b
            b = (carry << 1) & 0xff
            # print((a, b))
        return a if a < 0x80 else ~(a ^ 0xff)



def main():
    a, b = -6, 5
    test = Solution()
    ret = test.getSum(a, b)
    print(ret)


if __name__ == '__main__':
    main()
