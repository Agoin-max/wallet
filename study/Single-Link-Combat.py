"""输入一个链表,链表值从尾到头顺序返回一个ArrayList"""


# 1.从头到尾取出链表数据区的数据放进List
# 2.List反转

class Node:
    """节点类"""

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def get_reverse_list(self, head):
        _array = []
        cur = head
        while cur:
            _array.append(cur.data)
            cur = cur.next
        _array.reverse()
        return _array


if __name__ == '__main__':
    _obj = Solution()
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    _array = _obj.get_reverse_list(head)
    print(_array)
