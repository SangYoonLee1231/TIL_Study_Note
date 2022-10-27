# 깃으로 Branch (브랜치) 생성하여 협업하기

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_branch.md#%EB%B8%8C%EB%9E%9C%EC%B9%98-branch-%EB%9E%80">브랜치 (Branch) 란?</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_branch.md#%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%A5%BC-%EC%83%9D%EC%84%B1%ED%95%98%EC%97%AC-%ED%98%91%EC%97%85%ED%95%98%EB%8A%94-%EB%B0%A9%EC%8B%9D">브랜치를 생성하여 협업하는 방식</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_branch.md#%EA%B9%83-%EB%AA%85%EB%A0%B9%EC%96%B4">깃 명령어</a>

<br/><br/>

## 브랜치 (Branch) 란?

- 브랜치란 깃의 하나의 Repository 내에서 특정한 작업을 진행하기 위해 독립적으로 만들어진 공간이다.

- 각각의 브랜치는 서로에게 영향을 주지 않기 때문에, 한 프로젝트 내에서 여러 작업을 동시에 진행할 수 있다.

<br/>

- 저장소 (Repository) 를 처음 생성 시, Git에서 'master' (혹은 'main') 브랜치가 만들어진다.

- 다른 브랜치를 생성하지 않으면, 깃에서 이루어지는 모든 작업(commit 등)은 master 브랜치에서 이루어진다.

<br/><br/>

## 브랜치를 생성하여 협업하는 방식

- 여러 명이서 협업을 진행할 때, 우선 master (메인) 브랜치에서 작업 전용 브랜치를 여러개 생성한다.

- 각각의 브랜치에서 서로 작업을 진행하고, 작업이 끝난 사람은 메인 브랜치에 자신의 브랜치의 변경사항을 적용한다.

- 다른 사람에 의해 업데이트 된 (원격 저장소의) 메인 브랜치를 자신(로컬 저장소)의 브랜치로 <code>pull</code>, <code>merge</code> 할 수 있다.

<br/>

### 코드가 순회하는 매커니즘

<img src="img/git_circulation.png">

<br/><br/>

## 깃 명령어

- 원격 저장소 (깃허브 레포지토리) 에서 로컬 저장소로 파일 그대로 가져오기

  ```
  git clone [원격 저장소 주소]
  ```

- 브랜치 생성하기 (반드시 master 브랜치에서 진행해야 한다)

  ```
  git branch [새 브랜치 이름]
  ```

- 현재 브랜치 확인

  ```
  git branch
  ```

- 다른 브랜치로 이동하기

  ```
  git checkout [이동할 브랜치 이름]
  ```

- 브랜치 생성과 동시에 이동하기

  ```
  git checkout -b [생성 및 이동할 브랜치 이름]
  ```

- 원격 저장소에 있는 코드를 로컬 저장소로 가져오기

  ```
  git pull origin [가져올 코드의 해당 브랜치 이름 (주로 master)]
  ```

- 코드 병합하기 : 로컬 저장소에서 현재 브랜치의 코드와 다른 브랜치의 코드를 합칠 때 사용

  ```
  git merge [다른 브렌치의 이름 (주로 master)]
  ```

- 브랜치 삭제하기

  ```
  git branch -d [삭제할 브랜치 이름]
  ```
