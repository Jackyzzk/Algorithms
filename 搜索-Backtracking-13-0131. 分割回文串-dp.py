class Solution(object):
    """
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
链接：https://leetcode-cn.com/problems/palindrome-partitioning
    """
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(pre):
            if pre == n:
                ret.append(rec[:])
                return
            for i in range(pre, n):
                if opt[pre][i]:
                    rec.append(s[pre:i + 1])
                    dfs(i + 1)
                    rec.pop()

        ret, rec = [], []
        n = len(s)
        opt = [[1] * n for i in range(n)]
        # opt[i][j] 表示 s[i] ~ s[j] 是不是回文串
        for i in range(n - 2, -1, -1):  # n - 2 与 n - 1 效果一样
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    opt[i][j] = opt[i + 1][j - 1]
                else:
                    opt[i][j] = 0
        dfs(0)
        return ret


def main():
    s = "aab"
    s = "abbab"
    test = Solution()
    ret = test.partition(s)
    print(ret)


if __name__ == '__main__':
    main()
