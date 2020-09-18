class Solution(object):
    """
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence/
    """
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rec, ret = {}, 0  # rec 的键值对分别记录端点坐标以及区间长度
        for x in nums:
            if x not in rec:
                left, right = rec.get(x - 1, 0), rec.get(x + 1, 0)
                # 根据区间长度可以从当前 x 找到端点坐标
                rec[x - left] = rec[x] = rec[x + right] = left + right + 1
                ret = max(ret, rec[x])
        return ret


def main():
    nums = [100, 4, 200, 1, 3, 2]
    # nums = [1, 0, -1]  # 3
    # nums = [1, 2, 0, 1]  # 3
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  # 9
    nums = []
    # nums = [1, 3, 5, 2, 4]  # 5
    # nums = [-6,6,-9,-7,0,3,4,-2,2,-1,9,-9,5,-3,6,1,5,-1,-2,9,-9,-4,-6,-5,6,-1,3]  # 14
    test = Solution()
    ret = test.longestConsecutive(nums)
    print(ret)


if __name__ == '__main__':
    main()
