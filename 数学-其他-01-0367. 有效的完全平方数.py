class Solution(object):
    """
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
说明：不要使用任何内置的库函数，如  sqrt。
输入：16
输出：True
输入：14
输出：False
二分查找
链接：https://leetcode-cn.com/problems/valid-perfect-square/
    """
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        p1 = 2
        p2 = num // 2
        while p1 < p2 - 1:
            t = (p1 + p2) // 2
            if t * t < num:
                p1 = t
            else:
                p2 = t
        if p2 * p2 == num:
            return True
        return False


def main():
    num = 25
    test = Solution()
    ret = test.isPerfectSquare(num)
    print(ret)


if __name__ == '__main__':
    main()
