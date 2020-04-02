class Solution(object):
    """
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
所有数字都是正整数。
解集不能包含重复的组合。 
输入: k = 3, n = 7
输出: [[1,2,4]]
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
链接：https://leetcode-cn.com/problems/combination-sum-iii
    """
    diff = 0

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(pre):
            for x in range(pre, 10):
                if self.diff < x or len(rec) > k:
                    return
                elif self.diff == x:
                    if len(rec) + 1 == k:
                        ret.append(rec + [x])
                    return
                else:
                    rec.append(x)
                    self.diff -= x
                    dfs(x + 1)
                    rec.pop()
                    self.diff += x

        ret, rec = [], []
        self.diff = n
        dfs(1)
        return ret


def main():
    k, n = 3, 7
    # k, n = 3, 9
    # k, n = 2, 18  # []
    test = Solution()
    ret = test.combinationSum3(k, n)
    print(ret)


if __name__ == '__main__':
    main()
