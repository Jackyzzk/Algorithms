class Solution(object):
    """
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
链接：https://leetcode-cn.com/problems/combination-sum-ii
    """
    diff = 0

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(pre):
            for i in range(pre, n):
                if i > pre and candidates[i] == candidates[i - 1]:
                    continue
                if self.diff < candidates[i]:
                    continue
                elif self.diff == candidates[i]:
                    ret.append(rec + [candidates[i]])
                else:
                    self.diff -= candidates[i]
                    rec.append(candidates[i])
                    dfs(i + 1)
                    rec.pop()
                    self.diff += candidates[i]

        ret, rec = [], []
        n = len(candidates)
        self.diff = target
        candidates.sort()
        dfs(0)
        return ret


def main():
    candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
    # candidates, target = [2, 5, 2, 1, 2], 5
    test = Solution()
    ret = test.combinationSum2(candidates, target)
    print(ret)


if __name__ == '__main__':
    main()
