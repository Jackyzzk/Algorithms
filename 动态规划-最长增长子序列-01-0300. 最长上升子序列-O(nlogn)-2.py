class Solution(object):
    """
给定一个无序的整数数组，找到其中最长上升子序列的长度。
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
    """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        opt, n = [nums[0]], len(nums)

        for x in nums:
            if x > opt[-1]:
                opt[n:n] = [x]
            else:
                p1, p2 = 0, len(opt) - 1
                while p1 < p2:
                    mid = (p1 + p2) >> 1
                    if opt[mid] < x:
                        p1 = mid + 1
                    elif opt[mid] > x:
                        p2 = mid
                    else:
                        p2 = mid
                        break
                opt[p2] = x
        return len(opt)


def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = []
    # nums = [2, 2]
    # nums = [4, 10, 4, 3, 8, 9]
    test = Solution()
    ret = test.lengthOfLIS(nums)
    print(ret)


if __name__ == '__main__':
    main()
