# 순차적 자료구조 : 단방향 연결 리스트 (Singly Linked List)

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 단방향 연결 리스트(Singly Linked List)란

* Node들이 <strong>한 쪽 방향으로만 연결된</strong> 연결 리스트이다.

<img src="img/singly_linked_list1.png">

* 가장 앞쪽에 있는 Node를 <strong>Head Node</strong>라 부르고, 가장 뒷쪽에 있는 Node를 <strong>Tail Node</strong>라 부른다.

* Node 1개의 구성 요소

    * 단방향 연결 리스트 : Node 1개 = key 1개, <strong>link 1개</strong> (+ 부가 데이터 value)
    
    * 양방향 연결 리스트 : Node 1개 = key 1개, <strong>link 2개</strong> (+ 부가 데이터 value)

<br/>

## 단방향 연결 리스트 구현

### Node 구현

```python
class Node:
    def __init__(self, key=None, value=None):
        self.key = key  # key값 저장
        self.next = None  # link 저장
        self.value = value  # value값 저장 (value 없으면 생략)

    def __str__(self):
        return str(self.key)
```

* <strong>def \_\_str\_\_(self) 함수를 생성하는 이유</strong>

    : v라는 Node가 있을 때, print(v.key)는 v의 key값을 출력하는 구문이다.  

    But, __str__함수를 만든다면, print(v), 즉 Node만을 매개변수로 입력해도 v의 key값을 출력할 수 있다.

    * print(v) == print(v.\_\_str\_\_())

```python
a = Node(3)
b = Node(9)
c = Node(-1)

a.next = b
b.next = c
# c.next = None 코드는 굳이 작성할 필요 X (이미 Node Class에 정의된 부분)
```

<br/>

### 삽입 연산 구현

* 삽입 연산 함수 2가지

    * <strong>pushFront</strong> : Head Node 앞에 새로운 Node를 삽입하는 함수

    * <strong>pushBack</strong> : Tail Node 다음에 새로운 Node를 삽입하는 함수

<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="img/singly_linked_list2.png" width="550px">

```python
class SignlyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    # Head Node 앞에 새로운 Node를 삽입하는 함수
    def pushFront(self, key):
        new_node = Node(key)    # 새 Node 생성
        new_node.next = L.head      # 현 Head Node 앞에 새 Node를 연결 (link에 Head 주소 저장)
        L.head = new_node     # head Node를 새 Node로 업데이트
        L.size += 1      # 연결 리스트 크기 1 증가


    # Tail Node 다음에 새로운 Node를 삽입하는 함수
    def pushBack(self, key):
        v = Node(key)
        if len(self) == 0:
            # 연결 리스트에 Node가 0개인 상태이므로,
            # 새로 삽입되는 Node v는 Tail Node인 동시에 Head Node이다.
            self.head = v
        else:
            # 연결 리스트에 Node가 있는 상태이므로,
            # Tail Node를 알기 위해선, Head부터 link를 따라 추적하여야 한다.
            tail = self.head    # 우선, Head Node 주소를 Tail Node 주소로 가정
            while tail.next != None:
                tail = tail.next     # 그 후, link값이 None이 될 때까지 link따라 실제 Tail Node를 추적
            tail.next = v    # 찾은 Tail Node 다음에 v를 추가. 이제 v가 Tail Node이다.
        self.size += 1   # 연결 리스트  크기 1증가
```
