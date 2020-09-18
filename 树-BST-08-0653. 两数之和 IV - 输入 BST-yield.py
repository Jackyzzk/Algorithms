# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
输入:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
输出: True
输入:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
输出: False
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
    """
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def dfs1(root):
            que, p = [], root
            while que or p:
                while p:
                    que.append(p)
                    p = p.left
                p = que.pop()
                yield p.val
                p = p.right

        def dfs2(root):
            que, p = [], root
            while que or p:
                while p:
                    que.append(p)
                    p = p.right
                p = que.pop()
                yield p.val
                p = p.left

        gen1, gen2 = dfs1(root), dfs2(root)
        p1, p2 = next(gen1), next(gen2)
        if p2 * 2 <= k or p1 * 2 >= k:
            return False
        while p1 != p2:
            if p1 + p2 == k:
                return True
            if p1 + p2 > k:
                p2 = next(gen2)
            else:
                p1 = next(gen1)
        return False


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
    nums = [5, 3, 6, 2, 4, None, 7]
    k = 9
    global m
    m = len(nums)
    root = create(nums, 0)
    bfs(root)
    test = Solution()
    ret = test.findTarget(root, k)
    # bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()
