class Tree(object):
    def __init__(self, element=None, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def traversal(self):
        """树的深度遍历，递归"""
        # 前序遍历，先把中间全部打印出来，再左，再右
        print(self.element)
        if self.left is not None:
            self.left.traversal()
        # 中序遍历，寻根再找兄弟，先把左边打印出来，再中间，再右
        # print(self.element)
        if self.right is not None:
            self.right.traversal()
        # 后序遍历,先兄弟，先把左边全部打印出来，再右，再中间
        # print(self.element)

    def reverse(self):
        """翻转"""
        self.left, self.right = self.right, self.left
        print(self.element)
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()


def test():
    t = Tree(0, Tree(1, Tree(3, Tree(5), Tree(6)), Tree(4, Tree(7), Tree(8))), Tree(2, Tree(9), Tree(10)))
    # left = Tree(1)
    # right = Tree(2)
    # t.left = left
    # t.right = right
    # Node = Tree
    # t = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    t.traversal()
    print("_________")
    t.reverse()


if __name__ == '__main__':
    test()