class Solution(object):
    """
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，
并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
请注意，一些重复出现的子串要计算它们出现的次数。
另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
s.length 在1到50,000之间。
s 只包含“0”或“1”字符。
链接：https://leetcode-cn.com/problems/count-binary-substrings
    """
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        t = 1  # 0或者1 单独的个数
        while t * 2 <= n:
            aux = 0
            for i in range(n - t):
                if s[i] != s[i + t]:
                    aux += 1
                else:
                    count += aux // t
                    aux = 0
            count += aux // t
            t += 1
        return count


def main():
    # s = "00110011"
    # s = "10101"
    # s = "01"
    s = "100111001"  # 6
    test = Solution()
    ret = test.countBinarySubstrings(s)
    print(ret)


if __name__ == '__main__':
    main()
