# 시스템의 구조 (사용자 영역, 커널 영역, 하드웨어)

> 참고 자료 : '시스템 프로그래밍' 학부 수업, 서적 '혼자 공부하는 컴퓨터 구조 + 운영체제'

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/computer_system_overview.md#%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B5%AC%EC%A1%B0">시스템의 구조</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/computer_system_overview.md#%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%98%81%EC%97%AD-%EC%9A%B4%EC%98%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8">사용자 영역 (운영 프로그램)</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/computer_system_overview.md#%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%BD%9C-vs-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EC%BD%9C">시스템 콜 vs 라이브러리 콜</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/computer_system_overview.md#%EC%BB%A4%EB%84%90-%EC%98%81%EC%97%AD-os">커널 영역 (OS)</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/computer_system_overview.md#%EC%BB%A4%EB%84%90-%EC%98%81%EC%97%AD%EC%97%90%EC%84%9C-%EC%9D%B4%EB%A3%A8%EC%96%B4%EC%A7%80%EB%8A%94-%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9Cos%EC%9D%98-4%EA%B0%80%EC%A7%80-%EC%97%AD%ED%95%A0">커널 영역에서 이루어지는 운영체제(OS)의 4가지 역할</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/computer_system_overview.md#%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4-%EC%98%81%EC%97%AD">하드웨어 영역</a>

<br/><br/>

## 시스템의 구조

- 일반적인 컴퓨터 시스템의 구조

    <div align="center">

    <img src="img/slide-17.png" />

    </div>

<br/>

- <strong>사용자 영역, 커널 영역, 하드웨어 영역</strong>으로 구분할 수 있다.

  - <strong>사용자 영역</strong>은 응용 프로그램들이 실행되는 메모리 공간이다.

  - <strong>커널 영역</strong>은 운영체제 프로그램이 실행되는 메모리 공간이다.

  - <strong>하드웨어 영역</strong>은 CPU, 메모리 등 컴퓨터의 물리적 부품들이 동작하는 공간이다.

<br/>

- 응용 프로그램은 운영체제(OS)의 기능, 서비스 등을 요청하기 위해 <strong>시스템 콜 (System Call)</strong>이라는 Fucntion Call을 한다.

<br/>

- 운영체제는 <strong>커널 영역</strong>에서 운영 프로그램들이 잘 실행될 수 있도록 <strong>하드웨어와 소프트웨어를 관리</strong>한다.

<br/><br/>

- (참고) Linux(리눅스) 시스템의 구조

    <div align="center">

    <img src="img/slide-18.png" />

    </div>

<br/><br/><br/>

## 사용자 영역 (운영 프로그램)

- <strong>유저 인터페이스(User Interface)</strong> 혹은 <strong>유저 스페이스(User Space)</strong> 영역으로도 불리며, <strong>커널 영역과 엄격히 분리되어 있다.</strong>

- <strong> 응용 프로그램(프로세스)들이 동작</strong>하는 메모리 공간이다.

<br/>

- <strong>프로세스 (Process)</strong> : 실행 중인 응용 프로그램들

<br/>

- <strong>이중 모드 (Dual Mode)</strong> : CPU가 명령어를 실행하는 모드를 두 가지로 나누는 방식이다. (시용지 모드, 커널 모드)

  - **시용자 모드**는 운영체제의 서비스를 제공받을 수 없는 실행 모드로, 일반적인 응용 프로그램은 사용자 모드로 실행된다.

  - **커널 모드**는 운영체제의 서비스를 제공받을 수 있는 실행 모드로, 사용자 모드에서 커널 모드로 전환하려면 '시스템 콜'을 꼭 해주어야 한다.

  - 즉, 응용 프로그램에서 OS의 기능 및 서비스를 요청하기 위해선 '<strong>시스템 콜</strong>'이 반드시 필요하다.

<br/>

- <strong>시스템 콜 (System Call)</strong> : OS가 가지는 기능을 호출하는 콜

  - ✨ 응용 프로그램에서 커널 영역에 직접 접근한다면 데이터를 잘못 건드려 시스템 전체에 악영향을 끼칠 위험이 생기기 때문에, 사용자 영역과 커널 영역이 엄격히 분리되어 있는 것이다.

<br/>

- 리눅스 시스템에서 명령을 입력받고 실행하는 창인 <strong>Shell(쉘)</strong>은 독립적인 인터페이스로, 커널 밖에 존재하는 응용 프로그램이다. 따라서 쉽게 다른 쉘로 교체할 수 있다.

<br/><br/>

### 시스템 콜 vs 라이브러리 콜

- <strong>시스템 콜</strong> : (커널 안의) OS가 가지고 있는 기능을 부름

  - 사용자 모드에서 커널 모드로 전환하는 방법

- <strong>라이브러리 콜</strong> : (커널 밖 유저 스페이스에 있는) 라이브러리가 갖고 있는 함수를 부름

  - 라이브러리 함수를 API라 많이 부른다.

  <div center="align">

  <img src="img/system_call_library_call.png" />

  </div>

<br/>

#### 모든 라이브러리 콜의 말단에는 시스템을 부르도록(시스템 콜) 되어 있다.

- 라이브러리 콜을 수십만 번 반복하는 경우 애플리케이션에서 바로 시스템 콜을 하는 것이 더 효과적이라 생각할 수 있다.

