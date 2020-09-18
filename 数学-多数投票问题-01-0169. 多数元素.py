import random

class Solution(object):
    """
给定一个大小为 n 的数组，找到其中的多数元素。
多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
输入: [3,2,3]
输出: 3
输入: [2,2,1,1,1,2,2]
输出: 2
链接：https://leetcode-cn.com/problems/majority-element/
    """
    def quick_seek(self, nums, left, right):
        mid = random.randint(left, right)
        nums[mid], nums[left] = nums[left], nums[mid]
        pivot = nums[left]
        p2 = left
        for p1 in range(left + 1, right + 1):
            if nums[p1] < pivot:
                p2 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
        nums[left], nums[p2] = nums[p2], nums[left]
        if p2 > n // 2:
            self.quick_seek(nums, left, p2 - 1)
        elif p2 < n // 2:
            self.quick_seek(nums, p2 + 1, right)

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global n
        n = len(nums)
        self.quick_seek(nums, 0, n - 1)
        return nums[n // 2]


def main():
    nums = [2, 2, 1, 1, 1, 2, 2]
    test = Solution()
    ret = test.majorityElement(nums)
    print(ret)


if __name__ == '__main__':
    main()
