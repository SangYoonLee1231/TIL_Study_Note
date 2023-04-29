# CSR vs SSR

> 참고 자료 : <a href="https://www.inflearn.com/course/lecture?courseSlug=%EB%94%B0%EB%9D%BC%ED%95%98%EB%8A%94-%EB%A0%88%EB%94%A7&unitId=123111&tab=curriculum">따라하며 배우는 노드, 리액트 시리즈 - 레딧 사이트 만들기(NextJS) (인프런 / John Ahn님)</a>,
> <a href="https://fastcampus.co.kr/courses/203527">김민태의 프론트엔드 아카데미 : 제 1강 JavaScript & TypeScript Essential (패스트캠퍼스 / 김민태님)</a>,
> <a href="https://www.sarah-note.com/%ED%81%B4%EB%A1%A0%EC%BD%94%EB%94%A9/posting2/">SSR vs CSR 비교 설명, Next.js가 탄생하게 된 이유 (블로그 포스트)</a>,
> <a href="https://www.startupcode.kr/company/blog/archives/12">CSR과 SSR의 장단점 (블로그 포스트)</a>

<br/>

### 목차

- <a href="">SSR vs CSR</a>
- <a href="">SSR과 CSR의 특징 (장단점)</a>

<br/><br/>

## SSR vs CSR

- 웹에서 UI를 만드는 역할은 HTML이 담당한다.

- 그리고 JavaScript를 이용해서 이 HTML을 조작할 수 있다.

- 따라서 JavaScript를 통해 UI를 제공해줄 수도 있다.

<br/>

- 그런데 결론적으로는, 어떤 식으로든 UI를 만들기 위해선 최종적으로 HTML 형태가 만들어져 있어야 하기 때문에,

- 이 HTML을 어디에서 만드는 지가 굉장히 중요해진다.

  - 웹 서버에서 UI에 필요한 정보들이 담긴 HTML을 이미 만들어 브라우저로 전송하는 방식을 <strong>SSR(Server Side Rendering)</strong>이라 한다.

    - 웹 서버에서 HTML을 주도적으로 만든다.

  - 웹 서버에 있는 HTML에는 UI에 대한 내용이 거의 없고, 브라우저에서 JS가 실행되면서 필요한 UI를 그떄그때마다 생성해내는 방식을 <strong>CSR(Client Side Rendering)</strong>이라 한다.

    - 클라이언트에서 HTML을 주도적으로 만든다.

    - React, Vue의 SPA(Single Page Application)에서 주로 쓰이는 기법이다.

<br/><br/>

## SSR과 CSR의 특징 (장단점)

- HTML을 만들 때 필요한 **데이터**는 브라우저에서 서버에 요청을 하여 데이터 베이스에서 가져온다.

<br/>

- 이 때 **SSR 방식**은 서버에서 HTML(UI)을 만들 때마다 필요한 모든 데이터를 가져온다.

- 따라서 클라이언트에서 페이지를 이동하거나 어떤 요청이 발생할 경우, 서버에서 매번 데이터 베이스에 접근하여 필요한 데이터를 가져와 HTML을 처음부터 새로 만들어주어야 한다.

- 이는 **서버 부하** 등의 문제를 일으키는 원인이 된다.

- 대신 SSR 방식은 SEO(Search Engine Optimization / 검색 엔진 최적화)가 가능하다. (자세한 내용은 아래에 설명)

<br/>

- 반면에 **CSR 방식**은 브라우저에서 HTML(UI)을 만들 때, 데이터를 제외한 UI 코드만을 프론트 서버에서 받아오고,

- 데이터가 필요할 때 클라이언트에서 서버에 요청하여 필요한 정보만 받는다.

- 따라서 SSR 방식에 비해 **서버 부하가 덜하다.**

- 단, UI 코드를 프론트 서버에서 받아올 때 JS 파일에 한 번에 번들되어 오기 때문에 **초기 진입 속도가 느리다**는 단점이 있다.

- 또한, 초기 HTML에 데이터가 없기 때문에, 검색 엔진이 해당 페이지에서 정보를 제대로 수집하지 못할 수 있으므로, **SEO(Search Engine Optimization / 검색 엔진 최적화)에 취약하다.**

<br/>

<!-- ##

- -->