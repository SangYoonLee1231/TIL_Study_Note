# CSR vs SSR

> 참고 자료 : <a href="https://www.inflearn.com/course/lecture?courseSlug=%EB%94%B0%EB%9D%BC%ED%95%98%EB%8A%94-%EB%A0%88%EB%94%A7&unitId=123111&tab=curriculum">따라하며 배우는 노드, 리액트 시리즈 - 레딧 사이트 만들기(NextJS) (인프런 / John Ahn님)</a>,  
> <a href="https://fastcampus.co.kr/courses/203527">김민태의 프론트엔드 아카데미 : 제 1강 JavaScript & TypeScript Essential (패스트캠퍼스 / 김민태님)</a>,  
> <a href="https://www.sarah-note.com/%ED%81%B4%EB%A1%A0%EC%BD%94%EB%94%A9/posting2/">SSR vs CSR 비교 설명, Next.js가 탄생하게 된 이유 (블로그 포스트)</a>,  
> <a href="https://www.startupcode.kr/company/blog/archives/12">CSR과 SSR의 장단점 (블로그 포스트)</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NextJS/ssr_vs_csr.md#ssr-vs-csr">SSR vs CSR</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NextJS/ssr_vs_csr.md#ssr%EA%B3%BC-csr%EC%9D%98-%ED%8A%B9%EC%A7%95-%EC%9E%A5%EB%8B%A8%EC%A0%90">SSR과 CSR의 특징 (장단점)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NextJS/ssr_vs_csr.md#%EC%96%B4%EB%96%A4-%EB%B0%A9%EC%8B%9D%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%A0-%EA%B2%83%EC%9D%B8%EA%B0%80">어떤 방식을 사용할 것인가</a>

<br/><br/>

## SSR vs CSR

- 웹에서 UI를 만드는 역할은 보통 HTML이 담당하고, JavaScript를 이용해서 이 HTML을 조작할 수 있다.

- 따라서 JavaScript를 통해 UI를 제공해줄 수도 있는 것이다.

<br/>

- 그런데 결론적으로는, 어떤 식으로든 UI를 만들기 위해선 최종적으로 HTML 형태가 만들어져 있어야 하기 때문에

- 이 HTML을 **어디에서 만드는 지**가 굉장히 중요해진다.

  - 웹 서버에서 UI에 필요한 정보들이 담긴 HTML을 미리 만들어 브라우저로 전송하는 방식을 <strong>SSR(Server Side Rendering)</strong>이라 한다.

    - 웹 서버에서 HTML을 주도적으로 만든다.

  - 웹 서버에 있는 HTML에는 UI에 대한 내용이 거의 없고, 브라우저에서 JS가 실행되면서 필요한 UI를 그떄그때 생성해내는 방식을 <strong>CSR(Client Side Rendering)</strong>이라 한다.

    - 클라이언트에서 HTML을 주도적으로 만든다.

    - React, Vue의 SPA(Single Page Application)에서 주로 쓰이는 기법이다.

<br/><br/>

## SSR과 CSR의 특징 (장단점)

- HTML을 만들 때 필요한 **데이터**는 브라우저에서 서버에 요청을 하여 데이터 베이스에서 가져온다.

<br/>

- 이 때 **SSR 방식**은 서버에서 HTML(UI)을 만들 때마다 필요한 모든 데이터를 가져온다.

- 따라서 클라이언트에서 페이지를 이동하거나 어떤 요청이 발생할 경우, 서버에서 매번 데이터 베이스에 접근하여 필요한 데이터를 가져와 HTML을 처음부터 새로 만들어주어야 한다.

- 이는 **서버 부하** 등의 문제를 일으키는 원인이 된다.

- 대신 SSR 방식은 **SEO(Search Engine Optimization / 검색 엔진 최적화)가 가능하다.** (자세한 내용은 아래에 설명)

<br/>

- 반면에 **CSR 방식**은 브라우저에서 HTML(UI)을 만들 때, 데이터를 제외한 UI 코드만을 프론트 서버에서 받아오고,

- 데이터가 필요할 때 클라이언트에서 서버에 요청하여 필요한 정보만 받는다.

- 따라서 SSR 방식에 비해 **서버 부하가 덜하다.**

- 단, CSR 방식은 **초기 진입 속도가 느리다**는 단점이 있다. (자세한 설명은 아래 ChatGPT 답변 참고)

- 또한, 초기 HTML에 데이터가 없기 때문에, 검색 엔진이 해당 페이지에서 정보를 제대로 수집하지 못할 수 있으므로 **SEO(Search Engine Optimization / 검색 엔진 최적화)에 취약하다.**

<br/>

> ### ☝🏻 Q. CSR과 SSR의 초기 진입 속도는 어떻게 다른가요? (By ChatGPT)
>
> CSR(Client Side Rendering)과 SSR(Server Side Rendering)의 초기 진입 속도는 기본적으로 다릅니다.
>
> CSR은 초기 페이지 요청 시 서버에서는 HTML 문서와 (클라이언트에서 데이터를 로드하고 렌더링하는 로직이 포함된) JavaScript 파일을 클라이언트로 전달합니다. 이후, 클라이언트는 JavaScript 파일을 실행하여 데이터를 로드하고 렌더링합니다. 이 과정은 초기 진입 속도가 느릴 수 있으며, 특히 첫 번째 페이지 로딩 시간이 길어질 수 있습니다. 클라이언트는 서버에서 전달받은 데이터를 사용하여 동적으로 페이지를 렌더링하므로, 사용자가 상호작용하는 동안에는 페이지 갱신이 빠르게 이루어질 수 있습니다.
>
> 반면 SSR은 초기 페이지 요청 시 서버에서 데이터를 미리 렌더링하여 완성된 HTML 문서로 전달합니다. 클라이언트는 이미 완성된 HTML을 받아 즉시 렌더링할 수 있으므로 초기 진입 속도가 빠릅니다. 사용자는 초기 페이지를 더 빠르게 볼 수 있지만, 동적인 변화가 있는 경우 서버에 요청을 보내고 새로운 HTML을 받아와야 하므로 사용자 경험의 지연이 발생할 수 있습니다.
>
> 따라서, CSR은 초기 페이지 로딩이 오래 걸리지만 상호작용 시 부드럽고 빠른 경험을 제공할 수 있으며, SSR은 초기 페이지 로딩이 빠르지만 동적인 변화가 있는 경우 지연이 발생할 수 있습니다. 각각의 장단점을 고려하여 프로젝트의 요구사항과 성능 목표에 맞는 렌더링 방식을 선택하는 것이 중요합니다.

<br/><br/>

## 어떤 방식을 사용할 것인가

- 어떤 웹앱이든 CSR 방식 혹은 SSR 방식으로 개발할 수 있다.

- 단지 어떤 방식이 더 효과적인지는 그 앱의 성격에 따라 달라질 수 있다.

- 따라서 개발자가 적잘한 방식을 잘 선택하여야 잘못된 선택에 따른 비효율을 예방할 수 있는 것이다.

<br/>

#### <a href="https://sylagape1231.tistory.com/122">📃 직접 작성한 기술 블로그 포스트 'CSR과 SSR이란 무엇일까?' 보러가기</a>

<br/>
