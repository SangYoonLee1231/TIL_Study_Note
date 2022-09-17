# 프로세스와 스레드

<br/>

### 목차

- 프로세스 (Process)
  - <a href="">프로세스 (Process) 란?</a>
  - <a href="">프로세스의 문맥</a>
    - <a href="">프로세스의 문맥의 종류</a>
  - <a href="">프로세스의 상태</a>
    - <a href="">프로세스 상태도</a>
  - <a href="">문맥 교환 (Context Switch)</a>
  - <a href="">스케줄러 (Scheduler)</a>
- 스레드 (Thread)
  - <a href="">스레드 (Thread) 란?</a>
  - <a href="">싱글 스레드 VS 멀티 스레드</a>
    - <a href="">멀티 스레드의 장점</a>

<br/><br/>

## 프로세스 (Process) 란?

- 프로세스란 <strong>실행 중인 프로그램</strong>을 의미한다.

<br/>

- <strong>운영체제</strong>에서 프로세스를 <strong>관리</strong>한다.

- <strong>CPU</strong>에서 프로세스를 <strong>제어</strong>한다. 이 때 CPU는 한 번에 <strong>하나의 프로세스만</strong> 제어할 수 있다.

<br/><br/><br/>

## 프로세스의 문맥

- 프로세스가 현재 <strong>어떤 상태</strong>에서 수행되고 있는지를 정확히 규명하기 위해 필요한 정보를 '프로세스의 문맥'이라 한다.

<br/>

- 현대 컴퓨터는 여러 프로세스들이 번갈아가며 CPU를 점유하고 그 프로세스의 명령을 수행한다.

- 이 때 특정 프로세스의 CPU 점유 차례가 다시 되돌아오면, 이전에 어디까지 명령을 수행했는지 그 정확한 시점과 상태를 알고 있어야 명령 수행을 정상적으로 재개할 수 있다.

<br/><br/>

### 프로세스의 문맥의 종류

- 프로세스의 문맥은 3가지로 나누어 볼 수 있다.

  1. CPU의 상태를 나타내는 <strong>하드웨어 문맥</strong> : CPU의 수행 상태

  2. <strong>프로세스의 주소 공간</strong> : 프로세스만의 주소 공간 (Code, Data, Stack)

  3. 프로세스 관련 <strong>커널 자료 구조</strong> : 여러 프로세스 관리를 위한 PCB(Process Control Block)와 Kernel stack(커널 내의 주소)

     > PCB (Process Control Block)
     >
     > 운영체제가 여러 프로세스를 관리하기 위해 각 프로세스마다 하나씩 두는 자료 구조

<br/><br/><br/>

## 프로세스의 상태

- 프로세스의 상태는 3가지로 구분할 수 있다.

  1. <strong>Running</strong> : CPU의 제어권을 잡고 instruction을 수행하고 있는 프로세스의 상태

  2. <strong>Ready</strong> : 다른 모든 준비(메모리 적재 등)를 끝낸 프로세스가 CPU를 기다리는 상태

  3. <strong>Block</strong> (Blocked, Wait, Sleep) : CPU의 제어권을 주어도 당장 instruction을 수행할 수 없는 상태  
     ( ex) 디스크에서 파일을 읽어와야 하는 경우 )  
     (즉 어딘가에서 프로세스는 계속 일하는 중이다.)

- 경우에 따라 아래 2가지 상태를 포함하기도 한다.

  - <strong>New (시작 상태)</strong> : 프로세스가 생성 중인 상태

  - <strong>Terminated (종료 상태)</strong> : 수행이 끝난 프로세스가 종료 중인 상태 (정리 중)

  - <strong>Suspended</strong> : 외부적인 이유로 프로세스의 수행이 정지된 상태 (By 사용자 or 중기 스케줄러)

<br/><br/>

### 프로세스 상태도

<div align="center">

<img src="img/diagram_of_process_state.png" />

👉<a href="https://zangzangs.tistory.com/108">사진 출처</a>

</div>

<br/><br/><br/>

## 문맥 교환 (Context Switch)

- CPU의 제어권을 한 프로세스에서 다른 프로세스로 넘겨주는 과정이다.

