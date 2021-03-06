# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
编写一个程序，找到两个单链表相交的起始节点。
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
    """
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not (headA and headB):
            return None
        p1 = headA
        p2 = headB
        count = 0
        while count < 3:
            if p1 != p2:
                if p1.next is None:
                    p1 = headB
                    count += 1
                else:
                    p1 = p1.next
                if p2.next is None:
                    p2 = headA
                    count += 1
                else:
                    p2 = p2.next
            else:
                return p1.val
        return None


def create(nums, skip, t=None):
    n = len(nums)
    a = ListNode(nums[0])
    x = a
    for i in range(1, n):
        x.next = ListNode(nums[i])
        if i == skip:
            if not t:
                t = x.next
            else:
                x.next = t
                break
        x = x.next
    return a, t


def main():
    intersect = 8
    list1 = [4, 1, 8, 4, 5]
    list2 = [5, 0, 1, 8, 4, 5]
    skip1 = 2
    skip2 = 3
    # intersect = 0
    # list1 = [2, 6, 4]
    # list2 = [1, 5]
    # skip1 = 3
    # skip2 = 2
    a, t = create(list1, skip1)
    b, t = create(list2, skip2, t)
    test = Solution()
    ret = test.getIntersectionNode(a, b)
    print(ret)


if __name__ == '__main__':
    main()
