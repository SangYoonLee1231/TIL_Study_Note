# 이진 트리 (Binary Tree)

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/binary_tree.md#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-binary-tree-1">이진 트리 (Binary Tree)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/binary_tree.md#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-traversal">이진 트리 순회 (Traversal)</a>

<br/><br/>

## 이진 트리 (Binary Tree)

- 각 노드(Node)의 자식 노드가 <strong>최대 2개까지</strong> 가능한 트리를 이진 트리라 부른다.

    <img src="img/tree_basic1.png" width="300px">

<br/><br/>

## 코드에서 이진 트리에 데이터를 저장하는 방법

### 방법1. 리스트 이용

- 이진 트리를 <strong>배열(리스트)</strong>로 표현한다. (ex. heap)

- 단점 : 메모리를 낭비할 가능성이 크다.

- 레벨1 → 레벨2 → 레벨3 → ...

  <br/>

  <img src="img/tree_basic2.png" width="300">

```python
A = [a, b, c, None, d, e, f, None, None, h, i  g, None, None, None]
```

<br/><br/>

### 방법2. 리스트 이용 - 재귀적으로 표현

    <img src="img/tree_basic3.png" width="260">

```
A = [a, [a의 왼쪽 sub tree], [a의 오른쪽 sub tree]]
```

```python
A = [ a, [ b, [], [ d, [], [] ] ] ], [ c, [ e, [], [] ], [ f, [], [] ] ]
```

<br/><br/>

### 방법3. 직접 노드를 Class로 정의

- <strong>노드 클래스를 직접 정의</strong>하고, <strong>각 노드 객체를 링크로 연결</strong>하여 표현한다.

  <img src="img/tree_basic4.png" width="210">

  <br/>

- 원하는 노드를 만들어서 그 노드를 원하는 위치에 가져다 놓고, 부모와 자식 노드를 각각 링크를 통해 연결하면 된다.

  <img src="img/binary_tree2.png" width="200"> <img src="img/binary_tree1.png" width="200">

  <br/>

- Node Class는 4개의 값을 가져야 한다.

  : <code>parent</code>, <code>key</code>, <code>left</code>, <code>right</code>

  ```python
  class Node:
      def __init__(self.key):
          self.key = key
          self.parent = self.left = self.right = None
      def __str__(self):
          return str(self.key)


  a = Node(6)
  b = Node(6)
  c = Node(1)
  d = Node(5)

  a.left = b
  a.right = c
  b.parent = c.parent = a
  b.right = d
  d.parent = b
  ```

<br/><br/>

## 이진 트리 순회 (Traversal)

- 노드들을 <strong>특정 순서</strong>에 따라 차례대로 빠지지 않고 방문하여 <strong>모든 key값을 출력하는 과정</strong>을 말한다.

- 순회하는 방법은 3가지가 있다.

    <br/>

    <img src="img/binary_tree3.png">

    <br/>

  - <strong>preorder (전위 순회)</strong> : 부모노드 → 왼쪽 자식 노드 → 오른쪽 자식 노드

    ```python
    def preorder(self):  # MLR
        if self != None:
            print(self.key)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    ```

    <br/>

  - <strong>inorder (중위 순회)</strong> : 왼쪽 자식 노드 → 부모노드 → 오른쪽 자식 노드

    ```python
    def inorder(self):  # LMR
        if self != None:
            if self.left:
                self.left.preorder()
            print(self.key)
            if self.right:
                self.right.preorder()
    ```

    <br/>

  - <strong>postorder (후위 순회)</strong> : 왼쪽 자식 노드 → 오른쪽 자식 노드 → 부모노드

    ```python
    def postorder(self):  # LRM
        if self != None:
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
            print(self.key)
    ```

<br/>

- 이진 트리의 모양을 모르는 상태에서 preorder 탐색 순서, inorder 탐색 순서 정보만으로 이진 트리의 구성을 알아낼 수 있다. (Reconstruct)
