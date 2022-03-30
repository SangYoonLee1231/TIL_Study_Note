from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def pop(self):
        if self.empty():
            raise Exception("Queue is Empty")
        return self.dq.popleft()
    
    def empty(self):
        return not self.size()
    
    def front(self):
        if self.empty():
            raise Exception("Queue is Empty")
        return self.dq[0]

    def size(self):
        return len(self.dq)


n, k = tuple(map(int, input().split()))
q = Queue()

for i in range(1, n+1):
    q.push(i)

while not q.empty():
    for _ in range(k-1):
        q.push(q.pop())
    print(q.pop(), end=' ')