# 리눅스 프로세스 관리 Part 1 (<code>fork</code>, <code>exec</code> 시스템 콜)

<br/>

> 참고 자료 : '시스템 프로그래밍' 학부 수업 자료

<br/><br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt1.md#%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EC%83%9D%EC%84%B1-%EA%B4%80%EB%A0%A8-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%BD%9C">프로세스 생성 관련 시스템 콜</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt1.md#fork-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%BD%9C">`fork` 시스템 콜</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt1.md#wait-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%BD%9C">`wait` 시스템 콜</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt1.md#concurrent-process">Concurrent Process</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt1.md#exit-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%BD%9C">`exit` 시스템 콜</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt1.md#exec-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%BD%9C">`exec` 시스템 콜</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt1.md#user-process-tree">User Process Tree</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt1.md#shell%EC%9D%98-%EB%8F%99%EC%9E%91-%EB%B0%A9%EC%8B%9D">Shell의 동작 방식</a>

<!-- - <a href=""></a> -->

<br/><br/>

## 프로세스 생성 관련 시스템 콜

### `fork` 시스템 콜

- 자기와 똑같이 생긴 프로세스를 하나 복제시키는 시스템 콜이다.

- 리눅스에선 프로세스 생성하는 방식이 특이하다.

  - 리눅스에선 새로운 프로세스를 `fork` 시스템 콜을 통해 만든다.

- 자기 프로세스를 fork하여 child 프로세스를 만든다. → <strong>Clone Process</strong>

- child process는 부모가 가진 모든 것을 똑같이 상속받는다.

  - 부모가 열고 있는 open file, file discripor도 모두 똑같이 상속받는다.

    → 부모와 같은 파일에 대한 정보를 가리키고 있다.

- 부모 프로세스가 fork를 하고 나면 부모 프로세스는 fork로부터 return 값을 받아야 한다.

  - child도 마찬가지로 fork에서 돌아오는 시점부터 실행이 시작됨

- parent와 child 프로세스는 겉으로 봐선 똑같기 때문에, OS에서는 parent와 child를 구분시켜주는 역할을 수행한다.

  - return 값 : **child = 0, parent = 막 태어난 child의 pid (0보다 큰 양수 값, 보통 parent보다 큰 값)**

  - parent와 child가 각각 본인이 해야 할 일을 구별해서 할 수 있도록 코드를 짤 수 있다.

<br/><br/>

### `wait` 시스템 콜

- wait 시스템 콜이란?

  - 부모, 자식 프로세스가 만들어지면 각자 자신의 길을 가는 독립적인 프로세스로 인식된다.

    - OS에서도 이 둘을 각각의 구별된 프로세스로 대한다.

  - 그러나, 경우에 따라 부모가 자식을 만들어두고 **잠시 본인의 동작을 일시중지**하고 있다가, **자식이 잘 실행되고 종료될 때까지 기다릴 수도 있다.**

  - 이 때 쓰는 시스템 콜이 `wait` 시스템 콜이다.

<br/><br/>

### Concurrent Process

- 처음에 어떤 프로세스에서 fork가 일어나는 순간 자식 프로세스가 생성된다.

- 그 후 두 프로세스는 각각 fork으로부터 return 값을 받는다.

- 이 리턴값에 따라 코드가 다르게 동작하도록 조건문을 사용하여 코드를 작성할 수 있다.

  → 이렇게 동시에 실행하는 여러 개의 프로세스를 **Concurrent Process**라 부른다.

  <img src="../img/2023-04-05_PM_4.37.13.png">

  - 여러 프로세스를 동시에 만들어서 각자 자신의 몫에 맞는 역할을 수행할 수 있도록 소프트웨이를 설계하자

<br/><br/>

### `exit` 시스템 콜

- `exit` 시스템 콜이란?

  - 부모가 자식 프로세스를 (fork 시스템 콜을 통해) 생성한 후  
    wait 시스템 콜로 인해 본인의 동작을 중지한 채 자식 프로세스가 끝나기를 기다리는 상황일 때,

  - **자식이 자신의 프로세스를 종료하기 위해** 쓰는 시스템 콜 → `exit` 시스템 콜

<br/>

- exit를 코드에 작성할 때 0~255 사이의 무부호 정수를 인자값으로 준다.

  - 숫자의 의미는 개발자에 부여하는 의미에 따라 달라진다.

- 프로세스가 끝나도 OS는 이를 바로 제거하지 않고 **좀비 상태**로 보존해 둔다.

  - 그 프로세스 만들어 낸 여러가지 정보들이 일단은 잠시 메모리에 유지될 필요가 있기 때문

<br/>

- exit 시스템 콜의 동작 과정

  - OS가 exit 시스템 콜에 준 숫자를 보고 OS는 child가 끝났음을 확인하다.

  - 그 후 OS는 해당 child 프로세스가 끝나기를 기다리고 있는 부모 프로세스가 있는지 확인한다.

  - 있다면, 해당 부모 프로세스에게 exit 코드를 전달해준다.

  - (이때 마침 wait 중인 부모 프로세스는 OS에게 어떤 변수의 주소를 전달해준다 → OS에게 어떤 정보를 이 주소에 저장해 달라)

  - return 값 (pid_t) : 방금 종료된 child의 pid (슬라이드 17)

    - (함수를 호출할 때 포인터를 전달하는 이유 : 그 포인터에 어떤 값을 넣어달라)

  - wait이 성공하면 좀비 상태의 자식 프로세스는 사라진다.

