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

## 단방향 연결 리스트의 Node 구현

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

```python
a = Node(3)
b = Node(9)
c = Node(-1)

a.next = b
b.next = c
# c.next = None 코드는 굳이 작성할 필요 X (이미 Node Class에 정의된 부분)
```
