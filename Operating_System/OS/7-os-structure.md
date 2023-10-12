# 7. OS의 구조 (OS Structure)

<br/>

> 참고 자료 : '운영체제' 학부 수업 자료 (이윤석 교수님)

- 📔 <strong><a href="https://drive.google.com/file/d/1zSIOzKWUjz93BfUfLVKvi4FSQqrD4XOH/view?usp=sharing">강의 내용 필기 노트 보러가기 (Lec 2)</a></strong>

<br/><br/>

### 목차

- <a href="">MS-DOS</a>
- <a href="">Monolithic Structure (단일 몸체 커널)</a>
- <a href="">Layered Structure</a>
- <a href="">Micro-kernel</a>
- <a href="">Modules (모듈)</a>
- <a href="">Virtual Machines</a>

<br/><br/>

> **완벽한 시스템이란 없다. 이점 뒤엔 반드시 이면이 존재한다.**

<br/>

## MS-DOS

- MS에서 개발한 거의 최초의 OS

- PC의 플로피디스크에 정보를 저장하는 저장지원 시스템 - 디스켓 관리 시스템

<br/>

- Application Program 아래에 기본적으로 항상 메모리에 올라와있는 resident system program이 있음 (커널 역할 수행)

- 그 아래에 MS-DOS device drivers (장치 관리자)가 있고

- 최하단에 ROM BIOS device drivers가 있음

  - BIOS : H/W에 탑재되어 있는 폼웨어

<br/>

- 대부분의 어플리케이션이 하드웨어에 직접 접근하는 것을 허락

- 어플리케이션 간 protection 개념이 굉장히 약했음

- OS에 대한 모듈화 개념이 부재

- 효율성↓, 보호↓, 보안에도 취약

<br/><br/><br/>

## Monolithic Structure (단일 몸체 커널)

- 모든 기능이 한 몸안에 있는 커널 구조

- 기능이 분화, 모듈화 시작 (UNIX)

- 커널 안으로 들어오고 나면, 다른 모듈에 접근할 땐 Function Call의 형태로 해당 기능을 호출

<br/>

- **단점**

  - 설계에서 구현까지 협업하기 어려움

  - 안정성 떨어짐 (버그 발생 시 전체로 금방 파금됨)

<br/><br/><br/>

## Layered Structure

- 개발하는 입장에서 방대한 소프트웨어를 좀 더 안정적으로 만들기 위해 계층별로 S/W를 구성하는 Layered Structure을 취한다.

- 상단의 레이어는 항상 바로 밑에 있는 레이어의 기능만 사용할 수 있다.

<br/>

- **장점** : 설계 단순화, 디버깅 쉬움, 기능 확장 용이

<br/>

- **단점**

  - 설계 어려움 (시스템의 깊은 이해 필요)

  - 더 아래의 계층에 접근하기 위해 반드시 중간 계층을 거쳐야 함

<br/><br/><br/>

## Micro-kernel

- Monolithic Kernel의 문제점인 싱글 버그가 전체 커널을 감염시킬 위험성을 배제하기 위해

  꼭 커널 모드에 있어야 하는 기능을 제외하고는 나머지를 유저 영역으로 옮긴 커널 구조

- 프로세스가 독립적인 객체들로 구성되어 있으므로, 프로세스 간 소통할 때 더 이상 Function Call을 사용하지 못하고

  대신 Message Passing 방식을 사용한다.

<br/>

- Mach는 현대에 쓰이는 OS의 바탕이 된다.

<br/>

- **장점**

  - 버그가 다른 프로세스로 전염되지 않는다. (프로세스가 독립적인 개체이므로)

  - 기능 확장이 쉽고 porting 역시 쉽다.

  - 커널이 작으므로, 코드 수도 적고 덩달아 버그 가능성도 낮아져 커널의 신뢰도가 올라간다.

  - 보안과 Protection ↑, 안정성↑

<br/>

- **단점**

  - Message Passing을 위해 유저와 커널 스페이스를 계속해서 오가야 하므로 Performance overhead가 있다.

  - Message Passing이 OS를 매개로 이루어지므로 compuation time↑

<br/><br/><br/>

## Modules (모듈)

- 독립적으로 개발되고 관리되는 소프트웨어 단위

- layer에 비해 덜 엄격하게 (flexible하게) 정의 가능

<br/>

- 대부분의 현대 OS들은 커널 모듈방식을 사용하여 개발된다.

- 이는 객체 지향 접근법 (Object-Oriented Approach) 을 사용한다.

<br/>

- OOP의 장점이자 기본 철학

  - Hiding the Details : 꼭 필요한 인터페이스만 사람들에게 제공하고, 보여질 필요가 없는 것들은 감춘다.

<br/><br/><br/>

## Virtual Machines

- 하드웨어 위에 독립된 소프트웨어 형식의 가상 머신을 제공

- 여러 개의 OS를 서포트 할 수 있다.

<br/>

- **Hypervisor**

  - Virtual Machine을 만들기 위해서 지원하는 계층

  - ex) VMWare Structure, Virtual Box 등

<br/>

- **장점**

  - 광장히 Flexible하다.

  - 다양한 SW 지원 환경을 제공한다.

  - 시스템 빌딩 혹은 커널 개발 시 매우 유용한 기능을 제공한다.

<br/><br/>
