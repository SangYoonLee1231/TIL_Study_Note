# 프로세스

<br/>

### 목차

- <a href=""></a>

<br/><br/>

## 프로세스란?

- 프로세스란 <strong>실행 중인 프로그램</strong>을 의미한다.

<br/>

- <strong>운영체제</strong>에서 프로세스를 <strong>관리</strong>한다.

- <strong>CPU</strong>에서 프로세스를 <strong>제어</strong>한다. 이 때 CPU는 한 번에 <strong>하나의 프로세스만</strong> 제어할 수 있다.

<br/><br/><br/>

## 프로세스의 문맥

- 프로세스가 현재 <strong>어떤 상태</strong>에서 수행되고 있는지를 정확히 규명하기 위해 필요한 정보를 '프로세스의 문맥'이라 한다.

<br/>

- 현대 컴퓨터는 여러 프로세스들이 번갈아가며 CPU를 점유하며 실행(명령이 수행)된다.

- 이때 특정 프로세스의 차례가 다시 돌아와 명령을 다시 수행하기 위해선, 이전에 어디까지 명령을 수행했는지 정확한 수행 시점과 상태를 파악하고 있어야 한다.

  - 그래야만 그 다음 과정부터 명령 수행 작업을 이어나갈 수 있기 때문이다.

<br/><br/>

### 프로세스의 문맥의 종류

- 프로세스의 문맥은 3가지로 나누어 볼 수 있다.

  1. CPU의 상태를 나타내는 <strong>하드웨어 문맥</strong> : CPU의 수행 상태

  2. <strong>프로세스의 주소 공간</strong> : 프로세스만의 주소 공간 (Code, Data, Stack)

  3. 프로세스 관련 <strong>커널 자료 구조</strong> : 여러 프로세스 관리를 위한 PCB(Process Control Block)와 Kernel stack(커널 내의 주소)

     > PCB (Process Control Block)
     >
     > 운영체제가 각 프로세스를 관리하기 위해 각 프로세스마다 하나씩 두는 자료 구조

<br/><br/><br/>

## 프로세스의 상태

- 프로세스의 상태는 3가지로 구분할 수 있다.

  1. <strong>Running</strong> : CPU의 제어권을 잡고 instruction을 수행하고 있는 프로세스의 상태

  2. <strong>Ready</strong> : 다른 모든 준비(메모리 적재 등)를 끝낸 프로세스가 CPU를 기다리는 상태

  3. <strong>Block</strong> (Blocked, Wait, Sleep) : CPU의 제어권을 주어도 당장 instruction을 수행할 수 없는 상태  
     ( ex) 디스크에서 파일을 읽어와야 하는 경우)

- 경우에 따라 아래 2가지 상태를 포함하기도 한다.

  - <strong>New (시작 상태)</strong> : 프로세스가 생성 중인 상태

  - <strong>Terminated (종료 상태)</strong> : 수행이 끝난 프로세스가 종료 중인 상태 (정리 중)

<br/><br/>

### 프로세스 상태도

<div align="center">

<img src="img/diagram_of_process_state.png" />

👉<a href="https://zangzangs.tistory.com/108">사진 출처</a>

</div>

<br/><br/><br/>

## 문맥 교환 (Context Switch)

- CPU의 제어권을 한 프로세스에서 다른 프로세스로 넘겨주는 과정이다.

- 특정 프로세스가 CPU 제어권을 넘겨주어야 하면, 그 상태(문맥)를 자신의 PCB에 저장한다.

<br/><br/><br/>

> 참고 자료
>
> <a href="https://zangzangs.tistory.com/108">[OS] 프로세스 관리, 프로세스 문맥(context)</a> (블로그 포스트)
> 이화여대 반효경 교수님의 『<a href="http://www.kocw.net/home/cview.do?cid=3646706b4347ef09#.YyUzPR6IolU.link">운영체제</a>』 강의
