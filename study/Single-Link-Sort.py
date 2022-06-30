# 单链表的排序

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortInList(self, head: ListNode) -> ListNode:
        # write code here
        if not head:
            return None
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        res.sort()
        a = ListNode(0)
        cur1 = a
        for i in res:
            a.next = ListNode(i)
            a = a.next
        return cur1.next
