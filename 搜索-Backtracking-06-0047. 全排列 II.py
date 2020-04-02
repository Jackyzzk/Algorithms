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
    visit = 0

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs():
            if len(pre) == n:
                ret.append(pre[:])
                return
            for i in range(n):
                # 剪枝条件1：用过的元素不能再使用
                # 剪枝条件2：当当前元素和前一个元素值相同，并且前一个元素还没有被使用过的时候，我们要剪枝
                if 1 << i & self.visit:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not (1 << (i - 1) & self.visit):
                    continue
                pre.append(nums[i])
                self.visit |= 1 << i
                dfs()
                pre.pop()
                self.visit ^= 1 << i

        ret, pre = [], []
        nums.sort()
        global n
        n = len(nums)
        dfs()
        return ret


def main():
    nums = [1, 2, 2]
    # nums = [2, 2, 1, 1]  # [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
    nums = [1]
    test = Solution()
    ret = test.permuteUnique(nums)
    print(ret)


if __name__ == '__main__':
    main()
