class Solution(object):
    """
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。
输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
输出:
"apple"
输入:
s = "abpcplea", d = ["a","b","c"]
输出:
"a"
说明:
所有输入的字符串只包含小写字母。
字典的大小不会超过 1000。
所有输入的字符串长度不会超过 1000。
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/
    """
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x: (-len(x), x))
        for x in d:
            i, n = 0, len(x)
            for t in s:
                if t == x[i]:
                    i += 1
                    if i == n:
                        return x
        return ''


def main():
    s = "abpcplea"
    s = "bab"
    d = ["ba", "ab", "a", "b"]
    # d = ["a", "b", "c"]
    # d = ["ale", "apple", "monkey", "plea"]
    # s = "apple"
    # d = ["zxc", "vbn"]
    test = Solution()
    ret = test.findLongestWord(s, d)
    print(ret)


if __name__ == '__main__':
    main()


