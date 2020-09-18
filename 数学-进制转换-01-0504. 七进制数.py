class Solution(object):
    """
给定一个整数，将其转化为7进制，并以字符串形式输出。
输入: 100
输出: "202"
输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
链接：https://leetcode-cn.com/problems/base-7/
    """
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        mark = 0
        if num < 0:
            num = -num
            mark = 1
        elif num == 0:
            return str(0)
        x = []
        while num > 0:
            m = num % 7
            num = num // 7  # 比 num //= 7 快一点，但是更耗空间
            x[0:0] = [str(m)]
        if mark:
            return '-' + ''.join(x)
        else:
            return ''.join(x)


def main():
    num = 100
    test = Solution()
    ret = test.convertToBase7(num)
    print(ret)


if __name__ == '__main__':
    main()
