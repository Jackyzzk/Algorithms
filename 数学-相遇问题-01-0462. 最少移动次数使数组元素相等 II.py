import random

class Solution(object):
    """
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，
其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。
输入: [1,2,3]
输出: 2
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
使用快速选择找到中位数，时间复杂度 O(N)
先排序，时间复杂度：O(NlogN)
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/
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

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global n
        n = len(nums)
        self.quick_seek(nums, 0, n - 1)
        t = nums[n // 2]
        ret = 0
        for i in range(n):
            ret += abs(nums[i] - t)
        return ret


def main():
    nums = [1]
    test = Solution()
    ret = test.minMoves2(nums)
    print(ret)


if __name__ == '__main__':
    main()
