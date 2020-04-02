class Solution(object):
    """
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
    """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            x = numbers[p1] + numbers[p2]
            if x > target:
                p2 -= 1
            elif x < target:
                p1 += 1
            else:  # x == target:
                return [p1 + 1, p2 + 1]


def main():
    numbers = [2, 7, 9, 11]
    target = 16
    test = Solution()
    ret = test.twoSum(numbers, target)
    print(ret)


if __name__ == '__main__':
    main()