class Node:
    def __init__(self, element):
        self.data = element
        self.link = None


head = Node(10)
head.link = Node(20)
head.link.link = Node(30)

node = Node(50)
node.link = head
head = node