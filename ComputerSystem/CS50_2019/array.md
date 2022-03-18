# 배열

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/ComputerSystem/CS50_2019/array.md#%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%A7%81">컴파일링</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/>

## 컴파일링

- C언어로 작성된 프로그램을 make나 clang 명령어를 통해 실행할 때 컴파일링 (Compiling) 이 일어난다.

<br/>

- 컴파일링은 아래 <strong>네 개의 단계</strong>를 걸쳐 일어난다.

### 전처리 (Preprocessing)

- <code>#</code>으로 시작되는 C 소스 코드는 컴피일 실행 전, <strong>전처리기가 무언가를 실행하도록 지시</strong>한다.

  - <code>#include</code> : C 소스 코드의 해당 부분을 <strong><code><></code> 안에 적힌 파일의 실제 코드로 대체</strong>한다.

<br/>

### 컴파일링 (Compiling)

- <strong>C 소스 코드를 어셈블리 코드(중간 단계)로 변환</strong>한다.

- CPU (컴퓨터의 뇌) 가 실제로 이해할 수 있는 언어에 가까워진다.

- 어셈블리 코드엔 CPU가 실제로 이해할 수 있는 매우 기초적인 수준의 명령어가 포함되어 있다.

<br/>

### 어셈블링 (Assembling)

- <strong>어셈블리 코드를 머신 언어(0과 1로 구성)로 변환</strong>한다.

- '어셈블러'라는 프로그램이 수행한다.

<br/>

### 링킹 (Linking)

- 소스 프로그램에 사용된 모든 파일을 하나의 큰 오브젝트 코드 (머신 코드) 파일로 합치는 과정이다.

- clang 명령어를 매 파일마다 실행하도록 하는 것을 방지한다.
