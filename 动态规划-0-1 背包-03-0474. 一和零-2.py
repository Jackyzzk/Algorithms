class Solution(object):
    """
在计算机界中，我们总是追求用有限的资源获取最大的收益。
现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
给定 0 和 1 的数量都不会超过 100。
给定字符串数组的长度不会超过 600。
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
        rec = {(0, 0): 0}
        for x in strs:
            a, b, aux = x.count('0'), x.count('1'), {}
            for (u, v), w in rec.items():
                if u + a <= m and v + b <= n and w + 1 > rec.get((u + a, v + b), 0):
                    aux[(u + a, v + b)] = w + 1
            rec.update(aux)
        return max(rec.values())
        # return rec


def main():
    # strs, m, n = {"10", "0001", "111001", "1", "0"}, 5, 3
    # strs, m, n = {"10", "0", "1"}, 1, 1
    # strs, m, n = ['01', '10', '0', '1'], 3, 2
    # strs, m, n = ["10", "0001", "111001", "1", "0"], 3, 4  # 3
    # strs, m, n = ['0', '1', '01'], 1, 1  # (1, 1): 2 , 因为出场顺序 w + 1 有可能比rec里面存在的要小
    strs, m, n = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0",
                  "1", "0", "0110101", "0", "11", "01", "00", "01111", "0011", "1", "1000",
                  "0", "11101", "1", "0", "10", "0111"], 9, 80  # 17
    test = Solution()
    ret = test.findMaxForm(strs, m, n)
    print(ret)


if __name__ == '__main__':
    main()
