# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
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
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
    """
    # for it in iterables:
    #     for i in it:
    #         yield i
    # 等价于：
    # for it in iterables:
    #     yield from it

    # 当 yield from 后面加上一个生成器后，就实现了生成的嵌套。
    # 1、调用方：调用委派生成器的客户端（调用方）代码
    # 2、委托生成器：包含yield from表达式的生成器函数
    # 3、子生成器：yield from后面加的生成器函数
    # 委托生成器的作用是：在调用方与子生成器之间建立一个双向通道。
    # 委托生成器，只起一个桥梁作用，它建立的是一个双向通道，它并没有权利也没有办法，对子生成器 yield 回来的内容做拦截。
    # 但是可以在 yield from 前面看到赋值

    def mid_order(self, root):
        if not root:
            return
        yield from self.mid_order(root.left)  # yield from 会运行到 下一行的 yield 处停下，而这里产生的 None 不会被传出去
        yield root.val
        yield from self.mid_order(root.right)

    def kthSmallest(self, root, k):
        gen = self.mid_order(root)
        for i in range(k - 1):
            next(gen)
        return next(gen)


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
    # nums = [3, 1, 4, None, 2]
    # k = 1
    nums = [5, 3, 6, 2, 4, None, None, 1]
    k = 3
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
