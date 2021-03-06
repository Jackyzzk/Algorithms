class Solution(object):
    """
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
链接：https://leetcode-cn.com/problems/merge-sorted-array/
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            if p1 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p2 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        return nums1


def main():
    nums1, m = [3, 7, 8, 9, 0, 0, 0], 4
    nums2, n = [2, 3, 4], 3
    # nums1, m = [1, 2, 3, 0, 0, 0], 3
    # nums2, n = [2, 5, 6], 3
    # nums1, m = [1], 1
    # nums2, n = [], 0
    test = Solution()
    ret = test.merge(nums1, m, nums2, n)
    print(ret)


if __name__ == '__main__':
    main()
