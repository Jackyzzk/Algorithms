class Solution(object):
    """
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。
输入: [3,4,5,1,2]
输出: 1
输入: [4,5,6,7,0,1,2]
输出: 0
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums) - 1
        if nums[p1] < nums[p2]:
            return nums[p1]
        while p1 < p2 - 1:
            t = (p1 + p2) >> 1
            if nums[t] >= nums[p1]:
                p1 = t
            else:
                p2 = t
        return nums[p2]


def main():
    # nums = [3, 4, 5, 1, 2]
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [2, 1]  # 1
    # nums = [3, 1, 2]  # 1
    # nums = [1, 2]
    test = Solution()
    ret = test.findMin(nums)
    print(ret)


if __name__ == '__main__':
    main()
