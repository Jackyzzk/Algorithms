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
        # palindrome /ˈpælɪndroʊm/ n. 回文
        # 马拉车算法的关键之处，就在于巧妙的应用了回文字符串的性质，来计算数组 pal。
        # 可以不用每次都从 i 点来向两边扩展。利用前面算好的回文串长度来优化当前回文串长度的查找
        # left -> p1 -> center -> p2 -> right，中心对称

        s = '^#' + '#'.join(s) + '#$'
        n = len(s)
        pal = [0] * n
        center = right = 0
        for i in range(1, n - 1):
            if i < right:  # 等于 right 的时候，下面的 min 中的 right - i 依然会取到默认的 0
                pal[i] = min(pal[2 * center - i], right - i)
            while s[i - pal[i] - 1] == s[i + pal[i] + 1]:  # ^ $ 总能让循环停下来以至于不会越界
                pal[i] += 1
            if i + pal[i] > right:  # 比 if i > right: 快很多，要及时更新对称中心
                center, right = i, i + pal[i]
        return sum(x >> 1 for x in pal) + (n >> 1) - 1


def main():
    # s = "aaa"
    s = 'abc'
    # s = "fdsklf"  # 6
    test = Solution()
    ret = test.countSubstrings(s)
    print(ret)


if __name__ == '__main__':
    main()
