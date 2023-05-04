# 리눅스 프로세스 관리 Part 6 (Record Lock)

<br/>

> 참고 자료 : '시스템 프로그래밍' 학부 수업 자료

<br/><br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt6.md#mutex-lock-%EC%8B%AC%ED%99%94">Mutex Lock 심화</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt6.md#mutex">Mutex</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt6.md#%EB%AC%B8%EC%A0%9C-%EC%83%81%ED%99%A9-%EC%A0%95%EC%9D%98">문제 상황 정의</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt6.md#%EB%AC%B8%EC%A0%9C-%EC%83%81%ED%99%A9-%EA%B0%9C%EC%84%A0-%EB%B0%A9%EB%B2%95">문제 상황 개선 방법</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt6.md#lock%EC%9D%98-%EA%B5%AC%EB%B6%84">Lock의 구분</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt6.md#record-lock-%ED%95%A8%EC%88%98--fcntl-%ED%95%A8%EC%88%98">Record Lock 함수 : `fcntl` 함수</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Operating_System/System_Programming_Linux/linux_process_control_pt6.md#record-lock">Record Lock</a>

<br/><br/>

## Mutex Lock 심화

### Mutex

- 공유 변수, 공유 파일, 공유 데이터에 한 순간에 한 쓰레드 또는 한 프로세스씩 접근해서 데이터를 갱신할 수 있도록 만든 잠금장치

- 서로 다른 두 개의 쓰레드가 count라는 변수에 접근해서 값을 더하거나 뺀다.

- 그럼 count에 항상 접근하기 전에

  - Mutex Lock을 획득하고

  - 그 후 count를 조작하는 작업을 수행한 후 (Critical Section)

  - Mutex Unlock

- 을 해주어야 한다.

- 한 순간에 한 쓰레드만 작업할 수 있도록 하기 위해서다. (Race Condition 방지)

- Record Lock도 이것과 유사한 개념인데, 조금 더 세밀하게 상황을 조절한다.

<br/>

### 문제 상황 정의

- 어떤 데이터에 여러 개의 쓰레드가 동시에 읽거나 쓰는 경우를 생각해보자.

- **Reader** : (예) 웹 포탈에 올려진 기사를 읽는 사람 (독자)

- **Writer** : (예) 웹 포탈에 기사를 써서 올리는 사람 (기자)

- Reader와 Writer 프로세스가 데이터(변수나 파일)에 동시에 접근해서 작업을 하려 하는데,

- 이 때, 이 데이터에 한 번에 하나의 프로세스씩만 접근해서 작업을 하도록 해야 한다고 하자.

- 그럼 이 상황에서 Mutex를 쓸 수 있다. (Mutex는 Mutual exclusion을 의미)

  - 한 순간에 한 프로세스씩만 접근이 가능하도록 기능을 제공

- 이렇게 되면 한 번에 한 명의 Reader나 한 명의 Writer만 접근할 수 있게 되므로, 성능이 심각히 떨어지는 문제가 발생한다.

  - (예) 웹에서 기사를 읽으려고 하는데, 앞 사람이 다 읽을 때까지 계속 기다리고 있어야 한다.

<br/>

### 문제 상황 개선 방법

- 데이터를 조작하는 경우, 당연히 한 순간에 한 Writer만 접근해서 작업을 하도록 해주어야 한다. (베타적 권한 갖고 데이터를 갱신해야 한다.)

  - 읽는 도중 데이터 수정 시, 읽는 내용과 바뀐 내용이 뒤엉킬 수 있음

- **Writing을 할 때 → Exclusive lock을 가져야 한다.**

- 반면에, Reading을 할 땐 다른 프로세스의 접근을 막을 이유가 없으므로 같이 접속하도록 해준다.

  - Reading은 Race Condition이 발생하지 않으므로

- 다만, Reading 중 Writer 프로세스가 들어오는 것은 막아야 한다.

- **정리**

  - 내가 읽을 때, 다른 사람이 들어와서 Reading 하는 것은 허용한다.

  - 내가 읽을 때, 다른 사람이 들어와서 Writing 하는 것은 허용하지 않는다.

- **Reading을 할 때 → Shared lock을 허용하자.**

  ![스크린샷 2023-05-01 오후 6.51.53.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cb9a92b6-a445-49de-b6e5-774d94044cb3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.51.53.png)

- 보통 Writing 보다 Reading하는 경우가 더 많다.

- Read를 어떻게 다루는 가에 따라서 성능에 큰 차이를 준다.

- **하나의 Mutex를 Reading할 때는 Exclusive lock으로, Writing을 할 땐 Shared lock으로 구분해서 쓰자.**

<br/>

### Lock의 구분

- **Writer’s lock (Exclusive lock)**

  - 한 Writer가 Exclusive lock을 갖고 있으면, 다른 Writer는 기다려야 한다.

  - 한 Writer가 Writing을 하는 중에도 다른 Writer는 당연히 기다려야 한다.

