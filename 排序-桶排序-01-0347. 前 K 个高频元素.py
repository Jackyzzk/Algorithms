class Solution(object):
    """
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
输入: nums = [1], k = 1
输出: [1]
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
链接：https://leetcode-cn.com/problems/top-k-frequent-elements/
    """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count, ret = {}, []
        for x in nums:
            count[x] = count.get(x, 0) + 1
        m = max(count.values())
        bucket = [[] for i in range(m + 1)]  # 生成桶 每个桶的下标代表出现频率
        for key, val in count.items():
            bucket[val].append(key)
        for i in range(m, 0, -1):
            ret.extend(bucket[i])
            if len(ret) >= k:
                return ret[:k]


def main():
    nums = [1, 2, 1, 3, 2, 1, 5, 5, 5, 7, 6, 6]
    k = 1
    nums = [1, 1, 1, 2, 2, 3]
    k = 3
    # nums = [1]
    # k = 1
    test = Solution()
    ret = test.topKFrequent(nums, k)
    print(ret)


if __name__ == '__main__':
    main()

