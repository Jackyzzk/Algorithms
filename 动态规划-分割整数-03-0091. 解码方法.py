class Solution(object):
    """
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
链接：https://leetcode-cn.com/problems/decode-ways
    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        n = len(s)
        opt = [1] * n
        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    opt[i] = opt[i - 2]
                else:
                    return 0
            elif '0' < s[i] < '7':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    opt[i] = opt[i - 1] + opt[i - 2]
                else:
                    opt[i] = opt[i - 1]
            else:  # '7' <= s[i] <= '9'
                if s[i - 1] == '1':
                    opt[i] = opt[i - 1] + opt[i - 2]
                else:
                    opt[i] = opt[i - 1]
        return opt[-1]


def main():
    # s = '0'  # 0
    s = '27'  # 1
    s = '01'  # 0
    test = Solution()
    ret = test.numDecodings(s)
    print(ret)


if __name__ == '__main__':
    main()
