"""单链表study"""


class Node:
    """节点类"""

    def __init__(self, data):
        self.data = data  # 链表数据区
        self.next = None  # 链表指针区(链接区)


class SingleLinkList:
    """单链表类 -> 数学模型 + 一组操作(增、删、改...)"""

    def __init__(self):
        # 创建链表时,默认空链表 -> 头节点-指针区指向None -> object: self.head
        self.head = None

    # 1.判断链表是否为空 -> 头节点为None时代表空链表
    def is_empty(self):
        # return self.head == None
        return self.head is None

    # 2.获取链表长度 -> 头节点开始依次往后遍历,None时结束
    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    # 3.遍历整个链表
    def travel(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    # 4.从链表的头部添加一个节点
    def add(self, data):  # data节点中的数据区
        node = Node(data)
        # 把node的指针指向原来的头节点
        node.next = self.head
        # 把node设置为新的头节点
        self.head = node

    # 5.从链表的尾部添加一个节点
    def append(self, data):
        node = Node(data)
        # 空链表情况
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.next = None

    # 6.查看链表中是否存在某个元素
    def search(self, item):
        cur = self.head
        while cur:
            if cur.data == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    obj = SingleLinkList()
    # 创建链表: 100 -> 200 -> 300 -> None
    obj.add(300)
    obj.add(200)
    obj.add(100)
    print(obj.is_empty())
    print(obj.length())
    obj.travel()
    obj.append(400)
    print(obj.is_empty())
    obj.travel()
    print(obj.search(400))