class Solution(object):
    """
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。
给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。
输入: 5
输出: 2
解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
输入: 1
输出: 0
解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
链接：https://leetcode-cn.com/problems/number-complement
    """
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1 << 31
        while not num & mask:
            mask >>= 1  # 找到最高位的 1 和它的位
        mask = (mask << 1) - 1  # 左移 1 位减 1 完成掩码构造
        return num ^ mask



def main():
    num = 5
    test = Solution()
    ret = test.findComplement(num)
    print(ret)


if __name__ == '__main__':
    main()
