# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
给定的 n 保证是有效的。
进阶：你能尝试使用一趟扫描实现吗？
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        aux = ListNode(0)
        aux.next = head
        count = 0
        p1 = p2 = aux
        while count < n + 1:
            p1 = p1.next
            count += 1
        while p1:
            p1, p2 = p1.next, p2.next
        p2.next = p2.next.next
        return aux.next


def create(nums):
    n = len(nums)
    a = ListNode(nums[0])
    x = a
    for i in range(1, n):
        x.next = ListNode(nums[i])
        x = x.next
    return a


def main():
    list1 = [1, 2, 3, 4, 5]
    # list1 = [1]
    head = create(list1)
    n = 2
    test = Solution()
    ret = test.removeNthFromEnd(head, n)
    print(ret)


if __name__ == '__main__':
    main()