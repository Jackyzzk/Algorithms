# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，
这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
链接：https://leetcode-cn.com/problems/odd-even-linked-list/
    """
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p1, p2, rec = head, head.next, head.next
        while p2 and p2.next:  # 每次循环结束p2总在p1后面
            p1.next, p1 = p1.next.next, p1.next.next
            p2.next, p2 = p2.next.next, p2.next.next
        p1.next = rec
        return head


def create(nums):
    n = len(nums)
    aux = ListNode(0)
    p = aux
    for i in range(n):
        p.next = ListNode(nums[i])
        p = p.next
    return aux.next


def main():
    # list1 = [1, 2]
    # list1 = [2, 1, 3, 5, 6, 4, 7]
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    head = create(list1)
    test = Solution()
    ret = test.oddEvenList(head)
    print(ret)


if __name__ == '__main__':
    main()
