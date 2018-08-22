# 实现链表的Node类是一个节点，
# 有两个属性，一个存储元素，一个存储指向另一个节点的引用
class Node():
    def __init__(self, element=None, next_n=None):
        self.e = element
        # 存下一个Node
        self.next = next_n

    def append(self, element):
        """
        插入到链表尾，往node末尾插入一个元素
        node:是一个Node实例
        element:任意类型元素
        """
        n = self
        while n.next is not None:
            n = n.next
            # 循环结束n是最后一个元素，最后的n.next = None
            # 假设传node参数为head,最后的n.next是n3
        new_node = Node(element)
        # 将上面的点加到n.next
        n.next = new_node

    @staticmethod
    def prepend(element):
        """
        插入到链表头
        :param head:传入一个头
        :param element:任意类型元素
        :return:
        """
        head = Node()
        n = Node(element)
        # n 成为了新的头
        n.next = head.next
        # 将数据写入头
        head.next = n

    def pop(self):
        """
        传入头删掉最末尾的元素
        :param head: 传入一个头
        :return:返回被删掉的对象的值
        """
        head = self.head # todo 不是同一个head,新的
        tail = head
        while tail.next is not None:
            tail = tail.next
            # 此时tail是最末尾的元素
            print("tail:", tail)
        n = head
        print('n:', n.next)
        while n.next is not tail:
            n = n.next
            # 此时n是tail之前的元素
            print(n)
        # 清掉最后一个元素
        n.next = None
        # 返回被删掉元素的值
        return tail.e


def pop(head):
    """
    传入头删掉最末尾的元素
    :param head: 传入一个头
    :return:返回被删掉的对象的值
    """

    tail = head
    while tail.next is not None:
        tail = tail.next
        # 此时tail是最末尾的元素
    n = head
    while n.next is not tail:
        n = n.next
        # 此时n是tail之前的元素
    # 清掉最后一个元素
    n.next = None
    # 返回被删掉元素的值
    return tail.e


def log_list(node):
    """
    打印一个点及之后所有点的值
    :param node: Node的实例
    """
    n = node
    s = ''
    while n is not None:
        s += (str(n.e) + '>')
        n = n.next
    print(s)


def main():
    head = Node()
    n1 = Node(111)
    n2 = Node(222)
    n3 = Node(333)

    head.next = n1
    n1.next = n2
    n2.next = n3
    head.append(444)
    head.append(555)
    # pop(head)
    head.pop()
    head.prepend('header')
    log_list(head)
# None>header>111>222>333>444>


def main2():
    pass



if __name__ == '__main__':
    main()