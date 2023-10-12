# 2. OS의 역사

<br/>

> 참고 자료 : '운영체제' 학부 수업 자료 (이윤석 교수님)

- 📔 <strong><a href="https://drive.google.com/file/d/1TxI6KTJy-1fH4e1DFlgcXPIVdxS11tg3/view?usp=sharing">강의 내용 필기 노트 보러가기 (Lec 1)</a></strong>

<br/><br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/2-os-history.md#early-systems">Early Systems</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/2-os-history.md#batch-processing-systems-%EC%9D%BC%EA%B4%84-%EC%B2%98%EB%A6%AC-%EC%8B%9C%EC%8A%A4%ED%85%9C">Batch Processing Systems (일괄 처리 시스템)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/2-os-history.md#multi-programming-systems">Multi-programming Systems</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/2-os-history.md#time-sharing-multi-tasking-systems-3%EC%84%B8%EB%8C%80">Time Sharing (Multi-tasking) Systems (3세대)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/2-os-history.md#4%EC%84%B8%EB%8C%80-systems">4세대 Systems</a>

<br/><br/>

## Early Systems

- 1920, 30년대

- 컴퓨터가 처음 나왔을 시기로 OS라는 개념이 존재하지 않았다.

<br/><br/>

## Batch Processing Systems (일괄 처리 시스템)

- **Job Control Programming**

- **Jobs** - 한 줄의 코딩이 카드 (puncjed card) 한 장에 대응

- **오프라인 작업**으로, 시스템 성능은 I/O 장치가 좌우하였다.

- 마그네틱 테잎이 등장한 이후로 성능이 약간 개선되었다.

- I/O 장치 작업 동안 CPU는 놀고 있어야 하므로, 결과적으로 CPU가 낭비된다.

  - I/O 작업도 심지어 너무 오래 걸림

<br/><br/>

## Multi-programming Systems

- CPU 성능을 개선하기 위해, 성격이 다른 여러 작업을 메모리에 같이 올려 동시에 작업이 진행되도록 한다.

- <strong>목적 : CPU(와 I/O 장치)의 활용도 향상</strong>

  - I/O가 실행되면 CPU를 다음 프로그램에게 할당해주자.

  - 이렇게 I/O와 CPU가 같이 동작하는 환경을 만들어 CPU의 활용도를 올려보자. (병행 실행 환경)

- 여전히 **오프라인 작업**, 그러나 Batch 시 여러 개의 작업을 같이 올리는 것이 가능해졌다.

<br/>

- <strong>Spooling (Simultaneous Peripheral Opration On-Line)</strong>

  - 프린터와 같은 장치에 직접 기록하는 것보다 마그네틱 테잎에 기록하는 것이 훨씬 더 빠르다는 점을 이용

  - 마그네틱 테잎이나 메모리에 데이터를 담아둘 수 있는 I/O 버퍼를 두어  
    직접 장치에 입출력하는 대신, 데이터를 임시 저장하여 바로 입출력 과정을 마치도록 하는 기법

  - 데이터를 임시 저장해두고 프로그램은 (기다리지 않고) 바로 다음 작업을 수행한다.

  - 임시 저장해둔 데이터는 나중에 천천히 프린터로 보내면 사용자에게 결과가 정상적으로 잘 갈 것이다.

  - (아래 한글이나 윈도우즈에도 Spooler가 있음)

<br/><br/>

## Time Sharing (Multi-tasking) Systems (3세대)

- 특정 프로세스가 CPU을 장시간 독점하여 다른 프로세스의 **대기 시간이 길어지는 것을 방지**하기 위해

- CPU를 **시간 단위로 분할**해서 사용하자.

- 시간 단위 = <strong>Time-slice (Time quantum)</strong>

- 지정된 시간이 지나면 CPU가 무조건 다음 프로세스에 할당되도록 하자.

- <strong>목적 : 사용자의 응답성 개선</strong>

<br/>

- **온라인 작업**, 상호작용, 대화형 컴퓨터의 기반

- 비로소 온라인 프로세싱을 지원하는 OS의 기본적인 형태가 이때 갖추어졌다.

- 획기적인 방식!

- Round-Robin Scheduling

<br/>

- ⚠️ 주의점

  - <strong>Multi-programming system != Multi-tasking system</strong>

<br/><br/>

## 4세대 Systems

- 4세대에 들어오면서 마이크로 프로세서 기술이 굉장히 혁신젓으로 발달하였다.

- 이에 따라 하드웨어의 퍼포먼스도 향상

- 마이크로 프로세서는 작고 빠르게, 저장소는 훨씬 크게 (속도는 거의 그대로)

  - 마이크로 프로세서와 저장소 간의 속도 Gap이 더 커지게 됨 → 캐시 메모리 등장의 배경

- 프로세서가 할 수 있는 일들이 많아지면서, 예전에 OS가 담당했던 일들이 다 밑에 있는 컨트롤러, I/O 장치 쪽으로 내려가게 되었다.

- CPU 역시 성능이 좋아져 할 수 있는 일들이 많아졌고, 인터페이스도 Graphical하게 되었다. (GUI 환경)

<br/><br/>
