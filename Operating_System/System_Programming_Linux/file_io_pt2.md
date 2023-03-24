# 파일 I/O Part 2 (파일 스트림과 디스크립터, 버퍼 심화)

<br/>

> 참고 자료 : '시스템 프로그래밍' 학부 수업 자료

<br/><br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/file_io_pt2.md#%EB%A6%AC%EB%88%85%EC%8A%A4-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%A7%9B%EB%B3%B4%EA%B8%B0">리눅스 명령어 맛보기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/file_io_pt2.md#%ED%8C%8C%EC%9D%BC-io-part-1-%EB%B3%B5%EC%8A%B5">파일 I/O Part 1 복습</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/file_io_pt2.md#%EB%B2%84%ED%8D%BC-buffer-%EC%8B%AC%ED%99%94">버퍼 (Buffer) 심화</a>
<!-- - <a href=""></a> -->

<br/><br/>

### 리눅스 명령어 맛보기

- <code>ls /</code> : 현재 디렉토리 리스트 보기 + 루트

- <code>ls /sp-resource/</code> : sp-resource 디렉토리 내부 보기

- <code>ls /sp-resource/.\*</code> : .으로 시작하는 모든 것을 보여줌

  - <code>..</code> : 현 디렉토리의 하나 위

- <code>pwd</code> : 현재 어디에 있는지 확인하는 명령어

- <code>cp -r /sp-resource/.vim\* .</code> : vim으로 시작하는 모든 디렉토리를 복사

  - <code>cp</code> : 목사

  - <code>-r</code> : 서브 디렉토리까지 모두 긁어서 가져옴

  - <code>.</code> : 현재 위치

- <code>ls -al</code> : 모든 파일과 속성 표시

- <code>vi test.c</code> : 기본 템플릿으로 소스 코드 보기

- <code>cp -r /sp-resource/ .</code> : 루트 밑 sp-resource에 있는 모든 걸 복사

<br/><br/>

## 파일 I/O Part 1 복습

- I/O 스탠다드 라이브러리가 제공하는 I/O Function을 지금까지 써왔다.

  - fprint() 등

- 결국은 OS가 제공하는 파일 시스템 콜을 써야 OS에게 서비스 요청이 간다.

- 라이브러리가 제공하는 함수, 그걸 왜 써야하는지?, 무슨 특징이 있는지?

  1. 라이브러리가 사용자에게 편리성을 제공한다.

  2. 라이브러리에 버퍼를 두어 커널에서 올라오는 데이터를 버퍼에 임시로 저장해서 이를 반복적으로 활용할 수 있다. (반복 호출 방지)

     1. 버퍼 = 캐시

<br/>

- 캐싱 기법은 모든 계층에 적용된다.

  - 하드디스크 보다 더 빠른 SSD의 속도에 비하면 하드디스크는 너무 느린 장치

    - SSD의 일부에 하드디스크의 저장 내용을 올려둠

    - 하드디스크에 접근하는 횟수 감소 → 성능 개선

  - 느린 장치의 데이터 → 빠른 장치의 데이터에 올려둠 : **캐싱 기법**

- 파일 스트림과 파일 디스크립터는 1대1로 대응

  - 파일 스트림 안에는 파일과 관련된 여러 정보들이 있지만

  - 그 중 중요한 정보로 파일 디스크립터가 몇 번인지 기록하고 있다

- 파일 디스크립터는 파일의 장치 정보를 담고 있는 일종의 인덱스

  - 프로세스 만들어지면 기본적으로 3개가 할당

    - stdin, stdout, stderr → 0, 1, 2번

<br/>

- 반대로, 시스템 콜을 이용해서 바로 파일을 오픈하고 작업할 수 있다.

- 시스템 콜을 이용해서 파일을 오픈하면 파일 스트림 구조체가 만들어지지 않는다.

  - 파일 스트림 구조체는 라이브러리 콜을 통해서만 만들어지는 구조체

  - 시스템 콜은 파일 스트림을 만들지 않는다.

  - fdopen : 시스템 콜을 통해 파일 디스크립터만 만들고 → 이를 가지고 오픈(read, write)모드를 갖는 파일 스트림 구조체를 만들어줘

<br/>

- 함수의 이름, 인자, 반환값, 값들의 타입 꼭 잘 기억할 것

<br/><br/>

## 버퍼 (Buffer) 심화

- 버퍼는 내가 쓰는 라이브러리에서 관리하는 버퍼 (라이브러리 버퍼링)

  - fread → 데이터 전달 → buffer에 자연스럽게 카피

  - 만일 버퍼가 없다면 바로 커널에 진입해야 함

  - 버퍼가 있으면, 엔터가 들어오거나, 버퍼에 있는 내용이 일정량 다 차야 커널에 전달

  - 버퍼를 사용할 때, (출력을 예로 듦) 내가 write 하면 버퍼링 하지 말고 바로 커널로 내려보내서 장치에 나타나게 하라 → **Unbuffering**

  - 시스템 콜로 매번 내려보내면 시간 오래 걸림, 비용 문제 발생 → 그래서 버퍼를 씀

<br/>

### 버퍼링 모드

- **Full Buffering** : 버퍼 용량이 꽉 차야 다음 과정(ex: I/O)이 수행

  - 시스템 콜 횟수 현격히 줄일 수 있음

  - 버퍼가 꽉 찰 때까지는 눈에 나타나지 않는다.

  - fflush 함수 : (버퍼의) 모든 걸 내려보내라

- **Line Buffering** : 한 줄이 찰 때마다 커널로 내려보내라

  - \n이 나와야만 한 줄로 인식

  - getchar() (키보드에서 문자 하나씩 받아들일 때) 문제
    - line buffering에선 getchar() 함수가 정상적으로 동작하지 않음

- **Unbuffering** : 버퍼를 쓰지 말고 곧바로 커널로 내려보내 장치에 결과가 나타나게 하라

<br/>

- 상황을 보고 버퍼링 모드를 사용해야 할 때 쓰고 아님 말고

- fflush() 써도 된다.

- 데이터 안정성을 추구하려면 시스템 콜을 자주 호출하여 버퍼에 있는 데이터를 내려보내야 한다.

- 시스템을 잘 이해하고 있자.

<br/>

- 리눅스에선 (디폴트 값)

  - stderr : 항상 unbuffering (긴급한 메세지)

  - stdin/stdout : 항상 line buffering

  - 그 외 나머지 : 항상 full buffering

<br/>

### 버퍼링 관련 함수

- <code>void **setbuf** (FILE *stream, char *buf);</code>

  - <code>char \*buf</code> : character array의 주소, 8KB or 16KB 잡아놓고 그 주소 가짐

  - 그 array을 <code>FILE \*stream</code>이 사용하는 버퍼로 세팅

  - <code>char \*buf</code>이 <code>NULL</code>이라면 Unbuffering으로 쓰겠다는 의미

- <code>int **setvbuf** (FILE *stream, char *buf, int type, size_t size);</code>

  - <code>int type</code> : 버퍼링 타입 지정 (Full, Line, Unbuffering)

  - <code>size_t size</code> : 버퍼 사이즈 지정

  - **return 값** : 0이면 성공적으로 수행, 0이 아니면 에러 코드 반환

<br/>

- 에러 코드를 잘 처리하는 것도 매우 중요한 일 중 하나

- 시스템 콜이든 라이브러리 콜이든 호출하면 리턴값을 확인하는 습관을 가질 것