<br/><br/>

### `exec` 시스템 콜

- 자식 프로세스가 자신의 내용을 완전히 바꾸기 위해 사용하는 시스템 콜

- **exec는 새로운 프로세스를 생성하지 않는다.**

  - 이미 존재하는 자신의 프로세스를 바꿀 뿐이다.

  - pid, open file, priorty 등은 그대로 유지한다.

  - 자신의 몸체만 바꿀 뿐 (코드, 데이터, 힙, 스택 포함)

  - 부모-자녀 관계도 그대로 유지된다.

  <img src="../img/2023-04-05_PM_4.42.18.png">

<br/>

- 시스템 콜의 변종 (variation)

  - 핵심은 똑같다. 새로운 걸 이용하여 탈바꿈한다.
  - 인자를 전달하는 방법, 경유에 따라 부모가 갖고 있는 환경 정보 그대로 전달 등

  - (`exec-v`를 이용하면 하고 싶은 일을 대부분 할 수 있다.)

<br/><br/>

### User Process Tree

<img src="../img/2023-04-04_AM_10.19.44.png">

- **init** : 최초로 생성되는 유저 프로세스 (프로세스의 조상)

- init을 fork하면 그 순간에 init의 클론 (자식들) 생성

  → `exec(getty)` 시스템 콜 호출 → 자식 프로세스가 getty 내용으로 바뀜

- getty 프로세스 → 누군가 접근을 시도하면 login으로 바뀜 (by exec) → login에 성공하면 shell process로 변신 (exec) (**모두 다 같은 프로세스이다.**)

  - **shell의 부모는 login이 아니다.**

  - **shell의 부모는 init이다.**

  - shell도 독립된 하나의 프로세스이다. 커널과 분리되어 유저 영역에서 돌아가는 프로그램이다.

<br/><br/>

### Shell의 동작 방식

1. Shell에 명령이 들어오면, Shell은 우선 그 명령어를 해석한다.

2. 그 후 Shell은 해당 명령어를 실행하기 위해 프로세스를 하나 생성한다.

3. 그 때 fork를 통해 Shell의 똑같은 자식 프로세스가 하나 만들어진다.

   - 우리 눈에 보이진 않고, OS 내부에서 이미지만 똑같은 자료구조체가 만들어진다.

4. Shell이 exec을 통해 새로 만든 자식 프로세스를 실행시킬 프로그램으로 변신시킨다. (ex : 아래 한글)

   - 아래 한글의 parent process는 Shell이다.

- 즉, Shell과 그 뒤에 만들어지는 응용 프로그램은 서로 부모-자식 관계인 것이다.

<br/>

- **예시**

  <img src="../img/2023-04-04_AM_10.20.24.png">

- `$ ./a.out` : shell, a.out 프로세스 생성

  - shell은 일반적으로 자식을 만들면 그 자식이 종료될 때까지 wait한다.

  - shell 프로세스의 내부에 fork 이후 wait을 하는 코드가 존재한다.

- `$ cat myfile` : cat은 파일을 표준 출력에 띄워주는 명령어이다.

  - cat이라는 프로세스가 만들어진다.

- `$ ./a.out &`의 `&` 표시 : shell이 waiting을 하지 않는다. ‘나는 나대로 다음 실행을 하겠다’는 의미이다.

  - 이때 이 프로세스를 background process라 한다.

  - `&`을 하면 prompt가 바로 띄워진다.

- `rm myfile` : rm 프로세스도 실행된다. (shell, a.out, rm 총 3개의 프로세스가 동시에 실행되고 있다.)

- `$ ./a.out > output` 의 `>` : 재지정 연산자(>, assignment operator)

  - 이 브라켓이 없으면, 모든 표준 출력이 화면에 나타난다.

  - 브라켓이 있으면, 화면에 나타나야 될 표준 출력이 지정한 이름의 file에 담긴다.

<br/>

- Stdout을 재지정할 때

  - stderr를 출력할 때에는 꺽쇠 뒤에 2를 써주어야 한다.

    - stderr의 디스크립터 번호가 2

<br/>

- **Simple shell example**

  <img src="../img/2023-04-04_AM_10.28.11.png">

  - prompt를 통해 입력 받은 string을 읽어들이고 이를 해석한다.

  - 이러한 문자열 해석을 구문 분석 (parsing)이라 한다.

  - 위 코드는 구문 분석을 하는 코드이다.

  - fork를 하는 순간 shell과 똑같은 프로세스가 하나 생성된다.

  - 그리고 나서 fork의 리턴값을 체크한다. (pid가 0이면 자식 프로세스)

  - **foreground 프로세스**

    - foreground process = 자식이 끝날 때까지 기다린다.

    - VS background process

<br/>
