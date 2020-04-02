# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
    """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(root):
            return dfs(root.left) + [root.val] + dfs(root.right) if root else []

        return dfs(root)[k - 1]


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
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
    nums = [3, 1, 4, None, 2]
    k = 1
    # nums = [5, 3, 6, 2, 4, None, None, 1]
    # k = 3
    global m
    m = len(nums)
    root = create(nums, 0)
    bfs(root)
    test = Solution()
    ret = test.kthSmallest(root, k)
    # bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()
