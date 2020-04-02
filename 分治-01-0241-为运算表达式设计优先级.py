class Solution(object):
    """
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。
你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses/
    """
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def dfs(a, b):
            rec = []
            if b < a:
                return [0]
            for i in range(a, b + 1):
                if input[i] in {'*', '+', '-'}:
                    left = dfs(a, i - 1)
                    right = dfs(i + 1, b)
                    # rec.extend([eval(str(x) + input[i] + str(y)) for x in left for y in right])
                    if input[i] == '+':
                        rec.extend([x + y for x in left for y in right])
                    elif input[i] == '-':
                        rec.extend([x - y for x in left for y in right])
                    else:  # input == '*':
                        rec.extend([x * y for x in left for y in right])
            return rec if rec else [int(input[a:b + 1])]

        n = len(input)
        return dfs(0, n - 1)


def main():
    # input = "2-1-1"
    input = "2*3-4*5"
    # input = "11"
    test = Solution()
    ret = test.diffWaysToCompute(input)
    print(ret)


if __name__ == '__main__':
    main()
