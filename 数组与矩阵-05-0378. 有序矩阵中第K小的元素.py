class Solution(object):
    """
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。
matrix =
[
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8, 返回 13。
你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
    """
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """


def main():
    matrix = \
[
   [1,   5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
    k = 8
    test = Solution()
    ret = test.kthSmallest(matrix, k)
    print(ret)


if __name__ == '__main__':
    main()
