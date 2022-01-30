# 해시 테이블 (Hash Table) - 충돌 회피 방법 (Collision Resolution Method) - Open Addressing의 Linear Probing 위주

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 총돌 회피 방법

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

<img src="img/hash_table6.png" width="350px"> <img src="img/hash_table7.png" width="350px">

<img src="img/hash_table8.png" width="350px"> <img src="img/hash_table9.png" width="350px">