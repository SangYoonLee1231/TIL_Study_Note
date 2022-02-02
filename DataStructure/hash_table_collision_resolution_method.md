# 해시 테이블 - 충돌 회피 방법 - Open Addressing의 Linear Probing

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 총돌 회피 방법 (Collision Resolution Method)

* 해시 함수를 아무리 잘 설계하더라도 완벽한(perfect) 해시 함수가 될 수는 없으므로, 그 함수 또한 <strong>반드시 충돌이 발생</strong>하게 된다.

* 아이템을 해시 테이블에 저장하려는 곳에 이미 다른 데이터가 저장되어 있으면, <strong>다른 장소를 찾아야 한다.</strong>

* <strong>그 장소를 정하는 방법</strong>이 <strong>충돌 회피 방법(Collision Resolution Method)</strong>이다.

<br/>

## 대표적인 충돌 회피 방법 : open addressing

* 충돌이 발생했을 때, 주위에 빈 장소를 찾아서 데이터를 저장하는 방법이다.

* 주위의 빈 장소를 찾는 방법에 따라 여러 종류로 설명할 수 있다.

* chainging과 대조되는 방법이다.

### open addressing의 종류

* Linear Probing

* Quadratic Probing

* Double Hashing

<br/>

## Linear Probing

* 충돌 발생 시, 빈 공간을 찾기 위해 <strong>다음 슬롯을 순차적으로 탐색</strong>하고, 먼저 찾은 빈 공간에 데이터를 저장하는 방법이다.

* 이 때, <strong>처음 슬롯과 끝 슬롯은 이어져있다</strong>고 가정한다.

<br/>

### Linear Probing 수행 방법 예시


* 해시 테이블 H의 슬롯에 하나의 값만 저장될 수 있다고 가정한다.

* 해시 테이블 H에 A5, A2, A3, B5, A9, B2, B9, C2의 값이 순서대로 저장된다.

* 각 값이 저장되는 슬롯의 번호는 알파벳 다음의 숫자이다.

<img src="img/hash_table6.png" width="350px">

<br/>

1. 먼저 A5, A2, A3을 저장한다. 그리고 B5를 저장할 차례가 되었다.  

2. B5를 5번째 슬롯에 저장하려 하는데, 이미 A5가 저장되어 있으므로 충돌이 발생했다.  
    따라서 다른 빈 슬롯을 찾아야 한다.

3. linear probing 방법에 따라 다음 6번 슬롯을 확인한다.

4. 6번 슬롯은 비어 있으므로 B5를 H[6]에 저장한다.

<img src="img/hash_table7.png" width="350px">

<br/>

5. 다음으로, A9, B2, B9을 순서대로 해시 테이블에 저장하려 한다.

6. A9은 9번째 슬롯이 비어있으므로 H[9]에 그대로 저장한다.

7. 그리고 B2는, 2번째 슬롯이 차 있으므로, linear probing에 따라 빈 공간을 탐색하여 B[4]에 저장한다.

8. 다음 B9 역시 9번째 슬롯이 차 있으므로, linear probing에 따라 빈 공간을 탐색해야 하는데,  
    처음 슬롯과 끝 슬롯은 이어져있다고 보기 때문에, 9번째의 다음 슬롯을 탐색할 땐 맨 처음인 0번째 슬롯으로 넘어간다.

9. 0번째 슬롯은 비어있으므로 B9을 H[0]에 저장한다.

<img src="img/hash_table8.png" width="350px">

<br/>

10. 마지막으로 C2를 저장할 차례다.

11. 2번째 슬롯부터 6번째 슬롯까지 전부 다 차있기 때문에, C2는 H[7]에 저장된다.

<img src="img/hash_table9.png" width="350px">

<br/>

* H[2] ~ H[7]처럼 데이터들이 연속된 슬롯에 모여있는 것을 <strong>cluster</strong>이라 한다.

* cluster이 많아지면 <strong>삽입 및 탐색 연산 시 시간이 더 많이 소요</strong>되기 때문에, 되도록 cluster이 생기지 않도록 해야 한다.

<br/>

### Linear Probing 연산

* search 연산

* insert 연산

* delete 연산