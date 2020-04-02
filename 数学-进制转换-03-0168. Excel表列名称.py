class Solution(object):
    """
给定一个正整数，返回它在 Excel 表中相对应的列名称。
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
输入: 1    输出: "A"
输入: 28   输出: "AB"
输入: 701  输出: "ZY"
链接：https://leetcode-cn.com/problems/excel-sheet-column-title/
    """
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # x = [chr(i) for i in range(65, 91)] 注意 取不到91
        ret = []
        while n > 0:
            n -= 1  # 因为A对应1同时是进制的开始，相当于每一位输出都增加了一个单位量(26^0, 26^1...26^i)
            m = n % 26
            n = n // 26  # n -= 1 真正开始影响整除的就只在临界值发生
            # if m == 0:  # 借位的思想
            #     m = 26
            #     n -= 1
            ret[0:0] = [chr(65 + m)]
        return ''.join(ret)


def main():
    n = 703
    test = Solution()
    ret = test.convertToTitle(n)
    print(ret)


if __name__ == '__main__':
    main()
