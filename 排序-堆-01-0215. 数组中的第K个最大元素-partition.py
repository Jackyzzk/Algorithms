import random


class Solution(object):
    """
在未排序的数组中找到第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
    """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right):
            mid, p2 = random.randint(left, right), left
            nums[mid], nums[left] = nums[left], nums[mid]
            for p1 in range(left + 1, right + 1):
                if nums[p1] < nums[left]:  # pivot = nums[left]
                    p2 += 1
                    nums[p1], nums[p2] = nums[p2], nums[p1]
            nums[left], nums[p2] = nums[p2], nums[left]
            if p2 > k:
                partition(left, p2 - 1)
            elif p2 < k:
                partition(p2 + 1, right)

        k = len(nums) - k
        partition(0, len(nums) - 1)
        return nums[k]


def main():
    nums = [3, 2, 1, 5, 6, 4]
    k = 1
    # nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # k = 4
    # nums = [5, 2, 4, 1, 3, 6, 0]
    # k = 1
    test = Solution()
    ret = test.findKthLargest(nums, k)
    print(ret)


if __name__ == '__main__':
    main()
