# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
    """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        def length(p):
            count = 0
            while p:
                count += 1
                p = p.next
            return count

        def rebuild(start, end):
            nonlocal head  # nonlocal关键字修饰变量后，表示该变量是上一级函数中的局部变量
            left = right = None
            m = (start + end) // 2
            if start <= m - 1:
                left = rebuild(start, m - 1)
            root = TreeNode(head.val)
            head = head.next
            if m + 1 <= end:
                right = rebuild(m + 1, end)
            root.left, root.right = left, right
            return root

        n = length(head)
        return rebuild(1, n)


def create(nums):
    n = len(nums)
    aux = ListNode(0)
    p = aux
    for i in range(n):
        p.next = ListNode(nums[i])
        p = p.next
    return aux.next


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
    list1 = [-10, -3, 0, 5, 9]

    head = create(list1)
    test = Solution()
    ret = test.sortedListToBST(head)
    bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()

