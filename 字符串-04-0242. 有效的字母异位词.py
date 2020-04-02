class Solution(object):
    """
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
输入: s = "anagram", t = "nagaram"
输出: true
输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
链接：https://leetcode-cn.com/problems/valid-anagram
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        aux1, aux2 = {}, {}
        for x in s:
            aux1[x] = aux1.get(x, 0) + 1
        for x in t:
            aux2[x] = aux2.get(x, 0) + 1
        return aux1 == aux2


def main():
    # s = "anagram"
    # t = "nagaram"
    s = "rat"
    t = "car"
    test = Solution()
    ret = test.isAnagram(s, t)
    print(ret)


if __name__ == '__main__':
    main()
