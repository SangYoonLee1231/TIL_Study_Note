# 연결 리스트 - 기본 개념

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/linked_list_basic.md#%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8-linked-list-%EB%93%B1%EC%9E%A5-%EB%B0%B0%EA%B2%BD">연결 리스트 (Linked List) 등장 배경</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/linked_list_basic.md#%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8-linked-list-%EC%86%8C%EA%B0%9C">연결 리스트 (Linked List) 소개</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/linked_list_basic.md#%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EC%9E%A5%EB%8B%A8%EC%A0%90-vs-%EB%B0%B0%EC%97%B4">연결 리스트의 장단점 (vs 배열)</a>

<br/><br/>

## 연결 리스트 (Linked List) 등장 배경

- 배열의 삽입과 삭제 연산 수행 시간은 <code>O(n)</code>이다. 이는 삽입과 삭제가 자주 일어나는 상황에선 비효율적일 수 있다.

- 이런 문제를 해결하기 위해 <strong>연결 리스트</strong>라는 새로운 자료구조가 등장한다.

<br/>

- 연결 리스트는 탐색 할 때 <code>O(n)</code>만큼 걸리지만, <strong>삽입과 삭제 연산은 <code>O(1)</code>만에 수행</strong>할 수 있으므로 삽입과 삭제가 잦은 상황에 자주 사용된다.

<br/><br/>

## 연결 리스트 (Linked List) 소개

- 연결 리스트 (Linked List)는 <strong>Node들이 link로 연결된 형태의 자료 구조</strong>이다.

  <img src="img/linked_list1.png">

<br/>

- 연결 리스트는 값을 저장하는 각각의 공간이 <strong>메모리 상에 흩어져 있다</strong>.

  - 연속된 메모리 공간에 값을 저장하는 배열과 다르다.

<br/>

- 어떤 값과 그 다음 위치에 있는 값을 알기 위해선, 한 공간에 <strong>2개의 정보</strong>를 저장해야 한다. 이 공간을 <strong>노드(Node)</strong>라 부른다.

- <strong>노드(Node)</strong>는 <strong>데이터를 담는 하나의 창구</strong>이다.

  - <strong>노드(Node)</strong> = <strong>값(data, key)</strong> + <strong>다음 값의 주소(link)</strong>

<br/>

- (반복) 연결 리스트란 Node들이 link로 연결된 자료 구조이다.

- Node들이 서로 어떻게 연결되어 있는지에 따라 <strong>단방향 연결 리스트</strong>, <strong>양방향 연결 리스트</strong>로 구분할 수 있다.

<br/><br/>

## 연결 리스트의 장단점 (vs 배열)

- 배열과 달리, 연결 리스트는 <strong>어떤 값에 접근 시, 상수 시간 O(1) 내에 수행할 수 없다</strong>는 단점이 있다.  
  (<code>O(n)</code>만큼 걸린다)

<br/>

- 그러나 <strong>새로운 값을 중간에 삽입하는 과정</strong>은 배열보다 더 빨리 걸린다.

  - 배열 <code>insert</code> 수행시간 : <strong>O(n)</strong>

  - 연결 리스트 <code>insert</code> 수행시간 : <strong>O(1)</strong>

<img src="img/linked_list2.png" width="250px"> <img src="img/linked_list3.png" width="400px">  
\<배열> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \<연결 리스트>

<br/><br/>

> 사진 출처 : https://ehclub.co.kr/1228 , <a href="https://youtu.be/sMpsvA5O0xU">신찬수 교수님 유튜브 강의</a>
