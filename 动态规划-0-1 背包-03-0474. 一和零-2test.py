class Solution(object):
    """
在计算机界中，我们总是追求用有限的资源获取最大的收益。
现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
给定 0 和 1 的数量都不会超过 100。
给定字符串数组的长度不会超过 600。
输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
输出: 4
解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
输入: Array = {"10", "0", "1"}, m = 1, n = 1
输出: 2
解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
链接：https://leetcode-cn.com/problems/ones-and-zeroes
    """
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        opt = [[0] * (n + 1) for i in range(m + 1)]
        for x in strs:
            a, b = x.count('0'), x.count('1')
            if a > m or b > n:
                continue
            for i in range(m, a - 1, -1):
                for j in range(n, b - 1, -1):
                    opt[i][j] = max(opt[i][j], opt[i - a][j - b] + 1)
        return opt[-1][-1]


def main():
    # strs, m, n = {"10", "0001", "111001", "1", "0"}, 5, 3
    # strs, m, n = {"10", "0", "1"}, 1, 1
    # strs, m, n = {'1'}, 0, 1
    # strs, m, n = ["10", "0001", "111001", "1", "0"], 3, 4  # 3
    strs, m, n = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0",
                  "1", "0", "0110101", "0", "11", "01", "00", "01111", "0011", "1", "1000",
                  "0", "11101", "1", "0", "10", "0111"], 9, 80  # 17
    test = Solution()
    ret = test.findMaxForm(strs, m, n)
    print(ret)


if __name__ == '__main__':
    main()
