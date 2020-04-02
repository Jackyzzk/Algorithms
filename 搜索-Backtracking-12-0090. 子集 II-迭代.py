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
        ret = [[]]
        nums.sort()
        n = len(nums)
        # 用 aux 来标记上一个数产生新解的起始坐标
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                ret, aux = ret + [ret[j] + [nums[i]] for j in range(aux, len(ret))], len(ret)
            else:
                ret, aux = ret + [t + [nums[i]] for t in ret], len(ret)
        return ret


def main():
    nums = [1, 2, 2, 2]
    test = Solution()
    ret = test.subsetsWithDup(nums)
    print(ret)


if __name__ == '__main__':
    main()
