# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
    """
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        n1 = 1 + self.maxDepth(root.left)
        n2 = 1 + self.maxDepth(root.right)
        return max(n1, n2)


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    nums = [3, 9, 20, None, None, 15, 7]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.maxDepth(root)
    print(ret)


if __name__ == '__main__':
    main()

