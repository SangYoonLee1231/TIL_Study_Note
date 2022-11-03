# Git - 깃으로 자신의 레포지토리 (Repository) 관리하기

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_manage_my_repository.md#1-%EC%82%AC%EC%A0%84-%EC%9E%91%EC%97%85">1. 사전 작업</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_manage_my_repository.md#2-%ED%8F%B4%EB%8D%94-b%EB%A1%9C%EC%BB%AC-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%99%80-repository-a%EC%9B%90%EA%B2%A9-%EC%A0%80%EC%9E%A5%EC%86%8C%EB%A5%BC-%EC%84%9C%EB%A1%9C-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0-clone-repository">2. 로컬 저장소와 원격 저장소를 서로 연동하기 (Clone Repository)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_manage_my_repository.md#3-%EA%B9%83-%EC%BB%A4%EB%B0%8B%ED%95%98%EA%B8%B0">3. 깃 커밋하기</a>

<br/><br/>

- 자신의 클라이언트 (로컬 저장소) 에서 깃으로 자신의 Repository (원격 저장소) 를 관리하는 방법에 대해 정리해보고자 한다.

- 새 폴더와 새 Repository를 만들어서 작업하는 것을 전제로 한다.

<br/><br/><br/>

### 1. 사전 작업

- <strong>1-1.</strong> <strong>자신의 컴퓨터 (로컬 저장소) 에서 다룰 본인의 Repository를 깃허브에서 새로 하나 생성한다.</strong>

  - 이제부터 이 Repository를 <strong>Repository A</strong>라 부른다.

<br/>

- <strong>1-2.</strong> <strong>본인의 컴퓨터의 원하는 디렉토리(위치)에 Repository A를 다룰 폴더를 새로 생성해준다.</strong>

  - 이제부터 이 폴더를 <strong>폴더 B</strong>라 부른다.

<br/><br/>

### 2. '폴더 B'(로컬 저장소)와 'Repository A'(원격 저장소)를 서로 연동하기 (Clone Repository)

- <strong>2-1.</strong> <strong>터미널을 열고 폴더 B의 디렉토리로 이동한다.</strong>

<br/>

- <strong>2-2.</strong> <strong>폴더 B의 디렉토리에서 git을 초가화하는 명령어를 입력한다.</strong>

  👉 <code>git init</code>

  - 깃 초기화 명령으로, "이제부터 해당 폴더를 깃으로 관리하겠습니다" 라는 의미라 생각하면 된다.

<br/>

- <strong>2-3.</strong> <strong>폴더 B와 Repository A (원격 저장소) 를 서로 연결하는 명령어를 입력한다.</strong>

  👉 <code>git remote add origin <strong>[원격저장소 URL]</strong></code>

  (origin은 원격저장소 URL의 별명이다.)

  - <strong>원격저장소URL</strong>에는 자신의 연동하고자 할 Repository A의 주소를 입력하면 된다.

    - Repository 주소 형태 : https://github.com/계정/레포지토리.git

  - (<code>git remote -v</code> 명령어를 입력하면, 원격 저장소에 잘 연결이 되었는지 확인할 수 있다.)

<br/>

- <strong>이제 폴더 B는 Repository A의 로컬 저장소가 되었다.</strong>

<br/><br/>

### 3. 깃 커밋하기

- <strong>이제 로컬 저장소 (폴더 B) 에서 파일을 수정하고 깃으로 커밋하면, 원격 저장소 (깃허브의 Repository A) 에 그대로 반영된다.</strong>

- 이 과정은 총 3가지로 설명할 수 있다.

  - <strong>3-1.</strong> <strong>수정된 모든 파일 및 폴더를 Staging에 추가</strong>

    👉 <code>git add .</code>

  - <strong>3-2.</strong> <strong>Staging에 있는 것들을 그대로 커밋</strong>

    👉 <code>git commit -m "커밋 메세지"</code>

  <!-- - (처음으로 push 하기 전, 브랜치 설정 작업이 한 번 필요하다.)

    👉 <code>git push --set -upstream origin master</code> -->

  - <strong>3-3.</strong> <strong>원격 저장소에 푸쉬</strong>

    👉 <code>git push origin [브랜치 이름]</code>

<br/>

- 앞으로 로컬 저장소에서 작업하고 수정 사항을 Repository A에 반영할 때마다 <strong>위 과정을 반복</strong>해주면 된다.

- 만일 자신의 로컬 저장소가 아닌 다른 곳에서 Repository를 수정하였고

  <strong>이 수정 사항을 자신의 로컬 저장소에도 그대로 반영하고 싶다면</strong>

  <code>git fetch origin</code> 명령어를 사용해주면 된다.

<br/>

- <strong><a href="https://desktop.github.com/">GitHub Desktop</a> 프로그램</strong>을 이용하면 깃 명령어를 사용하지 않고도 위의 작업을 손쉽게 할 수 있다.

  - 만일 명령어와 터미널이 본인에게 진입 장벽으로 작용한다면, 이 프로그램을 우선 사용해보면서 깃에 친숙해져 보는 건 어떨까.
