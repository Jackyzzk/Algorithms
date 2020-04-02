# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
给定二叉树
          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree/
    """
    ret = 0

    def depth(self, root):
        if not root:
            return 0
        n1 = self.depth(root.left)
        n2 = self.depth(root.right)
        if n1 + n2 > self.ret:
            self.ret = n1 + n2
        return max(n1, n2) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.ret


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    nums = [1, 2, None, 4, 5, None, None, 6, None]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.diameterOfBinaryTree(root)
    print(ret)


if __name__ == '__main__':
    main()


