## Git - 조각 지식 모음

<br/>

- 깃(Git)와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_piece_info.md#gitignore-%ED%8C%8C%EC%9D%BC">.gitignore 파일</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

### <code>.gitignore</code> 파일

- <code>.gitignore</code>은 Git에서 커밋을 할 때, <strong>무시하고 싶은 파일들의 이름</strong>을 기록하는 파일이다.

  - Git은 기본적으로 디렉토리에서 (숨겨진 파일 포함) 모든 파일을 참조할 수 있다.

  - 따라서 커밋할 때마다 업로드하고 싶지 않은 파일들을 매번 제외해야 하는 귀찮음을 없에기 위해 <code>.gitignore</code> 파일을 만들어 사용한다.

<br/>

- <code>.gitignore</code> 파일 사용 예시

  ```
  .DS_Store
  /screenshots
  ```
