# 명령어 정리 (터미널, 깃)

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_command.md#%ED%84%B0%EB%AF%B8%EB%84%90-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%AA%A8%EC%9D%8C">터미널 명령어 모음</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_command.md#window">Window</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_command.md#windows-%EC%BB%A4%EB%A7%A8%EB%93%9C-vs-mac-os-%ED%84%B0%EB%AF%B8%EB%84%90-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%B9%84%EA%B5%90">Windows 커맨드 vs Mac OS 터미널 명령어 비교</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_command.md#%EA%B9%83-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%AA%A8%EC%9D%8C">깃 명령어 모음</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Git/git_command.md#%EA%B9%83-%EB%8B%A8%EC%B6%95%ED%82%A4-%EC%84%A4%EC%A0%95">깃 단축키 설정</a>
- <a href=""></a>

<br/><br/>

## 터미널 명령어 모음

### Window

- <code>cd [이동할 경로]</code> (change directory) : 커멘트 창을 해당 위치로 이동

  - <code>cd..</code> : 그 전의 경로로 이동

  - <code>cd C:\\</code> : 기본 경로가 변경

  - <code>D:</code> : D드라이브로 이동 (앞에 <code>cd</code> 작성하면 안됨)

- <code>dir</code> (directory) : 현재 위치의 파일과 디렉토리(폴더) 목록 보기

- <code>md [생성할 폴더 이름]</code>, <code>mkdir [생성할 폴더 이름]</code> (make directory) : 디렉토리(폴더) 생성

- <code>rd [삭제할 폴더 이름]</code>, <code>rmdir [삭제할 폴더 이름]</code> (remove directory) : 디렉토리(폴더) 삭제

  - <code>/s</code> : 입력시 폴더 안에 파일이 있더라도 전부 완전 삭제 (휴지통 가지 X)

- <code>path</code> : 환경변수 path 보기

- <code>cls</code> : 현재 명령 프롬프트 창 초기화 (이전 명령어 결과를 지움)

- <code>del [삭제할 파일명]</code> : 파일 삭제

- <code>copy [복사할 파일명] [복사할 위치 경로]</code> : 파일 복사

  - <code>xcopy [복사할 파일명] [복사할 위치 경로]</code> : 숨김 파일도 모두 복사

- <code>move [파일명] [이동할 위치 경로]</code> : 파일 이동

- <code>rename [현재 파일명] [변경후 파일명]</code> : 파일명 또는 디렉토리면 변경

- <code>date</code> : 현재 날짜 보기 (새로운 날짜를 입력하라고 할 시 그냥 엔터치면 됨)

- <code>help</code> : 명령어 도움말 보기

- <code>ipconfig</code> : 네트워크 설정상태 보기 (/all 옵션 붙여 상세한 설정 정보 볼 수 있음)

- <code>tasklist</code> : 현재 실행중인 프로세스 모두 표시

- <code>exit</code> : 재 명령 프롬프트 창 종료

<br/>

### Windows 커맨드 vs Mac OS 터미널 명령어 비교

<table>
    <thead>
        <tr>
            <th>명령어</th>
            <th>Windows CMD</th>
            <th>Max OS Terminal</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>현재 디렉토리</th>
            <th>cd</th>
            <th>pwd</th>
        </tr>
        <tr>
            <th>현재 디렉토리 파일 리스트 보기</th>
            <th>dir</th>
            <th>ls</th>
        </tr>
        <tr>
            <th>디렉토리 이동</th>
            <th>cd</th>
            <th>cd</th>
        </tr>
        <tr>
            <th>디렉토리 생성</th>
            <th>md, mkdir</th>
            <th>mkdir</th>
        </tr>
        <tr>
            <th>디렉토리 삭제</th>
            <th>rm, rmdir</th>
            <th>rmdir</th>
        </tr>
        <tr>
            <th>화면 클리어</th>
            <th>cls</th>
            <th>clear</th>
        </tr>
        <tr>
            <th>null 파일 생성</th>
            <th>type NUL></th>
            <th>touch</th>
        </tr>
        <tr>
            <th>파일삭제</th>
            <th>del</th>
            <th>rm</th>
        </tr>
        <tr>
            <th>파일이동</th>
            <th>move</th>
            <th>mv</th>
        </tr>
        <tr>
            <th>파일/디렉토리 이름 바꾸기</th>
            <th>ren, rename</th>
            <th>mv</th>
        </tr>
        <tr>
            <th>Explorer / Finder에서 열기</th>
            <th>start</th>
            <th>open</th>
        </tr>
    </tbody>
</table>

<br/><br>

## 깃 명령어 모음

- git config

- git commit

- git add -option

### 깃 단축키 설정

- git config --global alias.st status : git의 status 명령어를 st로 줄여쓰기 허용

<br/>

- 깃 명령어를 모두 확인할 수 있는 공식 문서 👉<a href="https://git-scm.com/docs">바로가기 </a>
