# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
链接：https://leetcode-cn.com/problems/path-sum/
    """
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not (root.left or root.right):  # 叶子节点是指没有子节点的节点
            return root.val == sum
        b1 = self.hasPathSum(root.left, sum - root.val) if root.left else False
        b2 = self.hasPathSum(root.right, sum - root.val) if root.right else False
        return b1 or b2


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
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
    h = 22
    # nums = [None]
    # h = 0
    # nums = [1, 2]
    # h = 1
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.hasPathSum(root, h)
    print(ret)


if __name__ == '__main__':
    main()
