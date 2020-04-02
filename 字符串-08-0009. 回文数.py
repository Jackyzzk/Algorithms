class Solution(object):
    """
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
输入: 121
输出: true
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？
链接：https://leetcode-cn.com/problems/palindrome-number
    """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        t, m = 0, x
        while m:
            t = m % 10 + t * 10
            m = m // 10
        return t == x


def main():
    x = 1221
    test = Solution()
    ret = test.isPalindrome(x)
    print(ret)


if __name__ == '__main__':
    main()
