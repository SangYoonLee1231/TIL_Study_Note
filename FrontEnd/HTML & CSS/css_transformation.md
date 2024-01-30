# CSS - Transformation

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## Transformation 소개

* 줄여서 <code>transform</code>이라 한다.

* <code>transform</code> 속성은 해당 요소를 말 그대로 '<strong>변형</strong>'하는 CSS 속성이다.

    * 변형 : <strong>회전, 확대/축소, 이동 등등</strong>

<br/>

* <strong>다른 요소의 box를 변형시키지 않고</strong>, 원하는 요소만 독자적으로 변형시킨다.

* 다른 요소는 해당 요소가 변형되었는지 알아차리지 못한다.

    * <code>transform</code>은 box 차원에서 일어나지 않고, <strong>페이지 픽셀의 다른 부분에서 일어나기 때문</strong>이다.

* 일종의 <strong>3D Transformation</strong>이므로 <code>margin</code>, <code>padding</code>이 적용하지 않는다.

<br/>

## Transformation 함수

* <code>transform</code>의 속성값으로 쓰이는 함수를 <strong>Transformation 함수</strong>라 한다.

```css
img {
    transform: rotateX(90deg), rotateY(45deg), rotateZ(30deg);
}
```

<br/>

* <a href="https://developer.mozilla.org/ko/docs/Web/CSS/transform">Transformation 공식 문서</a> 

    * 공식 문서에 있는 다양한 Transformation 함수를 복붙하여 마음껏 사용할 수 있다.

    * <a href="https://developer.mozilla.org/ko/docs/Web/CSS/transform-function">Transformation 함수 기능 설명서</a>

* Transformation 함수 종류 (일부)

    * <code>rotate</code> : 회전

    * <code>translate</code> : 이동

    * <code>scale</code> : 확대/축소
    
    * <code>perspective</code>

    * <code>matrix</code>

    * <code>skew</code> : 비스듬히 기울이기

<br/>

## ✨ Trasition을 통한 애니메이션 효과 부여

* <code>transform</code>과 <code>transition</code>을 <strong>함께 사용</strong>하면, 아름다운 애니메이션을 연출할 수 있다.

```css
img {
    transition: transform 1s ease-in-out;
}
img:hover {
    transform: rotateY(360deg), scale(0.5);
}
```