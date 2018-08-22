

# 实现链表的Node类是一个节点，
# 有两个属性，一个存储元素，一个存储指向另一个节点的引用
class Node():
    def __init__(self, element=None, next_n=None):
        self.element = element
        self.next = next_n

    def __repr__(self):
        return str(self.element)


class Queue():
    # 分别指向头尾
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    # 如果head的next属性为空，则说明队列是空的
    def empty(self):
        return self.head.next is None

    # 创建一个Node
    # 让tail.next 指向它
    # 让tail指向它,tail现在就是新的队尾了
    def enqueue(self, element):
        # print("en:element", element)
        n = Node(element)
        # print("en:n", n, n.next)
        self.tail.next = n
        # print(self.tail)
        self.tail = n
        # print(self.tail)
        pass

    def dequeue(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node


def main():
    q = Queue()
    q.enqueue(1)
    # q.enqueue(2)

    print("head:", q.head)
    print("tail:", q.tail)


if __name__ == '__main__':
    main()