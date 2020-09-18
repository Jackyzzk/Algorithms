class Solution(object):
    """
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
假设字符串的长度不会超过 1010。
输入:  "abccccdd"
输出:   7
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
链接：https://leetcode-cn.com/problems/longest-palindrome
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        rec, mid = {}, 0
        for x in s:
            rec[x] = rec.get(x, 0) + 1
        for x in rec:
            if rec[x] & 1:
                mid = 1
                rec[x] -= 1
        return sum(rec.values()) + mid


def main():
    s = "abccccdd"
    # s = "cccddddd"
    test = Solution()
    ret = test.longestPalindrome(s)
    print(ret)


if __name__ == '__main__':
    main()
