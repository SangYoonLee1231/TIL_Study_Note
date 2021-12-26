# 순차적 자료구조 : 배열 vs 리스트

<br/>

>  참고 자료 : 「자료구조」 학부 수업 및 <a href="https://youtube.com/playlist?list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK">유튜브 강의</a> (신찬수 교수님)

<br/>

## 배열 (Array) - C언어

* 배열은 같은 자료형의 변수로 이루어진 요소가 모여 직선 모양으로 줄지어 있는 자료구조다.

* 인덱스(index)를 통해 값 접근 가능하다.

* 【읽기】와 【쓰기】를 연산으로 제공한다. (수행시간 = O(1))

<img src="img/array1.png">

* 배열 A에 해당하는 변수엔 A[0]의 첫 번째 byte의 주소가 저장된다.

> ※ 배열에서 수

<br/>

## 리스트 (List) - 파이썬

* 리스트(List)는 배열과 동일하게 같은 자료형의 변수를 모은 자료구조로, 인덱스(index)를 통해 값 접근 가능하다.

* 그러나, 배열보다 훨씬 더 <strong>다양하고 유용한 연산</strong>을 제공한다.

<img src="img/list1.png">

* 리스트의 각 요소의 실제 값은 다른 메모리에 객체 형태로 저장되어 있다.

* 리스트의 각 요소는 이 객체들의 주소를 가리킨다.

<br/>

## 리스트(List)의 또 다른 특징 - Dynamic Array

* 리스트는 배열과 달리, 자신의 용량을 <strong>자동으로 조절</strong>한다. (리스트를 Dyanamic Array라고도 부르는 이유)
