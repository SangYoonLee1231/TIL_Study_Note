# 힙 (Heap)

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

### 목차

- <a href="">힙 (Heap) 이란?</a>
- <a href="">힙의 중요한 성질</a>
- <a href="">힙 제공 연산</a>
  - <a href="">make_heap 연산</a>
  - <a href="">insert 연산</a>
  - <a href="">find_max 연산</a>
  - <a href="">delete_max 연산</a>
  - <a href=""></a>
  - <a href=""></a>

<br/>

## 힙 (Heap) 이란?

- 힙의 조건을 만족하는 이진 트리

<br/>

- ✨ 힙 조건

  - 모양 성질을 만족해야 한다.

    - 모양 성질 : 이진 트리의 각 레벨마다 노드가 좌측부터 순서대로 꽉 차있다.

  - 힙 성질을 만족해야 한다.

    - 힙 성질 : 모든 부모 노드의 key값은 자식 노드의 key값보다 같거나 크다.

    <br/>

    <img src="img/heap1.png" width="600">

<br/><br/>

## 힙의 중요한 성질

- <code>H[k]</code>의 왼쪽 자식 노드 : <code>H[2*k + 1]</code>

- <code>H[k]</code>의 오른쪽 자식 노드 : <code>H[2*k + 2]</code>

<br/>

- <code>H[x]</code>의 부모 노드 : <code>H[(x-1) // 2]</code>

<br/>

- 루트 노드(Root Node), 즉 <code>H[0]</code>엔 가장 큰 값이 있다.

<br/>

### 힙의 장점

- 내부 요소를 모두 <code>O(1)</code>시간 안에 접근할 수 있다.

- 힙의 각 레벨마다 노드가 좌측부터 순서대로 빈 공간 없이 꽉 차있으므로, (빈 공간으로 인한) 메모리 낭비가 없다.

<br/><br/>

## 힙 제공 연산

### make_heap 연산

- 이진 트리를 표현하는 임의의 배열을 힙으로 만드는 (힙 성질을 만족하도록 하는) 연산

- 밑에 소개할 3개의 연산 모두에 사용되는, 가장 기초적인 연산

- 수행 시간 : <code>O(log(n))</code>

<br/>

### insert 연산

- 힙에 새로운 값을 삽입하는 연산 (힙 성질을 벗어나지 않도록)

- 수행 시간 : <code>O(log(n))</code>

<br/>

### find_max 연산

- 힙의 최댓값 <code>H[0]</code>을 반환하는 연산

- 수행 시간 : <code>O(1)</code>

<br/>

### delete_max 연산

- 힙에서 최댓값을 <code>H[0]</code>을 제거하는 연산

- 수행 시간 : <code>O(log(n))</code>

<br/>

<br/><br/>
