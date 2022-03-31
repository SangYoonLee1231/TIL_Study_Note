# 이진 탐색 트리 (Binary Search Tree / BST)

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

### 목차

- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## 이진 탐색 트리란?

- <strong>부모의 왼쪽 서브 트리 (모든) Node들은 부모보다 값이 작고, 오른쪽 서브 트리 (모든) Node들은 부모보다 값이 큰 이진 트리</strong>

    <img src="img/binary_search_tree1.png" width="800">

<br/>

- 다음은 6의 값을 갖는 노드로 인해 이진 탐색 트리가 아니다.

    <img src="img/binary_search_tree2.png" width="800">

<br/><br/>

## 이진 탐색 트리의 탐색

- 이진 탐색 트리에 어떤 값 x가 있는지 찾고자 한다.

- 우선 루트 노드와 x값을 비교한다.

  - 루트 노드 기준으로 x값이 더 크면, 우측 서브 트리에 x가 있을 가능성이 있으므로, 우측으로 이동한다.

  - 루트 노드 기준으로 x값이 더 작으면, 좌측 서브 트리에 x가 있을 가능성이 있으므로, 좌측으로 이동한다.

  - 이 과정을 반복한다.

  <img src="img/binary_search_tree3.gif">

<br/>

- <strong>수도 코드로 구현</strong>

  ```python
  function bst.search(x)
      set node = bst.root                     # root에서 시작합니다.
      while node != null and node.value != x  # node에 들어있는 값이 x가 되기 전까지 계속 반복합니다.
          if node.value > x                   # 노드에 있는 값이 x보다 크다면
              node = node.left                # 왼쪽 자식으로 내려와 탐색을 진행합니다.
          else                                # 노드에 있는 값이 x보다 작다면
              node = node.right               # 오른쪽 자식으로 내려와 탐색을 진행합니다.

      return node                             # 최종 위치를 반환합니다.
  ```

<br/><br/>

## 이진 탐색 트리의 삽입

<br/><br/>

> 사진 출처 : <a href="https://youtu.be/kGZoEShMcSQ">신찬수 교수님 유튜브 강의</a>, <a href="https://www.codetree.ai/missions">Code Tree - Novice High</a>
