# 链表的奇偶重排

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # write code here
        if not head:
            return None
        cur = head
        res1, res2 = [], []
        n = 1
        while cur:
            if n % 2 == 0:
                res1.append(cur.val)
            else:
                res2.append(cur.val)
            cur = cur.next
            n = n + 1
        res = res2 + res1
        a = ListNode(0)
        ans = a
        for i in res:
            a.next = ListNode(i)
            a = a.next
        return ans.next
