class Solution(object):
    """
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
输入: s = "egg", t = "add"
输出: true
输入: s = "foo", t = "bar"
输出: false
输入: s = "paper", t = "title"
输出: true
你可以假设 s 和 t 具有相同的长度。
链接：https://leetcode-cn.com/problems/isomorphic-strings
    """
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def judge(temp):
            aux, rec, i = {}, [], 1
            for x in temp:
                if x not in aux:
                    aux[x] = i
                    i += 1
                rec.append(aux[x])
            return rec

        return judge(s) == judge(t)


def main():
    # s = "paper"
    # t = "title"
    s = "egg"
    t = "adc"
    test = Solution()
    ret = test.isIsomorphic(s, t)
    print(ret)


if __name__ == '__main__':
    main()
