class Solution(object):
    """
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
链接：https://leetcode-cn.com/problems/house-robber
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n < 3:
            return max(nums)
        opt = [0] * n
        opt[0], opt[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            opt[i] = max(opt[i - 1], nums[i] + opt[i - 2])
        return opt[n - 1]


def main():
    nums = [2, 7, 9, 3, 1]  # 12
    # nums = [1, 2, 3, 1]
    # nums = []
    # nums = [1]
    # nums = [2, 1, 1, 2]  # 4
    test = Solution()
    ret = test.rob(nums)
    print(ret)


if __name__ == '__main__':
    main()
