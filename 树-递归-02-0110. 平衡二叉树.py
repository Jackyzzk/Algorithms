# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
链接：https://leetcode-cn.com/problems/balanced-binary-tree/
    """
    def depth(self, root):
        if not root:
            return 0
        n1 = self.depth(root.left)
        n2 = self.depth(root.right)
        return max(n1, n2) + 1

    def depth_judge(self, root):
        if not root:
            return True
        t1 = self.depth(root.left)
        t2 = self.depth(root.right)
        t = abs(t1 - t2)
        if t <= 1:
            return True
        else:
            return False

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        b1 = self.isBalanced(root.left) and self.depth_judge(root.left)
        b2 = self.isBalanced(root.right) and self.depth_judge(root.right)
        return b1 and b2 and self.depth_judge(root)


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    # nums = [3, 9, 20, None, None, 15, 7]
    nums = [1, 2, 2, 3, 3, None, None, 4, 4]
    # nums = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, None, None, 5, 5]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.isBalanced(root)
    print(ret)


if __name__ == '__main__':
    main()
