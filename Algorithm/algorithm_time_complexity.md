# 시간 복잡도

<br/>

> 참고 자료 : 「알고리즘」 학부 수업 자료 (신찬수 교수님)

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Algorithm/algorithm_time_complexity.md#%EA%B0%80%EC%83%81-%EC%BB%B4%ED%93%A8%ED%84%B0%EC%9D%98-%ED%95%84%EC%9A%94%EC%84%B1">가상 컴퓨터의 필요성</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Algorithm/algorithm_time_complexity.md#%EA%B0%80%EC%83%81-%EC%BB%B4%ED%93%A8%ED%84%B0">가상 컴퓨터</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Algorithm/algorithm_time_complexity.md#%EA%B8%B0%EB%B3%B8-%EC%97%B0%EC%82%B0">기본 연산</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## 가상 컴퓨터의 필요성

- 자료구조와 알고리즘은 <strong>코드</strong>로 구현되고, 이 코드는 <strong>컴퓨터</strong> 위에서 돌아간다.

<br/>

- 그러나 각 컴퓨터마다 <strong>HW(하드웨어)와 SW(소프트웨어)의 환경이 상이</strong>하고, 이는 알고리즘의 성능에 큰 문제가 된다.

  - 문제 1. 똑같은 알고리즘을 똑같은 언어로 구현하더라도 SW / HW 환경에 따라 <strong>성능이 달라진다</strong>.

  - 문제 2. <strong>다양한 입력</strong>에 따라 내가 작성한 코드가 얼마나 빨리 동작하는 객관적으로 측정할 수 없다.

<br/>

- 따라서, 이런 <strong>SW / HW 환경에 구애받지 않는 좀 더 객관적인 컴퓨터 모델을 가정</strong>할 필요가 있다.

- 하지만, 실제 그런 모델을 존재하지 않는다.

- 그러므로, 대신 HW / SW 환경과 독립적인 <strong>가상 컴퓨터 (Virtual Machine)</strong> 를 정의하고, 그 위에서 <strong>가상 언어 (Psuedo Language)</strong> 로 작성된 <strong>가상 코드 (Psuedo Code)</strong> 를 통해 알고리즘의 수행 시간을 측정하여 비교한다.

<br/><br/>

## 가상 컴퓨터

- 가상 컴퓨터를 통해 누구나 같은 환경에서 여러 알고리즘들을 객관적으로 비교할 수 있다.

<br/>

- 컴퓨터의 초기 모델 : Turing Machine

- 현대적 컴퓨터 모델 : <strong>RAM (Random Access Machine)</strong> &nbsp; (폰 노이만 (von Neumann) 이 제시)

<br/>

- <strong>RAM 모델 = CPU + Memory + Code (기본 연산들로 구성)</strong>

  - 프로그램과 프로그램이 다루는 모든 데이커가 Memory 상에 올라간다.

  - CPU가 그 Memory에 접근하여 데이터를 읽고, 쓰고, 변형시켜 원하는 값을 만들어낸다.

  - Code가 Memory에 들어있는 데이터를 어떤 식으로 가공할 지 결정을 내린다.

  - 이 Code는 <strong>기본 연산</strong>들로 구성되어 있다.

<br/><br/>

## 기본 연산

- <strong>단위 시간 내</strong>에 수행되는 가장 기본적인 연산이다.

<br/>

- 기본 연산 종류 (모두 <strong><code>1</code>시간 내에 수행</strong>된다 가정)

  - <strong>배정, 대입, 복사 연산 : <code>A = B</code></strong>

  - <strong>산술 연산 : <code>+</code>, <code>-</code> ,<code>\*</code>, <code>/</code></strong>

    - 나머지(<code>%</code>), 올림, 버림, 반올림 연산은 기본 연산으로 정의하진 않지만, 단위 시간 내에 수행된다고 가정한다.

  - <strong>비교 연산 : <code>></code>, <code>>=</code>, <code><</code>, <code><=</code>, <code>==</code>, <code>!=</code></strong>

    - <code>A < B</code> <=> <code>A - B < 0</code> : 두 수를 비교하는 것은 뺄셈 연산을 1번 수행하는 것과 같다.

  - <strong>논리 연산 : <code>AND</code>, <code>OR</code>, <code>NOT</code></strong>

  - <strong>비트 연산 : <code>bit-AND</code>, <code>OR</code>, <code>NOT</code></strong>
