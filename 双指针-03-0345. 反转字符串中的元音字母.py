class Solution(object):
    """
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
输入: "hello"
输出: "holle"
输入: "leetcode"
输出: "leotcede"
元音字母不包含字母"y"。
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string/
    """
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            if s[p1] not in yuan:
                p1 += 1
            elif s[p2] not in yuan:
                p2 -= 1
            else:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
        return ''.join(s)


def main():
    s = 'aA'
    s = "leetcode"
    test = Solution()
    ret = test.reverseVowels(s)
    print(ret)


if __name__ == '__main__':
    main()