# 输入一个链表,输出该链表中倒数第k个节点

class LinkNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    def get_k_node(self, head, k):
        # 转列表处理
        li = []
        cur = head
        while cur:
            li.append(cur.value)
            cur = cur.next
        if k > len(li):
            raise IndexError("list index out of range")
        return li[-k]

    def get_node(self, head: LinkNode, k: int) -> LinkNode:
        fast = head
        slow = head

        # 快指针先行k步
        for i in range(0, k):
            if fast != None:
                fast = fast.next
            # 达不到k步说明链表过短,没有倒数k
            else:
                return None
        # 快慢指针同步,快指针先到底,慢指针指向倒数第k个
        while fast:
            fast = fast.next
            slow = slow.next

        return slow
