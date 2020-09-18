class Solution(object):
    """
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
输入: "aab"
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
        def judge(p1, p2):
            while p1 < p2:
                if s[p1] == s[p2]:
                    p1 += 1
                    p2 -= 1
                else:
                    return False
            return True

        def dfs(pre):
            if pre == n:
                ret.append(rec[:])
                return
            for i in range(pre, n):
                if judge(pre, i):
                    rec.append(s[pre:i + 1])
                    dfs(i + 1)
                    rec.pop()

        ret, rec = [], []
        n = len(s)
        dfs(0)
        return ret


def main():
    s = "ababa"
    test = Solution()
    ret = test.partition(s)
    print(ret)


if __name__ == '__main__':
    main()
