class Solution(object):
    """
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
1      2abc  3def
4ghi   5jkl  6mno
7pqrs  8tuv  9wxyz
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # ord('2') = 50, ord('a') = 97, ord('9') = 57, ord('z') = 122
        # alphabet, cur = {}, 97
        # for i in range(8):
        #     k = 1 if i == 5 or i == 7 else 0
        #     alphabet[chr(50 + i)] = [chr(cur + j) for j in range(3 + k)]
        #     cur += 3 + k
        if not digits:
            return []
        alphabet = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        ret = ['']
        for k in digits:
            ret = [x + y for x in ret for y in alphabet[k]]
        return ret


def main():
    digits = '23'
    test = Solution()
    ret = test.letterCombinations(digits)
    print(ret)


if __name__ == '__main__':
    main()
