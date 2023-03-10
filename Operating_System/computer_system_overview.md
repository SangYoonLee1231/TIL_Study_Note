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

- 일반적인 컴퓨터의 구조

    <div align="center">

    <img src="img/slide-17.png" />

    </div>

  - <strong>사용자 영역, 커널 영역, 하드웨어 영역</strong>으로 구분할 수 있다.

    - <strong>사용자 영역</strong>은 응용 프로그램들이 실행되는 메모리 공간이다.

    - <strong>커널 영역</strong>은 운영체제 프로그램이 실행되는 메모리 공간이다.

    - <strong>하드웨어 영역</strong>은 CPU, 메모리 등 컴퓨터의 물리적 부품들이 동작하는 공간이다.

  - <strong>운영체제</strong>는 <strong>커널 영역</strong>에서 운영 프로그램들이 잘 실행될 수 있도록 <strong>하드웨어와 소프트웨어를 관리</strong>한다.

<br/>

- (참고) Linux(리눅스) 시스템의 구조

    <div align="center">

    <img src="img/slide-18.png" />

    </div>

<br/><br/>

## 사용자 영역 (운영 프로그램)

- 유저 인터페이스(User Interface) 혹은 유저 스페이스(User Space) 영역으로도 불리며, 커널 영역과 엄격히 분리되어 있다.

- <strong> 응용 프로그램(프로세스)들이 동작하는 메모리 공간이다.</strong>

  - <strong>프로세스 (Process)</strong> : 실행 중인 응용 프로그램들

- 응용 프로그램에서 OS의 기능 및 서비스를 요청하기 위해 '시스템 콜'을 한다.

  - <strong>시스템 콜 (System Call)</strong> : OS가 가지는 기능을 호출하는 콜

  - 응용 프로그램에서 커널 영역에 직접 접근하면 데이터를 잘못 건드려 시스템 전체에 악영향을 끼칠 위험이 있으므로 시스템 콜이 필요하다.

- <strong>눅스 시스템</strong>에서 명령을 입력받고 실행하는 창인 <strong>Shell(쉘)</strong>은 독립적인 인터페이스로, 커널 밖에 존재하는 응용 프로그램이다. 따라서 쉽게 다른 쉘로 교체할 수 있다.

<br/>

### 시스템 콜 vs 라이브러리 콜

- <strong>시스템 콜</strong> : (커널 안의) OS가 가지고 있는 기능을 부름

- <strong>라이브러리 콜</strong> : (커널 밖 유저 스페이스에 있는) 라이브러리가 갖고 있는 함수를 부름

  - 라이브러리 함수를 API라 많이 부름

<br/>

#### 모든 라이브러리 콜의 말단에는 시스템을 부르도록(시스템 콜) 되어 있다.

- 수십만 번 반복하는 경우 애플리케이션에서 바로 시스템 콜을 하는 것이 효과적일 수 있다.

- 그럼에도 라이브러리 함수가 만들어진 이유

  - 프로그래머에게 편리한 인터페이스를 제공하기 위해서

  - format 기능 (%d, %s, %20s 등) 들은 OS 시스템 콜엔 없다.

    - 이러한 풍부한 기능들을 제공해주기 위해서

<br/><br/>

## 커널 영역 (OS)

<div align="center">

<img src="img/slide-19.png" />

</div>

- 운영체제가 동작하는 메모리 공간으로 사용자 영역과 엄격히 분리되어 있다.

- 하드웨어를 편리하게 쓸 수 있도록, 하드웨어를 감싸고 있는 소프트웨어이다.

  - 이 중 핵심적인 부분이 **커널**이다.

  - 그러나 커널이 항상 메모리에 올라가 있는 것은 아니다. (b/c Virtual Memory 기법)

- 프로세스 죽이기, 메모리에 접근하여 내용 제거 등의 크리티컬한 명령을 수행한다.

<br/>

### 커널 영역에서 이루어지는 운영체제(OS)의 4가지 역할

- <strong>프로세스 관리 (Process Management)</strong>

  - 프로세스에게 CPU 자원을 어떻게 할당할 것인지 → 스케줄링

- <strong>파일 관리 (File Management)</strong>

  - 디스크의 파일 관리

- <strong>메모리 관리 (Memory Management)</strong>

- <strong>디바이스 관리 (Device Management)</strong>

<br/><br/>

## 하드웨어 영역

- 회로와 로직만 존재하고 자율적으로 움직일 수 있는 기능은 없다.

- 즉, OS가 없으면 깡통이다.

- 구성 요소 : <strong>디바이스 컨트롤러, 터미널 컨트롤러, 메모리 컨트롤러</strong>

  - <strong>컨트롤러 (Controller)</strong> : 하드디스크 장치에 명령을 내리고 특정 작업(예: 파일 가져오기)을 수행하는 프로세서

- <strong>인터럽트 (Interrupt)</strong> : 하드웨어가 밑에서 위로 올려주는 이벤트

  - (예: 네트워크에서 패킷이 왔어요, 디스크에서 데이터가 읽혔어요, 키보드가 눌렸어요)

  - OS는 인터럽트를 받아서 처리한다.

  - 시스템 콜이 구현된 끝단을 보면 인터럽트와 같다. 즉 인터럽트와 유사하게 구현되어 있다.

<br/>
