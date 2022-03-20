"""输入一个链表,反转链表后,输出新链表的表头"""


# 1.创建两个游标cur -> 反转操作的节点和上一个节点
# 2.操作的节点指向前一个节点
# 3.两个游标同时往后移
# 4.结束标准:当要操作的节点为None时结束


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def reverse_link(self, head):
        if head == None:
            return None
        # 建立两个游标
        pre = None
        cur = head
        while cur:
            # 反转节点,移动两个游标
            next_node = cur.next
            # 移动游标
            cur.next = pre
            pre = cur
            cur = next_node
        # 循环结束后,pre指向的即是表头
        return pre.data


if __name__ == "__main__":
    s = Solution()
    # 创建链表 100 -> 200 -> 300
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    value = s.reverse_link(head)
    print(value)
