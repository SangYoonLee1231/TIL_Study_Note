# Git - 깃으로 Branch (브랜치) 생성하여 협업하기 심화 (+ 오류 해결하기)

> 참고 자료 : 부트캠프 학습 자료

<br/>

### 목차

- <a href="">깃 브랜치 (branch) 작명 컨벤션</a>
- <a href=""><code>git checkout</code> (브랜치 이동) 시 주의 사항</a>
- <a href=""></a>
- <a href=""></a>

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

<br/><br/>

## <code>git checkout</code> (브랜치 이동) 시 주의 사항

- 작업 내역이 꼬일 수 있으므로, <strong>반드시 작업 내용을 모두 커밋하고 나서</strong> 브랜치를 이동한다.