- 특정 프로세스가 CPU 제어권을 넘겨줄 때, 현재 상태(문맥)를 자신의 PCB에 저장한다.

- 그리고 자신의 차례가 되돌아오면, 저장했던 문맥을 PCB에서 찾아 하드웨어에 다시 복원시킨다.

<br/><br/><br/>

## 스케줄러 (Scheduler)

- 프로세스들의 동작 순서를 잡아주는 역할

<br/>

- <strong>단기 스케줄러 (Short-Term Scheduler / CPU Scheduler)</strong>

  - 어떤 프로세스를 다음 번에 Running 할 지 결정하는 스케줄러

- <strong>중기 스케줄러 (Medium-Term Scheduler / Swapper)</strong>

  - 어떤 프로세스가 시작되면 바로 메모리에 적재

  - 만일 너무 많은 프로세스가 메모리에 올려져 있으면, 여유 공간을 마련하기 위해 일부 프로세스를 메모리에서 디스크로 쫓아낸다.

    - 쫓겨난 프로세스는 Suspend 상태가 된다.

  - 이렇게 하여 메모리에 올려진 프로세스 수를 조절한다. (Degree Of Multiprogramming을 제어) → 시스템 성능 향상

<br/><br/><br/>

## 스레드 (Thread) 란?

- 보통 하나의 프로세스는 하나의 CPU 실행 단위를 갖는다.

- 그러나 프로세스 하나의 내부에 CPU 실행 단위를 여러 개 둘 수도 있는데, 이 각각을 <strong>스레드 (Thread)</strong> 라 한다.

<br/>

- 동일한 일을 수행하는 여러 개의 프로세스가 필요할 때, 대신 하나의 프로세스만을 생성하고 그 안에 여러 개인 스레드(CPU 실행 단위)를 두는 방식으로 자원 낭비를 줄일 수 있다.

  - 이를 <strong>Lightweight Process</strong>라 부른다.

  - 자원 낭비가 절약되는 이유는, 모든 프로그램은 메모리에 적재가 되어야 실행이 가능하기 때문에, 프로세스 수를 줄이기 되면 그만큼 곧 메모리 자원 소모도 줄어들기 때문이다.

<br/>

- 각 스레드의 구성 : Program Counter + Register Set + Stack Space

- 스레드끼리 공유하는 부분을 <strong>Task</strong>라 부른다. (코드와 데이터 및 여러 자원)

<br/><br/><br/>

## 싱글 스레드 VS 멀티 스레드

- <strong>싱글 스레드</strong> : 한 프로세스에 하나의 스레드

- <strong>멀티 스레드</strong> : 한 프로세스에 여러 개의 스레드

<br/><br/>

### 멀티 스레드의 장점

- <strong>빠른 응답성 (Responsiveness)</strong> : 하나의 스레드가 Blocked 상태인 동안에도 동일한 Task 내의 다른 스레드가 실행(Running 상태)가 되어 빠른 처리를 할 수 있다.

- <strong>자원 공유 (Resource Sharing)</strong> : 만일 같은 일을 하는 프로세스가 여러 개 수행된다면, 그만큼 메모리 소모가 심해진다. 대신 하나의 프로세스에 여러 개의 스레드만 두면, 자원을 공유하는 부분이 생기게 되어 자원 절약 및 성능 향상의 효과를 얻을 수 있다.

- <strong>경제성 (Economy)</strong> : 하나의 새 프로세스를 생성하고 문맥 교환이 일어나는 것보다, 스레드를 하나 생성하고 스레드 간의 문맥 교환이 일어나는 것이 더 효율적이다. (Overhead가 덜 든다.)

- <strong> (Utilization of MultiProcessor Architectures)</strong> : CPU가 여려 개 있는 컴퓨터일 경우, 각 스레드를 (병렬적으로) 동시에 실행할 수 있어 더욱 빠른 결과를 얻을 수 있다.

<br/><br/><br/>

> 참고 자료
>
> <a href="https://zangzangs.tistory.com/108">[OS] 프로세스 관리, 프로세스 문맥(context)</a> (블로그 포스트)  
> 이화여대 반효경 교수님의 『<a href="http://www.kocw.net/home/cview.do?cid=3646706b4347ef09#.YyUzPR6IolU.link">운영체제</a>』 강의
