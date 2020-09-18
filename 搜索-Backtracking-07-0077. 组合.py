class Solution(object):
    """
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
链接：https://leetcode-cn.com/problems/combinations
    """
    visit = 0

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(pre):
            m = len(rec)
            if m == k:
                ret.append(rec[:])
                return
            # for i in range(pre, n + 1):
            #     if k - m > n + 1 - i:  # 数组内剩下的数的个数不足以满足组合所需求的个数
            #         return
            for i in range(pre, n + 2 + m - k):
                rec.append(i)
                dfs(i + 1)
                rec.pop()

        ret, rec = [], []
        if k <= n:
            dfs(1)
        return ret


def main():
    n, k = 4, 4
    test = Solution()
    ret = test.combine(n, k)
    print(ret)


if __name__ == '__main__':
    main()
