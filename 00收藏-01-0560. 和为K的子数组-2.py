class Solution(object):
    """
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k/
    """
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rec = {0: 1}
        total, count = 0, 0
        for x in nums:
            total += x
            if total - k in rec:
                count += rec[total - k]
            rec[total] = rec.get(total, 0) + 1
        return count


def main():
    nums, k = [1, 1, 1, 1, 1], 3
    # nums, k = [1, 1, 1, 1], 3
    # nums, k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0  # 55
    test = Solution()
    ret = test.subarraySum(nums, k)
    print(ret)


if __name__ == '__main__':
    main()
