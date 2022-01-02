# 순차적 자료구조 : 큐 (Queue)

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 큐 (Queue)

* 1차원의 선형(linear) 자료구조로 Stack과 유사하다.

* 2가지 기본 연산을 제공한다. (다른 추가 연산도 제공)

    * 기본 연산 : <strong>enqueue(삽입), dequeue(삭제)</strong>

    * 추가 연산 : <strong>isEmpty, front, len</strong>

* <strong>FIFO : First In First Out</strong>

    * 처음으로 들어온 요소가 제일 먼저 나간다.

<img src="img/queue1.png">

<br/>

## Queue 활용 예제

* <a href="https://www.acmicpc.net/problem/1158" target="_blank">Josephus Problem (백준 1158번)</a>