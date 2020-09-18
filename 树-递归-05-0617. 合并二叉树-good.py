# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，
那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
输入:
    Tree 1                     Tree 2
      1                         2
     / \                       / \
    3   2                     1   3
   /                           \   \
  5                             4   7
输出:
合并后的树:
     3
    / \
   4   5
  / \   \
 5   4   7
注意: 合并必须从两个树的根节点开始。
链接：https://leetcode-cn.com/problems/merge-two-binary-trees/
    """

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)  # 返回的也给赋值起来
        elif not t1:
            return t2
        return t1


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
    nums1 = [1, 3, 2, 5]
    nums2 = [2, 1, 3, None, 4, None, 7]
    global m
    m = len(nums1)
    root1 = create(nums1, 0)
    m = len(nums2)
    root2 = create(nums2, 0)
    test = Solution()
    ret = test.mergeTrees(root1, root2)
    print(ret)


if __name__ == '__main__':
    main()

