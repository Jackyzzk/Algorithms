# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
    """
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        n1 = self.minDepth(root.left)
        n2 = self.minDepth(root.right)
        if n2 == 0:
            return n1 + 1
        if n1 == 0:
            return n2 + 1
        return min(n1, n2) + 1


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    # nums = [3, 9, 20, None, None, 15, 7]
    nums = [1, 2]  # 2
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.minDepth(root)
    print(ret)


if __name__ == '__main__':
    main()
