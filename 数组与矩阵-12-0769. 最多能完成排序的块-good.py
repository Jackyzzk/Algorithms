class Solution(object):
    """
数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，
并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
我们最多能将数组分成多少块？
输入: arr = [4,3,2,1,0]
输出: 1
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
输入: arr = [1,0,2,3,4]
输出: 4
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
arr 的长度在 [1, 10] 之间。
arr[i]是 [0, 1, ..., arr.length - 1]的一种排列。
链接：https://leetcode-cn.com/problems/max-chunks-to-make-sorted
    """
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n, count, aux_max = len(arr), 0, 0
        for i in range(n):
            aux_max = max(aux_max, arr[i])
            if aux_max == i:  # 最大的数等于下标的时候
                count += 1
        return count


def main():
    # arr = [1, 0, 2, 3, 4]  # 4
    # arr = [4, 3, 2, 1, 0]  # 1
    # arr = [2, 1, 0, 3, 4]  # 3
    arr = [2, 0, 1]  # 1
    # arr = [1, 2, 0]  # 1
    # arr = [1, 0, 2, 3, 4]  # 4
    # arr = [1, 4, 0, 2, 3, 5]  # 2
    # arr = [1, 0]  # 1
    test = Solution()
    ret = test.maxChunksToSorted(arr)
    print(ret)


if __name__ == '__main__':
    main()
