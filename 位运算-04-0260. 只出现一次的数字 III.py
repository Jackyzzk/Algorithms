class Solution(object):
    """
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。
找出只出现一次的那两个元素。
输入: [1,2,1,3,2,5]
输出: [3,5]
结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
链接：https://leetcode-cn.com/problems/single-number-iii
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t, ret = 0, [0, 0]
        for x in nums:
            t ^= x  # 异或的结果表示在哪些位置上是不同的
        t &= -t  # t & (-t) 表示得到 t 的最后一个 1 连同它所在的位
        for x in nums:
            if x & t:  # 或运算添加属性，与运算判断属性，异或运算消去属性，这里的判断就是起到一个划分的作用
                ret[0] ^= x  # 重复出现的元素也会因为具有相同的特征而被划到同一边，然后异或运算后又等于 0
            else:
                ret[1] ^= x  # 这一步其实可以优化，ret[1] = ret[0] ^ t(第一次for后的t) ，因为 t = ret[0] ^ ret[1]
        return ret


def main():
    nums = [1, 2, 1, 3, 2, 5]
    test = Solution()
    ret = test.singleNumber(nums)
    print(ret)


if __name__ == '__main__':
    main()
