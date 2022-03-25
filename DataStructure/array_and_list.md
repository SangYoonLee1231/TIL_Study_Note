# 순차적 자료구조 : 배열 vs 리스트

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/array_and_list.md#%EB%B0%B0%EC%97%B4-array---c%EC%96%B8%EC%96%B4">배열 (Array) - C언어</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/array_and_list.md#%EB%A6%AC%EC%8A%A4%ED%8A%B8-list---%ED%8C%8C%EC%9D%B4%EC%8D%AC">리스트 (List) - 파이썬</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/array_and_list.md#%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%8A%94-dynamic-array%EB%8F%99%EC%A0%81-%EB%B0%B0%EC%97%B4%EC%9D%B4%EB%8B%A4">리스트는 Dynamic Array(동적 배열)이다.</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/array_and_list.md#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%82%B0-%EC%88%98%ED%96%89%EC%8B%9C%EA%B0%84">리스트 연산 수행시간</a>

<br/><br/>

## 배열 (Array) - C언어

- 배열은 같은 자료형의 변수가 모여, 직선 모양으로 줄지어 있는 <strong>선형(linear) 자료구조</strong>다.

- <strong>연속적인 메모리 공간을 할당</strong>하여 데이터를 저장한다.

- 【읽기】와 【쓰기】만을 연산으로 제공한다. (제한된 자료구조)

<br/>

- 배열의 이름과 동일한 변수 A에 A[0]의 첫 번째 byte의 주소가 저장된다.

  <img src="img/array1.png">

<br/>

- 배열은 <strong>인덱스(index)</strong>를 통해 각각의 값에 <strong>매우 빠르게</strong> 접근할 수 있다.

  - 수행시간 = <strong><code>O(1)</code> (RAM : Random Access Memory)</strong>

  - 배열의 시작 주소, 데이터 타입, 인덱스 3가지 정보만으로 값이 저장된 곳의 주소를 단위 시간 내에 계산할 수 있다.

<br/><br/>

## 리스트 (List) - 파이썬

- 리스트는 배열처럼 여러 변수를 모은 자료구조이나, 배열과 달리 한 리스트에 <strong>다른 자료형</strong>의 값들이 있어도 된다.

- 배열과 함께 대표적인 <strong>1차원의 선형(linear) 자료구조</strong>다.

<br/>

- 리스트의 각 요소의 실제 값은 다른 메모리에 객체 형태로 저장되어 있다.

- 리스트의 각 요소는 이 객체들의 주소를 가리킨다.

  <img src="img/list1.png">

<br/>

- 리스트 역시 <strong>인덱스(index)</strong>를 통해 각각의 값에 <strong>매우 빠르게</strong> 접근 가능하다.

  - 수행시간 = <strong><code>O(1)</code> </strong>

<br/>

- ✨ 그러나 배열과 달리 <strong>메모리 공간을 배열처럼 연속적으로 할당하지 않는다.</strong>

- 리스트는 값을 저장하는 각각의 공간이 <strong>메모리 상에 흩어져 있다</strong>.

  그럼에도 각각의 값에 접근할 때 걸리는 시간은 <code>O(1)</code>이다.

<br/>

### 리스트의 다양한 연산

- 리스트는 배열보다 훨씬 더 <strong>다양하고 유용한 연산</strong>을 제공한다. (리스트의 장점)

<br/>

- 【삽입】 <code>A.append(6)</code> : 맨 뒤에 6을 삽입

- 【삽입】 <code>A.insert(1, 10)</code> : A[1]에 10을 삽입

<br/>

- 【삭제】 <code>A.pop()</code> : 마지막 요소를 지우고 해당 값을 리턴

- 【삭제】 <code>A.pop(1)</code> : A[1]을 지우고 해당 값을 리턴

- 【삭제】 <code>A.remove(value)</code> : A에서 해당 value값 찾아서 제거 (2개 이상 존재 시 첫 번째만 제거)

<br/>

- 【탐색】 <code>A.index(value)</code> : A에서 해당 value값 찾아서 그 요소의 index를 리턴

- 【탐색】 <code>A.count(value)</code> : A에서 해당 value값을 가진 요소의 개수 리턴

<br/><br/>

## 리스트는 Dynamic Array(동적 배열)이다.

- 리스트는 배열과 달리, <strong>자신의 용량을 자동으로 조절한다.</strong> (리스트를 Dyanamic Array라고도 부르는 이유)

```python
import sys

A = [] # 빈 리스트
print(sys.getsizeof(A)) # 28 bytes

A.append(18) # A = [18]
print(sys.getsizeof(A)) # 44 bytes
```

- 파이썬에선, 자동으로 리스트의 공간이 모자르면 크기를 늘리고, 반대로 공간이 남으면 크기를 줄이는 작업을 수시로 한다.  
  (메모리 자동 조절 기능)

<br/>

<img src="img/list2.png">

```python
A.append(x):
    if A.n < A.capacity:
        # 리스트 용량이 넉넉한 경우
        A[n] = x
        A.n = n + 1
    else: # A.n == A.capacity
        # 리스트 용량이 더 필요한 경우 (자동으로 용량 크기 ↑)
        B = A.capacity * 2 # B는 임시용 리스트, *2는 용량을 늘린다는 의미
        for i in range(n):
            B[i] = A[i]
        A = B
        del B
        A[n] = x
        A.n = n + 1
```

<br/>

- 동적 배열은 굉장히 매력적인 자료구조 이지만 크기가 고정되어 있는 문제의 경우에는 정적 배열과 같은 양의 데이터를 저장하고 있음에도 불구하고 정적 배열보다는 더 많은 메모리를 사용하게 된다.

- 따라서 항상 동적 배열은 사용하는 것이 효과적이라고 말하기는 어렵다.

<br/><br/>

## 리스트 연산 수행시간

- 동적 배열에서 삽입, 삭제, 탐색하는 과정은 모두 정적 배열과 동일하기 때문에 시간복잡도는 완전히 일치하지만, 메모리를 필요한 만큼만 사용한다는 차이가 있다.

<br/>

- <code>A.append</code> , <code>A.pop</code> : <strong>O(1) 평균</strong>

- <code>A.insert</code> , <code>A.remove</code> : <strong>O(n) Worst Case</strong>

- <code>A.index</code> , <code>A.count</code> : <strong>O(n) Worst Case</strong>

<br/><br/>

> 사진 출처 : <a href="https://youtu.be/Lqd8o7vL2Z8">신찬수 교수님 유튜브 강의</a>
