# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。
通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
二叉排序树，若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
它的左、右子树也分别为二叉排序树。
输入:
    1
   / \
  0   2

  L = 1
  R = 2
输出:
    1
      \
       2
输入:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3
输出:
      3
     /
   2
  /
 1
链接：https://leetcode-cn.com/problems/trim-a-binary-search-tree/
    """
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        # L <= root.val <= R:
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


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
    nums = [3, 0, 4, None, 2, None, None, 1]
    l, r = 1, 3
    # nums = [1, 0, 2]
    # l, r = 1, 2
    global m
    m = len(nums)
    root = create(nums, 0)
    bfs(root)
    test = Solution()
    ret = test.trimBST(root, l, r)
    bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()
