class Solution(object):
    """
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，
导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，
导致集合丢失了一个整数并且有一个元素重复。
给定一个数组 nums 代表了集合 S 发生错误后的结果。
你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
输入: nums = [1,2,2,4]
输出: [2,3]
给定数组的长度范围是 [2, 10000]。
给定的数组是无序的。
链接：https://leetcode-cn.com/problems/set-mismatch
    """
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in nums:
            if nums[abs(x) - 1] > 0:  # 减1是为了对应下标
                nums[abs(x) - 1] *= -1
            else:  # 把原数组第x个数给翻转，如果已经翻转了就是x之前出现过了
                dup = abs(x)
        i = 0
        while True:
            if nums[i] < 0:
                i += 1
            else:
                break
        return [dup, i + 1]


def main():
    nums = [1, 2, 3, 4, 4]
    test = Solution()
    ret = test.findErrorNums(nums)
    print(ret)


if __name__ == '__main__':
    main()
