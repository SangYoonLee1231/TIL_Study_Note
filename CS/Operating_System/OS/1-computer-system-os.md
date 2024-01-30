# 1. 컴퓨터 시스템과 OS

<br/>

> 참고 자료 : '운영체제' 학부 수업 자료 (이윤석 교수님)

- 📔 <strong><a href="https://drive.google.com/file/d/1TxI6KTJy-1fH4e1DFlgcXPIVdxS11tg3/view?usp=sharing">강의 내용 필기 노트 보러가기 (Lec 1)</a></strong>

<br/><br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/1-computer-system-os.md#%EC%BB%B4%ED%93%A8%ED%84%B0-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%84%B1-%EC%9A%94%EC%86%8C">컴퓨터 시스템 구성 요소</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/1-computer-system-os.md#os-operating-system-%EB%9E%80">OS (Operating System) 란?</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/1-computer-system-os.md#%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%B8%A1%EB%A9%B4%EC%97%90%EC%84%9C-os%EB%9E%80">어플리케이션 측면에서 OS란?</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/1-computer-system-os.md#%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%B8%A1%EB%A9%B4%EC%97%90%EC%84%9C-os%EB%9E%80">시스템 측면에서 OS란?</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/OS/1-computer-system-os.md#os%EB%8A%94-highly-concurrent-event-driven-software">OS는 Highly-concurrent, event-driven software</a>

<br/><br/>

## 컴퓨터 시스템 구성 요소

- <strong>하드웨어 (Hardware)</strong> : 컴퓨팅 자원 제공, 구동 시키는 소프트웨어 없으면 깡통

- <strong>운영체제 (Operating System)</strong>

  - 하드웨어를 감싸고 있음

  - 하드웨어를 **동작, 편리하게 사용**하도록 지원하는 시스템 소프트웨어

  - 여러 **자원을 효과적으로 관리** (효율성, 공정성)

- <strong>시스템 프로그램 & 어플리케이션 프로그램</strong>

  - **시스템 프로그램** : 다른 소프트웨어를 지원하는 소프트웨어 (컴파일러, 어셈블러, DB 등)

  - **어플리케이션 프로그램** : 고유 기능을 가지는 소프트웨어 (한글, 엑셀 등)

- <strong>사용자 (User)</strong> : 사람 or 기계 or 컴퓨터

<br/>

- **컨트롤러 (controller)** : 각 장치에 달려 있어, CPU의 명령을 받아 장치를 가동시키는 역할 (= adaptor)

- **버스 (bus)** : 전기적 신호를 전달하는 라인

<br/><br/><br/>

## OS (Operating System) 란?

### 어플리케이션 측면에서 OS란?

- **프로그램의 실행환경을 제공**

  - 프로세스 형태로 CPU를 실행시킬 수 있도록 함

  - 프로세스가 사용할 메모리 공간을 지정

  - 하드디스크는 '책'처럼 단일화된 형태를 'Volume'으로 관리

<br/><br/>

### 시스템 측면에서 OS란?

- **관리자의 입장**에서 **자원을 더 효과적으로/공정하게 배분하기 위해 노력함**

  - **Sharing** : 같은 자원을 잘 나눠쓸 수 있도록

  - **Protection** : 해당 프로세스에게 할당된 공간 및 권한을 보호

  - **Fairness** : 공정하게 권한을 부여 (시스템마다 다름)

  - **Efficiency** : 효율성 (CPU, 베터리 낭비 줄이기)

  - **Concurrency** : 병행성 (생산성을 위해 여러 장치들이 동시에 작동)

<br/>

- 모든 프로그램은 각각 독립적인 공간을 보장받는 개체이다. (Protection)

  - 해당 자원을 외부에서 마음대로 접근할 수 없다.

  - 본인도 다른 프로그램의 내부를 함부로 접근할 수 없다.

<br/>

- **Dynamic Frequency** : CPU의 클럭을 동적으로 조절하여 파워가 낭비되지 않도록 함

<br/><br/>

### OS는 Highly-concurrent, event-driven software

- OS는 **유저 영역**과 핵심부인 **커널 영역**으로 나눤다.

- 유저 영역에서 OS가 제공하는 기능들을 사용하기 위해선 System Call을 호출해야만 한다.

  - 이 떄 System Call을 **인터럽트 (Interrupt)** 방식으로 부른다.

  - 이처럼 응용 프로그램이 의도적으로 **소프트웨어 인터럽트**를 일으키는 방법을 **Trap**이라 한다.

<br/>

#### 인터럽트 (Interrupt)

- OS의 밑에서 히드웨어 장치들이 작업을 마치고 알리는 이벤트(알림)

- 알림이 전달되면 OS는 하던 일을 멈추고 이 인터럽트를 처리한다.

- <strong>인터럽트 핸들러 (Interrupt Handler)</strong> : 인터럽트를 처리하는 루틴들

<br/>

#### OS는 Highly-concurrent, event-driven software (interrupt-driven software)

- OS에선 **여러 작업(사건)이 병행하여 지속적으로 발생**하고

  - **사건** : 위에서는 소프트웨어 인터럽트, 아래에서는 하드웨어 인터럽트 + Exception (예외 처리)

- 사건들이 발생할 때마다 OS는 이를 처리하는 '**사건처리반**' 역할을 수행한다.

<br/><br/>
