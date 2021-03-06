# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
假定 BST 有如下定义：
结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
给定 BST [1,null,2,2],
   1
    \
     2
    /
   2
返回[2].
提示：如果众数超过1个，不需考虑输出顺序
进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/
    """
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #  BST 是排序树 遍历用中序遍历
        if not root:
            return []
        rec, que, p = {}, [], root
        while que or p:
            while p:
                que.append(p)
                p = p.left
            p = que.pop()
            rec[p.val] = rec.get(p.val, 0) + 1
            p = p.right
        m = max(rec.values())
        ret = [k for k, v in rec.items() if v == m]
        return ret


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
    nums = [1, None, 2, None, None, 2]
    global m
    m = len(nums)
    root = create(nums, 0)
    bfs(root)
    test = Solution()
    ret = test.findMode(root)
    # bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()
