class Solution(object):
    """
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
    """
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for x in nums:
            if nums[abs(x) - 1] > 0:
                nums[abs(x) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] < 0:
                i += 1
            else:
                ret.append(i + 1)
        return ret


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    test = Solution()
    ret = test.findDisappearedNumbers(nums)
    print(ret)


if __name__ == '__main__':
    main()
