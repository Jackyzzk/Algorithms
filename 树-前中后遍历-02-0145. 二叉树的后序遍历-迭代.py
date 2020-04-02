# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，返回它的 后序 遍历。
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
后续遍历，左右根，根在最后，但是由于queue以及pop的原因，第一个处理的肯定是root根节点
这也就要求ret返回必须是倒序，即加入ret的顺序与ret的输出顺序相反
所以加入顺序为 根 右 左 ，即处理顺序是 根 右 左
而且前中后序遍历都是深度遍历，不能使用广度遍历的append，必须插队que[0:0]
所以写法是根 左 右 让左右插队
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
    """
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        que, ret = [root], []
        while que:
            p = que.pop(0)
            ret.append(p.val)
            if p.left:
                que[0:0] = [p.left]
            if p.right:
                que[0:0] = [p.right]
        ret.reverse()
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
    # nums = [1, 4, 3, 2]  # [1,4,2,3]
    nums = [3, 2, 4, None, None, 1]  # [2,1,4,3]
    # nums = [1]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.postorderTraversal(root)
    print(ret)


if __name__ == '__main__':
    main()
