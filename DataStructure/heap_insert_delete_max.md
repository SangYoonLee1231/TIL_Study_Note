# 힙 (Heap) - insert와 delete_max 연산

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

### 목차

- <a href="">필기 노트</a>
- <a href=""><code>insert</code> 연산</a>
  - <a href=""><code>heapify_up</code> 연산</a>
- <a href=""><code>find_max</code> 연산</a>
- <a href=""><code>delete_max</code> 연산</a>
- <a href="">heap 연산 정리</a>
- <a href="">heap sort (힙 정렬)</a>

<br/><br/>

## 필기 노트

<img src="img/heap_insert_delete_max1.jpg" width="900">
<img src="img/heap_insert_delete_max2.jpg" width="900">

<br/>

## <code>insert</code> 연산

- <code>insert</code> 연산은 다음 두 과정을 순서대로 진행하는 연산이다.

  - 노드를 특정 위치에 삽입

  - heap 성질을 만족하도록 삽입한 노드를 이동

<br/>

- key값 n을, heap인 배열 A에 삽입하는 insert 함수 정의

  ```python
  A = [15, 12, 6, 11, 10, 2, 3, 1, 8]

  def insert(n):
    A.append(n)  # 배열 A의 끝에 key값 n을 삽입
    A.heapify_up(k)  # A[k]를 root 방향으로 이동하면서 heapify

  insert(14)
      ↓
  '''
  def insert(14):
    A.append(14)  # 배열 A의 끝에 14를 삽입
    A.heapify_up(9)  # A[9]를 root 방향으로 이동하면서 heapify
  '''
  ```

- 시간 복잡도 : <code>O(logn)</code>

<br/>

### <code>heapify_up</code> 연산

- 주어진 노드를 위로 이동하여 heap 성질을 만족하도록 하는 연산이다.

  ```python
  def heapify_up(k):  # A[k]를 heapify
    while k > 0 and A[(k - 1) // 2] < A[k]:
        A[k], A[(k - 1) // 2] = A[(k - 1) // 2], A[k]
        k = (k - 1) // 2
  ```

- 시간 복잡도 : <code>O(logn)</code>

<br/><br/>

## <code>find_max</code> 연산

- heap에서 가장 큰 값을 찾아서 리턴해주는 연산

- 즉, root node값을 리턴하면 된다. → <code>return A[0]</code>

- 시간 복잡도 : <code>O(1)</code>

<br/><br/>

## <code>delete_max</code> 연산

- heap에서 가장 큰 값(<code>A[0]</code>)을 지우고, 맨 끝 원소의 Node를 <code>A[0]</code>으로 이동하는 연산

  - <code>A[0]</code>으로 이동 → <code>heapify_down</code>

<br/><br/>

## heap 연산 정리

<br/><br/>

## heap sort (힙 정렬)
