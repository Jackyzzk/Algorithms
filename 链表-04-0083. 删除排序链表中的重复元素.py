# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
输入: 1->1->2
输出: 1->2
输入: 1->1->2->3->3
输出: 1->2->3
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p and p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


def create(nums):
    n = len(nums)
    a = ListNode(nums[0])
    x = a
    for i in range(1, n):
        x.next = ListNode(nums[i])
        x = x.next
    return a


def main():
    # list1 = [1, 1, 2]
    list1 = [1, 1, 2, 3, 3]
    head = create(list1)
    test = Solution()
    ret = test.deleteDuplicates(head)
    print(ret)


if __name__ == '__main__':
    main()
