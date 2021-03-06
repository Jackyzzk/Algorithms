class Solution(object):
    """
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
输入: "aba"
输出: True
输入: "abca"
输出: True
解释: 你可以删除c字符。
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
链接：https://leetcode-cn.com/problems/valid-palindrome-ii/
    """
    mark = 0

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            elif not self.mark:
                self.mark = 1
                return self.validPalindrome(s[p1:p2]) or self.validPalindrome(s[p1 + 1:p2 + 1])
            else:
                return False
        return True


def main():
    s = "ebcbbececabbacecbbcbe"
    s = "abcaa"
    test = Solution()
    ret = test.validPalindrome(s)
    print(ret)


if __name__ == '__main__':
    main()
