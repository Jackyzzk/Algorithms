class Solution(object):
    """
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
链接：https://leetcode-cn.com/problems/subsets-ii
    """
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(pre):
            for i in range(pre, n):
                if i > pre and nums[i] == nums[i - 1]:
                    continue
                rec.append(nums[i])
                ret.append(rec[:])
                dfs(i + 1)
                rec.pop()

        ret, rec = [[]], []
        nums.sort()
        n = len(nums)
        dfs(0)
        return ret


def main():
    nums = [1, 2, 2]
    test = Solution()
    ret = test.subsetsWithDup(nums)
    print(ret)


if __name__ == '__main__':
    main()
