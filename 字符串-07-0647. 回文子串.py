class Solution(object):
    """
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
输入的字符串长度不会超过1000。
链接：https://leetcode-cn.com/problems/palindromic-substrings
    """
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, count = len(s), 0
        opt = [[1] * n for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    opt[i][j] = opt[i + 1][j - 1]
                    if opt[i][j]:
                        count += 1
                else:
                    opt[i][j] = 0
        return count + n


def main():
    s = "aaa"
    s = 'abc'
    s = "fdsklf"  # 6
    test = Solution()
    ret = test.countSubstrings(s)
    print(ret)


if __name__ == '__main__':
    main()
