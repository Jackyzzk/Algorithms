class Solution(object):
    """
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；
对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
输入: 26
输出: "1a"
输入: -1
输出: "ffffffff"
正整数的补码是其二进制表示，与原码相同
求负整数的补码，将其原码除符号位外的所有位取反（0变1，1变0，符号位为1不变）后加1
已知一个数的补码，求原码的操作其实就是对该补码再求补码
链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/
    """
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num = 2 ** 32 + num
        elif num == 0:
            return '0'
        x = []
        elem = ['a', 'b', 'c', 'd', 'e', 'f']
        while num > 0:
            m = num % 16
            num = num // 16
            if m < 10:
                x[0:0] = [str(m)]
            else:
                x[0:0] = [elem[m % 10]]
        return ''.join(x)


def main():
    num = -1
    test = Solution()
    ret = test.toHex(num)
    print(ret)


if __name__ == '__main__':
    main()
