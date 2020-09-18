class Solution(object):
    """
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
输入: 16
输出: true
输入: 5
输出: false
你能不使用循环或者递归来完成本题吗？
链接：https://leetcode-cn.com/problems/power-of-four
    """
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or num & (num - 1):
            return False
        if num & 0b10101010101010101010101010101010:
            return False
        return True


def main():
    num = 64
    test = Solution()
    ret = test.isPowerOfFour(num)
    print(ret)


if __name__ == '__main__':
    main()
