class Solution(object):
    """
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
不能使用代码库中的排序函数来解决这道题。
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
链接：https://leetcode-cn.com/problems/sort-colors/
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0 = -1  # 碰到0才走,开始先在域外等着
        p2 = len(nums)  # 碰到2才走,开始先在域外等着
        cur = 0  # 碰到小于等于1的都可以走
        # 一次循环下来0-p0全是0，p0-cur全是1，p2-最后全是2，此时cur与p2相遇
        while cur < p2:
            if nums[cur] == 0:
                p0 += 1
                nums[cur], nums[p0] = nums[p0], nums[cur]
                cur += 1  # 从 p0 换过来的值只能是 0 或者 1，cur 都可以 + 1
            elif nums[cur] == 2:
                p2 -= 1
                nums[cur], nums[p2] = nums[p2], nums[cur]
            else:  # nums[cur] == 1
                cur += 1


def main():
    nums = [0, 2, 1, 0, 2, 1, 1, 2, 1]
    # nums = [1, 2, 0]
    test = Solution()
    ret = test.sortColors(nums)
    print(nums)


if __name__ == '__main__':
    main()
