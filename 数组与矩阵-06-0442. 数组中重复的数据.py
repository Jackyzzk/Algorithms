class Solution(object):
    """
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
输入:
[4,3,2,7,8,2,3,1]
输出:
[2,3]
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
    """
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for x in nums:
            if nums[abs(x) - 1] > 0:
                nums[abs(x) - 1] *= -1
            else:
                ret.append(abs(x))
        return ret


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    test = Solution()
    ret = test.findDuplicates(nums)
    print(ret)


if __name__ == '__main__':
    main()
