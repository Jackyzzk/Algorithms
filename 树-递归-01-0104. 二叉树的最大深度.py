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
    if not nums:
        return None
    root = TreeNode(nums.pop(0))
    que = [root]
    while que:
        node = que.pop(0)
        left = nums.pop(0) if nums else None
        right = nums.pop(0) if nums else None
        node.left = TreeNode(left) if left is not None else None
        node.right = TreeNode(right) if right is not None else None
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
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

