

class Node(object):
    def __init__(self, ele):
        self.ele = ele
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<class Node {self.ele}>"
    __str__ = __repr__


class Tree(object):

    def __init__(self, root=None):
        self.root = root

    def add(self, ele):

        node = Node(ele)
        if not self.root:
            self.root = node
        else:

            queue = [self.root]
            while queue:
                cur_node = queue.pop(0)
                if not cur_node.left:
                    cur_node.left = node
                    return
                elif not cur_node.right:
                    cur_node.right = node
                    return
                else:
                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)

    def travel(self):
        """
        广度优先遍历
        :return:
        """
        if not self.root:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.ele, end='\t')
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    def travel_1(self, root=None):
        if not root:
            return
        # 前序遍历 根 左 右
        print(root.ele, end='\t')
        self.travel_1(root.left)
        self.travel_1(root.right)

    def travel_2(self, root=None):
        if not root:
            return
        # 中序遍历 左 根 右
        self.travel_2(root.left)
        print(root.ele, end='\t')
        self.travel_2(root.right)

    def travel_3(self, root=None):
        if not root:
            return
        self.travel_3(root.left)
        self.travel_3(root.right)
        # 后序遍历 左 右 根
        print(root.ele, end='\t')


t = Tree()
t.add(0)
t.add(1)
t.add(2)
t.add(3)
t.add(4)
t.add(5)
t.add(6)
t.add(7)
t.add(8)
t.add(9)

print(t.root.left.right)
t.travel()
print()
t.travel_1(t.root)
print()
t.travel_2(t.root)
print()
t.travel_3(t.root)