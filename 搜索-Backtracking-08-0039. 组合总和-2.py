class Solution(object):
    """
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
链接：https://leetcode-cn.com/problems/combination-sum
    """
    diff = 0

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(pre):
            for i in range(pre, n):
                if self.diff < candidates[i]:
                    return
                elif self.diff == candidates[i]:
                    ret.append(rec + [candidates[i]])
                else:
                    rec.append(candidates[i])
                    self.diff -= candidates[i]
                    dfs(i)
                    self.diff += candidates[i]
                    rec.pop()

        ret, rec = [], []
        # global n  # 只要在 def 内 n 第一次出现是读取，就自动向外层函数寻找 n
        candidates.sort()
        n = len(candidates)
        self.diff = target
        dfs(0)
        return ret


def main():
    # candidates, target = [2, 3, 6, 7], 7
    # candidates, target = [2, 3, 5], 8
    candidates, target = [8, 7, 4, 3], 11
    test = Solution()
    ret = test.combinationSum(candidates, target)
    print(ret)


if __name__ == '__main__':
    main()
