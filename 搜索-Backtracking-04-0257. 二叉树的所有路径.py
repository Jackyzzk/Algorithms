# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。
输入:
   1
 /   \
2     3
 \
  5
输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
链接：https://leetcode-cn.com/problems/binary-tree-paths/
    """
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(pre, cur):
            if cur.left or cur.right:
                if cur.left:
                    dfs(pre + str(cur.val) + '->', cur.left)
                if cur.right:
                    dfs(pre + str(cur.val) + '->', cur.right)
            else:
                ret.append(pre + str(cur.val))

        ret = []
        if root:
            dfs('', root)
        return ret


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
    nums = [1, 2, 3, None, 5]
    k = 1
    # nums = [5, 3, 6, 2, 4, None, None, 1]
    # k = 3
    global m
    m = len(nums)
    root = create(nums, 0)
    bfs(root)
    test = Solution()
    ret = test.binaryTreePaths(root)
    # bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()