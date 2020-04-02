# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
链接：https://leetcode-cn.com/problems/symmetric-tree/
    """
    def judge(self, t1, t2):
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        if t1.val == t2.val:
            return self.judge(t1.left, t2.right) and self.judge(t1.right, t2.left)
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.judge(root.left, root.right)


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    nums = [1, 2, 2, 3, 4, 5, 3]
    # nums = [1, 2, 2, None, 3, None, 3]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.isSymmetric(root)
    print(ret)


if __name__ == '__main__':
    main()
