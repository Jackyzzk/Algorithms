# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def rebuild(start, end):
            m = (start + end) >> 1
            left = right = None
            if start <= m - 1:
                left = rebuild(start, m - 1)  # 一直到 start = m，一头扎进最左端
            root = TreeNode(nums[self.count])
            self.count += 1
            if end >= m + 1:
                right = rebuild(m + 1, end)
            root.left, root.right = left, right
            return root

        self.count = 0
        return rebuild(0, len(nums) - 1)


def bfs(root):
    if not root:
        return root
    que, ret = [root], []
    while que:
        p = que.pop(0)
        ret.append(p.val)
        if p.left:
            que.append(p.left)
        if p.right:
            que.append(p.right)
    print(ret)


def main():
    nums = [-10, -3, 0, 5, 9]
    # nums = []
    test = Solution()
    ret = test.sortedArrayToBST(nums)
    bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()
