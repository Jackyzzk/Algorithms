class Solution(object):
    """
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
输入: a = "11",    b = "1"      输出: "100"
输入: a = "1010",  b = "1011"   输出: "10101"
链接：https://leetcode-cn.com/problems/add-binary/
    """
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = len(a)
        n2 = len(b)
        n = max(n1, n2)
        a = list('0' * (n - n1 + 1) + a)
        b = list('0' * (n - n2 + 1) + b)
        p = 0
        for i in range(n, -1, -1):
            t = int(a[i]) + int(b[i])
            a[i] = str((t + p) % 2)
            p = (t + p) // 2
        if a[0] == '0':
            a[0:2] = [a[1]]
        return ''.join(a)


def main():
    a = "1010"
    b = "1011"
    test = Solution()
    ret = test.addBinary(a, b)
    print(ret)


if __name__ == '__main__':
    main()
