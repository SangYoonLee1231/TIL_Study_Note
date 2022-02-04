## 트리 기본 개념

* <strong>부모 - 자식</strong> 간의 관계에 따라 자료를 구성하는 자료구조

* 순서에 따라 자료가 저장되는 자료구조와 다른 개념이다.

* 연결 리스트 (Linked List) 는 자식 노드가 0개 또는 1개인 트리의 특별한 경우로 볼 수 있다.

<br/>

## 이진 트리 (Binary Tree)

* 자식 노드가 최대 2개까지 가능한 트리

    <img src="img/tree_basic1.png" width="300px">

<br/>

### 용어 정리

* <strong>노드 (Node)</strong>

* <strong>링크 (Link) or 에지 (Edge) or 간선</strong> : 부모 노드와 자식 노드를 잇는 연결 고리

* <strong>루트 노드 (Root Node)</strong> : 맨 꼭대기에 있는, 모든 노드의 조상이 되는 노드

* <strong>리프 노드 (Leaf Node)</strong> : 자식이 없는 노드

<br/>

* <strong>부모 노드 (Parent Node)</strong> : 자신과 링크로 바로 연결된, 바로 윗 레벨에 있는 노드

* <strong>자식 노드 (Child Node)</strong> : 자신과 링크로 바로 연결된, 바로 아래 레벨에 있는 노드

* <strong>형제 노드</strong> : 자신과 같은 세대에 있는 노드. 서로 레벨값이 동일하다.

<br/>

* <strong>레벨 (Level)</strong> : 루트 노드를 레벨 1으로 두고 한 세대씩 내려가면서 1씩 증가하는 수치. 노드 개수가 기준이라고 한다.

* <strong>깊이 (Depth)</strong> : 루트 노드를 레벨 0으로 두고 한 세대씩 내려가면서 1씩 증가하는 수치. 간선 개수가 기준이라고 한다.

* <strong>높이 (Height)</strong> : 레벨과 반대로 리프 노드를 0으로 두고 한 세대씩 올라가면서 1씩 증가하는 수치

<br/>

* <strong>경로 (Path)</strong> : 어떤 두 노드 사이를 연결하는 노드의 순서

    * ex) 3 → 2 → 7 → 8 → 12 : 노드 3 → 12로 가는 경로

* <strong>경로 길이 (Path Length)</strong> : 경로의 애지 개수

    * ex) 경로 3 → 2 → 7 → 8 → 12 : 경로 길이 = 4

<br/>


    트리의 레벨 (Level) 개념이 조금 헷갈린다. 교수님은 루트 노드의 레벨을 0으로 두고 설명하시는데, 막상 검색으로 찾아보니 거의 모든 블로그가 루트 노드의 레벨을 1로 설명한다.

<br/>

### 코드에서 이진 트리에 데이터를 저장하는 방법

* 방법1. 리스트 이용

    * 레벨1 → 레벨2 → 레벨3 → ...

    <br/>

    <img src="img/tree_basic2.png" width="350">

    ```python
    A = [a, b, c, Node, d, e, f, None, None, h, i  g, None, None, None]
    ```

<br/>

* 방법2. 리스트 이용 - 재귀적으로 표현


* 방법3. 직접 노드를 Class로 정의