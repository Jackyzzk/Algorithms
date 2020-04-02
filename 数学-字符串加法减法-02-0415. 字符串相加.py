class Solution(object):
    """
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
链接：https://leetcode-cn.com/problems/add-strings/
    """
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)
        n1 = len(num1)
        n2 = len(num2)
        n = max(n1, n2) + 1
        num1[0:0] = ['0'] * (n - n1)
        num2[0:0] = ['0'] * (n - n2)
        p = 0
        for i in range(n - 1, -1, -1):
            t = ord(num1[i]) + ord(num2[i]) - ord('0') * 2
            num1[i] = chr((t + p) % 10 + ord('0'))
            p = (t + p) // 10
        if num1[0] == '0':
            num1[0:2] = [num1[1]]
        return ''.join(num1)


def main():
    num1 = '9'
    num2 = '99'
    test = Solution()
    ret = test.addStrings(num1, num2)
    print(ret)


if __name__ == '__main__':
    main()
