## Git - 조각 지식 모음

<br/>

- 깃(Git)와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_piece_info.md#gitignore-%ED%8C%8C%EC%9D%BC"><code>.gitignore</code> 파일</a>
- <a href=""><code>npm install</code> 시 주의 사항</a>
- <a href=""><code>git checkout</code> (브랜치 이동) 시 주의 사항</a>
- <a href="">깃 브랜치 (branch) 작명 컨벤션</a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## <code>.gitignore</code> 파일

- <code>.gitignore</code>은 Git에서 커밋을 할 때, <strong>무시하고 싶은 파일들의 이름</strong>을 기록하는 파일이다.

  - Git은 기본적으로 디렉토리에서 (숨겨진 파일 포함) 모든 파일을 참조할 수 있다.

  - 따라서 커밋할 때마다 업로드하고 싶지 않은 파일들을 매번 제외해야 하는 귀찮음을 없에기 위해 <code>.gitignore</code> 파일을 만들어 사용한다.

<br/>

- <code>.gitignore</code> 파일 사용 예시

  ```
  .DS_Store
  /node_modules
  /screenshots
  ```

- npm으로 설치한 패키지의 소스 파일(/node_modules)은 용량이 크기 때문에 깃으로 관리하지 않는다.

<br/><br/>

## <code>npm install</code> 시 주의 사항

- 원격 저장소에서 초기 세팅한 파일들을 내 로컬 저장소로 clone 받고, npm install부터 하고나서 branch 생성해야 된다고 한다. (이유는 모르곘지만)

<br/><br/>

## <code>git checkout</code> (브랜치 이동) 시 주의 사항

- 작업 내역이 꼬일 수 있으므로, <strong>반드시 작업 내용을 모두 커밋하고 나서</strong> 브랜치를 이동한다.

<br/><br/>

## 깃 브랜치 (branch) 작명 컨벤션

- 보통 branch명은 <strong>camelCase</strong>로 작성한다.

- 예시 : <code>feature/productDetail</code>

<br/>

- <strong>브랜치 기능 별 라벨명</strong>

  - <code>feature</code> : 기능 구현할 때

  - <code>develop</code> : 여러 기능을 합쳐서 테스트할 때

  - <code>release</code> : 배포 전 최종 테스트할 때

  - <code>hotfix</code> : 배포 후 급하게 버그를 수정할 때

<br/>

- <a href="https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow">Gitflow Workflow</a>를 참고하면 도움이 된다.
