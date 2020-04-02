# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，返回它的中序 遍历。
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
中序遍历，左根右
在第一个根节点被加入ret之前，要完成对左子树的遍历
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        que, ret = [], []
        p = root
        while que or p:
            while p:  # 一头扎进左子树最左端
                que.append(p)
                p = p.left
            p = que.pop()
            ret.append(p.val)
            p = p.right
        return ret


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    nums = [1, 2, 3, None, 4, 5]

    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.inorderTraversal(root)
    print(ret)


if __name__ == '__main__':
    main()
