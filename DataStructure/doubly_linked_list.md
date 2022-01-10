# 순차적 자료구조 : 양방향 연결 리스트 (Doubly Linked List)

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 양방향 연결 리스트(Singly Linked List)란

* Node들이 <strong>양쪽 방향으로 모두 연결된</strong> 연결 리스트이다.

<img src="img\doubly_linked_list1.png">

* 양방향 연결 리스트의 필요성

    * tail Node를 지우기 위해선, 직전 prev Node를 알아야 한다.

    * 그럴려면, head Node부터 차례대로 탐색해서 찾아야 하는데 (O(n) 걸림) 이는 매우 비효율적이다.

    * 만일, 뒤로 가는 link가 있다면, O(1)안에 prev Node를 찾을 수 있다. (prev link 필요성 대두)

<img src="img\doubly_linked_list2.png">

* 양방향 연결 리스트 Node의 구성 요소
    
    * key 1개 (+ 부가 데이터 value)
    
    * <strong>link 2개</strong>
        
        * next link, prev link

<br/>