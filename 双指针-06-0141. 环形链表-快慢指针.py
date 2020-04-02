# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution(object):
    """
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
链接：https://leetcode-cn.com/problems/linked-list-cycle/
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1, p2 = head, head.next
        while p1 != p2:
            if p2 and p2.next:
                p1, p2 = p1.next, p2.next.next
            else:
                return False
        return True


def create(nums, pos):
    n = len(nums)
    aux = ListNode(0)
    p = aux
    for i in range(n):
        p.next = ListNode(nums[i])
        p = p.next
        if i == pos:
            rec = p
    if pos >= 0:
        p.next = rec
    return aux.next


def main():
    list1, pos = [3, 2, 0, -4], 1
    # list1, pos = [1, 2], 0
    # list1, pos = [1], -1
    head = create(list1, pos)
    test = Solution()
    ret = test.hasCycle(head)
    print(ret)


if __name__ == '__main__':
    main()

