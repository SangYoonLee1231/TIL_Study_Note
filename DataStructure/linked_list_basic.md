# 순차적 자료구조 : 연결 리스트 (Linked List) 기본 개념

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 연결 리스트란

* Node들이 link로 연결된 자료 구조이다.

<img src="img/linked_list1.png">

<br/>

* 연결 리스트는 값을 저장하는 각각의 공간이 <strong>메모리 상에 흩어져 있다</strong>.
    
    * 연속된 메모리 공간에 값을 저장하는 배열과 다름

* 어떤 값의 다음 위치에 있는 값을 알기 위해선, 한 공간에 <strong>2개의 정보</strong>를 저장해야 한다. 이 공간을 <strong>노드(Node)</strong>라 부른다.

    * 2개의 정보 = 어떤 값 + 그 다음 값이 저장된 메모리의 주소

    * <strong>노드(Node) = 값(data, key) + 다음 값의 주소(link)</strong>

<br/>

* (반복) <strong>연결 리스트란 Node들이 link로 연결된 자료 구조</strong>이다.

* 연결 방향에 따라 <strong>한방향 연결 리스트</strong>, <strong>양방향 연결 리스트</strong>로 구분할 수 있다.

<br/>

## 연결 리스트의 장단점 (vs 배열)

* 배열과 달리, <strong>어떤 값에 접근 시, 상수 시간 O(1) 내에 수행할 수 없다</strong>는 단점이 있다.

* 그러나 <strong>새로운 값을 중간에 삽입하는 과정은 배열보다 더 빨리 걸린다</strong>.

    * 배열 insert 수행시간 : <strong>O(n)</strong>

    * 연결 리스트 insert 수행시간 : <strong>O(1)</strong>

<img src="img/linked_list2.png" width="250px"> <img src="img/linked_list3.png" width="400px">  
\<배열> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \<연결 리스트>
