# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
给定 1->2->3->4, 你应该返回 2->1->4->3.
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/
    """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        aux = ListNode(0)
        aux.next = head
        p = aux
        while p and p.next and p.next.next:
            p.next.next.next, p.next.next, p.next = p.next, p.next.next.next, p.next.next
            # 赋值的时候先从多的开始，读取的话则不用
            p = p.next.next
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
    list1 = [1, 2, 3, 4]
    # list1 = [1, 1, 2, 3, 3]
    head = create(list1)
    test = Solution()
    ret = test.swapPairs(head)
    print(ret)


if __name__ == '__main__':
    main()