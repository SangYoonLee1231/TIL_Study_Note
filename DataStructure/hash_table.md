# 해시 테이블 (Hash Table)

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 해시 테이블 (Hash Table) 소개

* 해시 테이블은 일종의 <strong>사전(dictonary)</strong>이다.

    * 해시 테이블의 데이터는 <strong>key값과 value값의 쌍</strong>으로 구성된다고 가정한다.

* <strong>평균 O(1)안에 삽입, 삭제, 탐색 연산이 모두 가능</strong>한 매우 유용한 자료구조이다.

* 매우 광범위한 분야에 사용되는, 실용성이 뛰어난 자료구조 중 하나이다.

<br/>

* 연산을 쉽게 할 수 있도록 자료를 <strong>서랍장</strong>처럼 저장한다.

    * 예를 들어, 양말과 장갑은 2번째 서랍에, 수건과 마스크는 4번째 서랍에 넣는 식이다.

      만일 수건을 찾고 싶다면, 수건이 저장된 서랍 번호를 계산을 통해 알아내고 (4번)  

        4번쨰 서랍에 들어있는 아이템들을 하나씩 비교에 수건을 찾으면 된다.

    <br/>

    * 구체적인 다른 예로, key값을 10으로 나눈 나머지에 해당하는 서랍에 자료를 저장할 수 있다.

        (key값이 2019317이면, 7번째 서랍에 자료를 저장)

        <img src="img/hash_table1.png" width="400px">

<br/>

* 이 때, <strong>정보(key값)가 저장될 서랍장 번호를 계산하는 함수 f(key)</strong> 를 <strong>해시 함수</strong>라 한다.

<br/>

## 해시 함수 (Hash Function)

* key 값을 index로 맵핑(mapping)할 때 쓰이는 함수로, f(key)로 나타낸다.

    <img src="img/hash_table2.png" width="200px">