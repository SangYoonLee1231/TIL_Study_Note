# 해시 테이블 - 충돌 회피 방법 - Open Addressing의 Linear Probing

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 총돌 회피 방법 (Collision Resolution Method)

* 해시 함수를 아무리 잘 설계하더라도 완벽한 해시 함수가 될 수는 없으므로, 그 함수 또한 반드시 충돌이 발생하게 된다.

* 아이템을 해시 테이블에 저장하려는 곳에 이미 다른 데이터가 저장되어 있으면, 다른 장소를 찯아야 한다.

* 그 장소를 정하는 방법이 충돌 회피 방법(Collision Resolution Method)이다.

<br/>

## 대표적인 충돌 회피 방법 : open addressing

* 충돌이 발생했을 때, 주위에 빈 장소를 찾아서 데이터를 저장하는 방법이다.

### open addressing의 종류

* Linear Probing

* Quadratic Probing

* Double Hashing

<br/>

## Linear Probing

* 충돌 발생 시 빈 공간을 찾기 위해 다음 슬롯을 확인하는 방법

* 이 때, 처음 슬롯과 끝 슬롯을 이어져있다고 가정한다.

<br/>

<img src="img/hash_table6.png" width="350px"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="img/hash_table7.png" width="350px">

<img src="img/hash_table8.png" width="350px"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="img/hash_table9.png" width="350px">

* 이 때, 데이터들이 연속된 슬롯에 모여있는 것을 cluster이라 하는데, 되도록 피해야 한다.

* cluster이 많아지면 삽입 및 탐색 연산 시 시간이 더 많이 소요하기 때문이다.

### Linear Probing 연산

* search 연산

* insert 연산

* delete 연산