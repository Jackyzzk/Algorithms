class Solution(object):
    """
给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
输入: 5
输出: True
解释: 5的二进制数是: 101
输入: 7
输出: False
解释: 7的二进制数是: 111
输入: 11
输出: False
解释: 11的二进制数是: 1011
输入: 10
输出: True
解释: 10的二进制数是: 1010
链接：https://leetcode-cn.com/problems/binary-number-with-alternating-bits
    """
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = n ^ (n >> 1)  # n 是交错的话，t就是一串 1
        if t & (t + 1):  # t & (t + 1) 在判断 t 是不是一串 1 的时候有固定返回 0
            return False
        return True


def main():
    n = 10
    test = Solution()
    ret = test.hasAlternatingBits(n)
    print(ret)


if __name__ == '__main__':
    main()
