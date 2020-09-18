class Solution(object):
    """
给定一个可包含重复数字的序列，返回所有不重复的全排列。
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
链接：https://leetcode-cn.com/problems/permutations-ii/
    """
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def swap(start, t):
            nums[start:] = [nums[t]] + nums[start:t] + nums[t + 1:]

        def back(start, t):
            nums[start:] = nums[start + 1:t + 1] + [nums[start]] + nums[t + 1:]

        def dfs(start=0):
            if start == n:
                ret.append(nums[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                swap(start, i)
                dfs(start + 1)
                back(start, i)

        ret = []
        n = len(nums)
        nums.sort()
        dfs()
        return ret


def main():
    nums = [1, 2, 2]
    nums = [2, 2, 1, 1]  # [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
    # nums = [1]
    nums = [0, 1, 0, 0, 9]  # 09010 重复
    # [[0,0,0,1,9],[0,0,0,9,1],[0,0,1,0,9],[0,0,1,9,0],[0,0,9,0,1],[0,0,9,1,0],[0,1,0,0,9],
    # [0,1,0,9,0],[0,1,9,0,0],[0,9,0,0,1],[0,9,0,1,0],[0,9,1,0,0],[1,0,0,0,9],[1,0,0,9,0],
    # [1,0,9,0,0],[1,9,0,0,0],[9,0,0,0,1],[9,0,0,1,0],[9,0,1,0,0],[9,1,0,0,0]]
    # nums = [0, 1, 0, 0, 2]
    test = Solution()
    ret = test.permuteUnique(nums)
    print(ret)


if __name__ == '__main__':
    main()
