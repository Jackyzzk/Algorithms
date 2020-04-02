class Solution(object):
    """
给定一个大小为 n 的数组，找到其中的多数元素。
多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
输入: [3,2,3]
输出: 3
输入: [2,2,1,1,1,2,2]
输出: 2
摩尔投票法
链接：https://leetcode-cn.com/problems/majority-element/
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count > 0:
                if nums[i] == p:
                    count += 1
                else:
                    count -= 1
            else:
                p = nums[i]
                count = 1
        return p


def main():
    nums = [2, 2, 1, 1, 1, 2, 2]
    test = Solution()
    ret = test.majorityElement(nums)
    print(ret)


if __name__ == '__main__':
    main()
