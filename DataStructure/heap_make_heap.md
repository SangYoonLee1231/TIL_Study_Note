# 힙 (Heap) - make_heap 연산

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
  - <a href=""></a>
  - <a href=""></a>

<br/>

## make_heap 과정

- 배열 맨 마지막 원소에 해당하는 Node부터 하나씩 탐색하면서, heap 성질을 만족하는 위치로 Node를 이동시킨다.

- 따라서 Leaf Node는 고려 대상에서 제외된다.

### heapify-down

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

### 시간복잡도

- make_heap : <code>O(n \* t)</code> = <code>O(nh)</code> = <code>O(nlogn)</code>  
   => <code>O(n)</code>

  - t = heapify_down 시간

- heapify_down : <code>O(h) \* O(1)</code> = <code>O(h)</code> = <code>O(logn)</code>

  - h = 힙의 높이

  - 최악의 경우 : heap 성질을 만족시키기 위해 root 노드가 leaf 노드까지 이동하는 경우
