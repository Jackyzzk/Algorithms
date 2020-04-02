# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，返回它的 前序 遍历。根左右
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
    """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        que = [root]
        ret = []
        while que:
            p = que.pop()  # append 和 pop 的组合是先进后出
            ret.append(p.val)
            if p.right:  # 先进后出
                que.append(p.right)
            if p.left:
                que.append(p.left)
        return ret


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    # nums = [1, None, 2, None, None, 3]
    nums = [1, 4, 3, 2]  # [1,4,2,3]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.preorderTraversal(root)
    print(ret)


if __name__ == '__main__':
    main()
