class Solution(object):
    """
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
输入: 4
输出: 2
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
链接：https://leetcode-cn.com/problems/sqrtx/
    """
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        p1, p2 = 1, x
        while p1 < p2 - 1:
            t = (p1 + p2) >> 1
            if t * t > x:
                p2 = t  # t不可能是解，所以 p2 也不会是最终的解
            else:
                p1 = t
        return p1


def main():
    # x = 1
    x = 744681054
    # x = 8
    x = 5
    test = Solution()
    ret = test.mySqrt(x)
    print(ret)


if __name__ == '__main__':
    main()
