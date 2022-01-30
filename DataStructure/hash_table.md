# 해시 테이블 기본 개념

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

        (key값이 2019317이면, 2019317 % 10 == 7이므로, 7번째 서랍에 자료를 저장)

        <img src="img/hash_table1.png" width="400px">

<br/>

* 이 때, 정보가 저장될 서랍장 번호를 계산하는 함수 <strong>f(key)</strong>를 <strong>해시 함수</strong>라 한다.

* 어떤 데이터를 해시 테이블에 저장하려고 할 때, 해시 함수에 의해 계산된 번호의 서랍장에 이미 다른 데이터가 있다면, 이 경우를 <strong>충돌(collision)</strong>이 발생했다고 한다.

    <img src="img/hash_table3.png">

    <br/>(2016학년도 9월 모의평가 국어 A형 비트코인 지문 中)

* 그리고 이 데이터를 저장할 다른 곳을 정하여 충돌 문제를 피하는 방법을 <strong>충돌 해결 방법(Collision Resolution Method)</strong>이라 한다.

<br/>

### 해시 테이블의 성질을 좌우하는 3가지 요소

* <strong>Table</strong> : List로 주로 관리 (크게 신경 쓸 필요 X)

* <strong>해시 함수 (Hash Function)</strong> : 어떤 좋은 해시 함수를 통해 key값을 인덱스로 맵핑할 것인가

* <strong>충돌 해결 방법 (Collision Resolution Method)</strong> : 충돌 해결 방법을 어떻게 잘 설계할 것인가

<br/>

