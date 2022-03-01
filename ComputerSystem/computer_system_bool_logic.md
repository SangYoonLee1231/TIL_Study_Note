# 불 논리

<br/>

> 참고 자료 : 개발 도서 『밑바닥부터 만드는 컴퓨터 시스템』 (노암 니산, 시몬 쇼켄 저, 김진홍 옮김 / 인사이트 출판)

<br/>

### 목차

- <a href=""></a>
- <a href=""></a>

<br/>

## 도입부

- 모든 디지털 기기는 <strong>기초 논리 게이트</strong>로 구성된 칩을 탑재하여, 이를 통해 정보를 저장하고 처리한다.

* 이러한 게이트의 논리적 작동방식은, 물리적 소재와 제작 기술과 상관 없이 모든 컴퓨터에서 동일하다.

* 불 대수 → 불 함수 → (불) 게이트 순으로 학습하고, 이를 토대로 기초 논리 게이트를 이해한다.

<br/><br/>

## 불 논리

### 불 대수 (Boolean algebra)

- 불 대수는 1과 0을 다루는 대수학이다.

- 더 정확히 말하면, 참/거짓, 1/0, 예/아니오, ON/OFF 같은 2진수 불(bool) 값을 다루는 대수학이다.

- 명제의 참과 거짓을 판단하는 '논리 연산'을 다루며, '불 연산'이라고도 불린다.

<br/>

#### 대표적인 논리 연산 종류

- <code>부정 (Not)</code> : 참과 거짓을 반대로 뒤집는 연산

    <table style="text-align: center">
        <tr><td>a</td><td>out</td></tr>
        <tr><td>0</td><td>1</td></tr>
        <tr><td>1</td><td>0</td></tr>
    </table>

- <code>논리곱 (And)</code> : 두 명제가 모두 참일 때만 결과값이 참인 연산

    <table style="text-align: center">
        <tr><td>a</td><td>b</td><td>out</td></tr>
        <tr><td>0</td><td>0</td><td>0</td></tr>
        <tr><td>0</td><td>1</td><td>0</td></tr>
        <tr><td>1</td><td>0</td><td>0</td></tr>
        <tr><td>1</td><td>1</td><td>1</td></tr>
    </table>

- <code>논리합 (Or)</code> : 두 명제 중 적어도 하나가 참일 때 결과값이 참인 연산

    <table style="text-align: center">
        <tr><td>a</td><td>b</td><td>out</td></tr>
        <tr><td>0</td><td>0</td><td>0</td></tr>
        <tr><td>0</td><td>1</td><td>1</td></tr>
        <tr><td>1</td><td>0</td><td>1</td></tr>
        <tr><td>1</td><td>1</td><td>1</td></tr>
    </table>

- <code>부정 논리곱 (Nand)</code> :

    <table style="text-align: center">
        <tr><td>a</td><td>b</td><td>out</td></tr>
        <tr><td>0</td><td>0</td><td>1</td></tr>
        <tr><td>0</td><td>1</td><td>1</td></tr>
        <tr><td>1</td><td>0</td><td>1</td></tr>
        <tr><td>1</td><td>1</td><td>0</td></tr>
    </table>

- <code>부정 논리합 (Nor)</code> :

    <table style="text-align: center">
        <tr><td>a</td><td>b</td><td>out</td></tr>
        <tr><td>0</td><td>0</td><td>1</td></tr>
        <tr><td>0</td><td>1</td><td>0</td></tr>
        <tr><td>1</td><td>0</td><td>0</td></tr>
        <tr><td>1</td><td>1</td><td>0</td></tr>
    </table>

- <code>배타적 논리합 (Xor)</code> :

    <table style="text-align: center">
        <tr><td>a</td><td>b</td><td>out</td></tr>
        <tr><td>0</td><td>0</td><td>0</td></tr>
        <tr><td>0</td><td>1</td><td>1</td></tr>
        <tr><td>1</td><td>0</td><td>1</td></tr>
        <tr><td>1</td><td>1</td><td>0</td></tr>
    </table>

<br/><br/>

### 불 함수

- 불 함수는 2진수를 입력받아 2진수로 출력하는 함수이다.

- 컴퓨터는 2진수로 모든 작업을 처리하는 하드웨어이므로, 불 함수는 하드웨어 아키텍처(의 명세, 구성, 최적화)에 중심적인 역할을 한다.

### 게이트 (또는 칩)

<br/>

## 기초 논리 게이트
