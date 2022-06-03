class Node:
    def __init__(self, key):
        self.key = key;
        self.parent = self.left = self.right = None;
    def __str__(self):
        return str(self.key)

a = Node(6)
b = Node(9)
c = Node(5)
d = Node(1)

a.left = b
a.right = d
b.parent = a
b.right = c
c.parent = b
d.parent = a