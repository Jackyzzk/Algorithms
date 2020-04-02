class Solution(object):
    """
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k/
    """
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sum = 0
        aux = {0: 1}
        count = 0
        for x in nums:
            # count += aux.get(pre_sum + x - k, 0)
            pre_sum += x
            # 假设 pre_sum 是一个数组，表示 nums[0] + .. + nums[i - 1]
            # k = nums[t] + .. + nums[i] = pre_sum[i] - pre_sum[t] + nums[i]
            # 目标变成 pre_sum[t] = pre_sum[i] + nums[i] - k 在 pre_sum中是否存在，存在几个
            # count += aux.get(pre_sum - k, 0)
            if pre_sum - k in aux:
                count += aux[pre_sum - k]
            # aux[pre_sum] = aux.get(pre_sum, 0) + 1
            if pre_sum in aux:
                aux[pre_sum] = aux[pre_sum] + 1
            else:
                aux[pre_sum] = 1
        return count


def main():
    # nums = [1, 1, 1, 1, 1]
    # k = 3
    # nums = [1, 1, 1, 1]
    # k = 3
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # nums = [0]
    k = 0
    test = Solution()
    ret = test.subarraySum(nums, k)
    print(ret)


if __name__ == '__main__':
    main()
