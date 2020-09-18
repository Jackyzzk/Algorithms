class Solution(object):
    """
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    """
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search_left(p1, p2, k):
            while p1 < p2:
                t = (p1 + p2) >> 1
                if nums[t] < k:
                    p1 = t + 1
                else:
                    p2 = t
            return p2

        if not nums or target > nums[-1] or target < nums[0]:
            return [-1, -1]
        p1, p2 = 0, len(nums) - 1
        left = search_left(p1, p2, target)
        if nums[left] != target:
            return [-1, -1]
        # 将寻找 target 最后一个位置，转换成寻找 target+1 第一个位置，再往前移动一个位置
        right = search_left(p1, p2, target + 1)
        if nums[right] != target:
            right -= 1
        return [left, right]


def main():
    # nums, target = [5, 7, 7, 8, 8, 10], 8
    # nums, target = [1, 3, 3, 4, 5, 5, 5], 2
    # nums, target = [2, 2, 2, 2, 2, 2, 2], 2
    nums, target = [0, 0, 1, 2, 3, 3, 4], 4
    test = Solution()
    ret = test.searchRange(nums, target)
    print(ret)


if __name__ == '__main__':
    main()
