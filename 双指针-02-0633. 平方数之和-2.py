class Solution(object):
    """
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
输入: 3
输出: False
链接：https://leetcode-cn.com/problems/sum-of-square-numbers
    """
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        root = int(c ** 0.5)
        rec = set()
        for i in range(root + 1):
            rec.add(c - i * i)
            if i * i in rec:
                return True
        return False
        # 33%


def main():
    # c = 2  # True
    c = 3
    test = Solution()
    ret = test.judgeSquareSum(c)
    print(ret)


if __name__ == '__main__':
    main()
