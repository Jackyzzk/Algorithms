class Solution(object):
    """
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
输入: [1,2,3,1]
输出: true
输入: [1,2,3,4]
输出: false
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
链接：https://leetcode-cn.com/problems/contains-duplicate/
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        rec = set()
        for x in nums:
            if x in rec:
                return True
            else:
                rec.add(x)
        return False


def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    # nums = [1, 2, 3, 1]
    # nums = []
    test = Solution()
    ret = test.containsDuplicate(nums)
    print(ret)


if __name__ == '__main__':
    main()
