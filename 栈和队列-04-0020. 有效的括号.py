class Solution(object):
    """
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
输入: "()"       输出: true
输入: "()[]{}"   输出: true
输入: "(]"       输出: false
输入: "([)]"     输出: false
输入: "{[]}"     输出: true
链接：https://leetcode-cn.com/problems/valid-parentheses
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rec = [0]
        aux = {'(': 1, ')': 2, '[': 3, ']': 4, '{': 5, '}': 6}
        for x in s:
            if aux[x] & 1:
                rec.append(aux[x])
            elif aux[x] - rec[-1] == 1:
                rec.pop()
            else:
                return False
        return rec[-1] == 0


def main():
    s = "{[]}"
    # s = "([)]"
    s = "()[]{}"
    # s = "(]"
    # s = '['
    test = Solution()
    ret = test.isValid(s)
    print(ret)


if __name__ == '__main__':
    main()
