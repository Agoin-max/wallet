# 判断一个链表是否为回文结构

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPail(self, head: ListNode) -> bool:
        # write code here
        li = []
        cur = head
        while cur:
            li.append(cur.val)
            cur = cur.next
        if li == li[::-1]:
            return True
        else:
            return False