- **Reader’s lock (Shared lock)**

  - 특수한 Mutex

  - 한 Reader가 Shared lock을 가지고 있으면, 다른 Reader도 바로 Join할 수 있다. (바로 Reader의 lock을 얻을 수 있다.)

  - 만일 어떤 Reader가 Reader의 lock을 얻을려고 했는데, 그 자원에 이미 다른 Writer가 접근하여 Writer’s Lock을 갖고 있으면, Reader lock은 바로 허용되지 않는다.

  - Writing이 완료될 때까지 기다려야 한다.

    ![스크린샷 2023-05-02 오전 12.02.05.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de102544-9d06-447c-9ea1-50e4e8617e4a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-02_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_12.02.05.png)

    (Region → Record로 수정)

<br/>

### Record Lock 함수 : `fcntl` 함수

- `int fcntl(int fildes, int cmd, struct flock *lock);`

- `#include <fcntl.h>` 헤더를 포함하여야 한다.

- 인자

  - `int fildes` : 내가 조작하려는 파일의 파일 디스크립터

  - `int cmd`

    - 조작을 하기 위한 명령어

    - `F_GETLK` : 내가 lock을 얻을 수 있는지 체크하는 명령

      - 만일 다른 프로세스가 lock을 갖고 있어 현재 lock을 못 얻는 상황이라면, 다음 인자인 `struct flock *lock` 구조체에 lock 정보를 담아서 알려줌

      - 만일 lock을 얻을 수 있다면, `struct flock *lock` 에서 l\*type(lock type) 정보에 F_UNLCK을 적어서 보내줌 (lock이 available함을 알려주는 정보)

        ![스크린샷 2023-05-01 오후 7.55.14.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52212868-ba3b-468e-9d6b-59e9c5b8e213/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-01*%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7.55.14.png)

    - `F_SETLK` : lock을 걸려고 할 때 쓰는 명령

      - **Non-blocking**으로 동작 : try시 실패할 경우 -1을 갖고 바로 돌아옴

      - `l_type`에 `F_RDLCK`(Shared Lock)을 try할 지 `F_WRLCK`(Exclusive Lock)을 try할 지 지정

      - 만약에 다른 프로세스가 그 사이에 lock을 가로채져 없어지면, 바로 -1을 리턴

      - 에러가 발생하면, `errno` = `EACCESS` or `EAGAIN` (lock에 접근할 수 없으므로 나중에 다시 시도해라)

    - `F_SETLKW` : lock을 취할 때 명령어

      - 마지막 W는 **Waiting**을 의미

      - **blocking**으로 동작 : try시 실패할 경우 바로 돌아오지 말고 lock이 available 할 때까지 **기다렸다가**, lock을 갖고 돌아옴

        - **(blocking = waiting)**

    - `F_SETLK` and `l_type == F_UNLCK`

      - lock을 쓰고 반환하는 용도

      - **lock을 썼으면 반드시 돌려주어야 한다.** 그렇게 하지 않으면, 모든 프로세스가 lock 획득을 위해 기다림 → 모두 blocking, 프로그램 멈춤

  - `struct flock *lock`

    - file lock의 구조체 (주소값을 전달)

    - 필요한 정보들을 설정한 다음, 그 정보를 전달하는 방법

<br/><br/>

## Record Lock

- Record Lock는 일종의 Mutex이다.

- **record** : 한 파일을 구성하는 기본 정보

  - 학생 정보 파일을 예로 들자

  - 학생 1명 = 학번, 이름, 연락처, 학적 관련 정보 등등

  - 이들을 하나의 구조체로 만듦, 이 구조체 하나가 한 record

  - 학생 전체의 record가 저장되어 있는 것 → 학적 테이블

  - 이 때, 이 record들 마다 하나하나 별도로 우리가 lock을 control하면 얼마나 좋을까

    - 예를 들어, 내가 접근하고자 하는 1번 lock, 10번 lock만 건다.

    - 그럼 모든 프로세스가 더 동시에 여러 곳에서 작업 가능

    - 만약에 전체에 한 lock만 적용하면 한 순간에 프로세스 하나만 들어가서 작업하기 때문에 concurrency(병행성)이 떨어진다.

  - **내가 lock을 걸 수 있는 범위를 지정하면 되겠다. → Record Lock**

    ![스크린샷 2023-05-01 오후 7.55.14.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de7faa8f-ff25-4316-92de-6e4229e0ebaa/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7.55.14.png)

  - `off_t l_whence` : 범위를 지정할 때 , 지정하는 기준 (시작점)

    - `SEET_SET`(맨 앞을 기준), `SEEK_CUR`(현재 지점을 기준), `SEEK_END`(맨 끝을 기준)

  - `off_t l_len` : lock할 범위의 전체 길이 지정 (0 : 파일 전체 길이)

  - `pit_t l_pid` : 내가 지정하는 값이 아니라 OS가 알려주는 값, lock이 available하지 않을 때 현재 lock을 가지고 있는 프로세스의 pid를 알려줌

  - **lock을 요구할 떈 파일 전체에 대해 요구하면 안되고, 내가 접근하려고 하는 record에 대해서만 lock을 요구해야 한다.**

  - **Concurrency(병행성)** : 여래 개의 쓰레드가 **동시에** 작업을 할 수 있다.

<br/>