- 그럼에도 라이브러리 함수가 만들어진 이유

  - 프로그래머에게 편리한 인터페이스를 제공하기 위해서

  - format 기능 (%d, %s, %20s 등) 들은 OS 시스템 콜엔 없다.

    - 이러한 풍부한 기능들을 제공해주기 위해 라이브러리 함수가 만들어졌다.

<br/><br/><br/>

## 커널 영역 (OS)

<div align="center">

<img src="img/slide-19.png" />

</div>

- <strong>운영체제</strong>가 동작하는 메모리 공간으로 <strong>사용자 영역과 엄격히 분리되어 있다.</strong>

- 하드웨어를 편리하게 쓸 수 있도록, 하드웨어를 감싸고 있는 소프트웨어이다.

  - 이 중 핵심적인 부분이 **커널**이다.

  - 즉, <strong>커널은 운영체제의 핵심 기능을 담당하는 부분</strong>이라 볼 수 있다.

  - 그러나 커널이 항상 메모리에 올라가 있는 것은 아니다. (b/c Virtual Memory 기법)

- 프로세스 죽이기, 메모리에 접근하여 데이터 제거 등의 크리티컬한 명령을 수행한다.

<br/>

> OS가 제공하는 서비스 중 커널에 포함되지 않는 서비스도 물론 존재한다.
> 그 대표적인 예시로 <strong>사용자 인터페이스(UI)</strong>가 있다. (GUI, CUI)

<br/><br/>

### 커널 영역에서 이루어지는 운영체제(OS)의 4가지 역할

- <strong>프로세스 관리 (Process Management)</strong>

  - 프로세스에게 CPU 자원을 어떻게 할당할 것인지 → 스케줄링

  - 프로세스 동기화, 교착 상태 해결

<br/>

- <strong>파일 관리 (File Management)</strong>

  - 디스크의 파일 관리 (컴퓨터의 여러 파일 및 폴더 관리)

<br/>

- <strong>메모리 관리 (Memory Management)</strong>

  - OS가 프로세스에게 메모리를 어떻게 할당해줄지

  - 메모리가 부족한 상황에선 이를 어떻게 극복하는지

<br/>

- <strong>디바이스 관리 (Device Management)</strong>

<br/><br/><br/>

## 하드웨어 영역

- 회로와 로직만 존재하고 자율적으로 움직일 수 있는 기능은 없다.

- 즉, OS가 없으면 깡통이다.

<br/>

- 구성 요소 : <strong>디바이스 컨트롤러, 터미널 컨트롤러, 메모리 컨트롤러</strong>

  - <strong>컨트롤러 (Controller)</strong> : 하드디스크 장치에 명령을 내리고 특정 작업(예: 파일 가져오기)을 수행하는 프로세서

<br/>

- <strong>인터럽트 (Interrupt)</strong> : 하드웨어가 밑에서 위로 올려주는 이벤트

  - 프로그램 실행 중에 예기치 않은 상황이 발생한 경우 현재 실행 중인 작업을 즉시 중단하고, 우선 이를 처리한 후 실행 중이던 작업으로 복귀하는 것

  - (예: 네트워크에서 패킷이 왔어요, 디스크에서 데이터가 읽혔어요, 키보드가 눌렸어요)

  - OS는 인터럽트를 받아서 처리한다.

  <br/>

  - 시스템 콜이 구현된 끝단을 보면 인터럽트와 같다. 즉 인터럽트와 유사하게 구현되어 있다.

  - CPU 외부에서 발생하는 **외부 인터럽트(= 하드웨이 인터럽트)**, CPU 내부에서 발생하는 <strong>내부 인터럽트(= 소프트웨어 인터럽트)</strong>로 구분할 수 있다.

    - 소프트웨어 인터럽트를 **Trap**이라 부르기도 한다.

<br/><br/>

> ### ☝🏻 Q. 소프트웨어 인터럽트(Trap)와 시스템 콜의 차이는 무엇인가요? (By ChatGPT)
>
> A. 소프트웨어 인터럽트와 시스템 콜은 모두 컴퓨터 시스템에서 프로세스와 커널 간의 상호작용을 관리하기 위한 메커니즘입니다. 하지만 두 메커니즘의 목적과 작동 방식에는 차이가 있습니다.
>
> 소프트웨어 인터럽트는 하드웨어 이벤트나 소프트웨어 요청으로 발생하는 **비동기적 이벤트**입니다. 예를 들어, 입출력 장치에서 데이터가 도착하면 하드웨어 인터럽트가 발생합니다. 이러한 인터럽트는 현재 실행 중인 프로세스를 중지하고 커널의 인터럽트 핸들러 함수로 제어를 전달합니다. 인터럽트 핸들러 함수는 인터럽트에 대한 처리를 수행하고, 다시 프로세스로 제어를 반환합니다.
>
> 반면, 시스템 콜은 사용자 프로세스가 커널에 서비스를 요청하는 방법입니다. 시스템 콜은 일반적으로 **동기적으로 호출**되며, 사용자 프로세스는 커널의 함수를 호출하여 서비스를 요청합니다. 이러한 함수 호출은 사용자 모드에서 실행되며, 해당 함수는 커널 모드로 전환하여 실행됩니다. 커널에서 요청된 서비스가 완료되면, 결과는 다시 사용자 프로세스로 반환됩니다.
>
> **요약하자면, 소프트웨어 인터럽트는 비동기적인 하드웨어 이벤트나 소프트웨어 요청에 응답하는 메커니즘이며, 시스템 콜은 동기적으로 사용자 프로세스가 커널에 서비스를 요청하는 메커니즘입니다.**

<br/>
