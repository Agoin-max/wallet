

#  删除有序链表中重复的元素

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # write code here
        if not head:
            return None
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head