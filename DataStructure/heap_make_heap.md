# 힙 (Heap) - <code>make_heap</code> 연산

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/heap_make_heap.md#%ED%95%84%EA%B8%B0-%EB%85%B8%ED%8A%B8">필기 노트</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/heap_make_heap.md#make_heap-%EA%B3%BC%EC%A0%95"><code>make_heap</code> 과정</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/heap_make_heap.md#heapify-down"><code>heapify-down</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/heap_make_heap.md#%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84">시간복잡도</a>

<br/><br/>

## 필기 노트

<img src="img/heap_make_heap1.jpg" width="900">
<img src="img/heap_make_heap2.jpg" width="900">

<br/>

## <code>make_heap</code> 과정

- 배열 맨 마지막 원소에 해당하는 Node부터 하나씩 탐색하면서, heap 성질을 만족하는 위치로 Node를 이동시킨다.

- 따라서 Leaf Node는 고려 대상에서 제외된다.

<br/>

### <code>heapify-down</code>

- 어떤 Node를 자식 노드와 서로 비교하며 heap 성질을 만족하는 위치로 내려보내는 함수

  ```python
  A = [2, 8, 6, 1, 10, 15, 3, 12, 11]

  def make_heap(A):
      n = len(A)
      for k in range(n-1, -1, -1):
          # A[k]를 heap 성질 만족시키는 곳으로 이동
          heapify_down(k, n)
  ```

  ```python
  def heapify_down(k, n):
      while A[k] != leaf node:
          L, R = 2*k + 1, 2*k + 2
          m = index(A[k], A[L], A[R])
                  # 이 3개 중 최댓값 index가 m으로 전달
          if k != m:
              A[k], A[m] = A[m], A[k]
              k = m
          else:
              break
  ```

<br/>

### 시간복잡도

- <code>make_heap</code> 함수 : <code>O(n \* t)</code> = <code>O(nh)</code> = <code>O(nlogn)</code>  
   => <code>O(n)</code>

  - <code>t</code> = heapify_down 시간

<br/>

- <code>heapify_down</code> 함수 : <code>O(h) \* O(1)</code> = <code>O(h)</code> = <code>O(logn)</code>

  - <code>h</code> = 힙의 높이

  - 최악의 경우 : heap 성질을 만족시키기 위해 root 노드가 leaf 노드까지 이동하는 경우
