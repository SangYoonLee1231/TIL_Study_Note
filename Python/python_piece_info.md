## Python - 조각 지식 모음

<br/>

* 파이썬과 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree</a>

<br/>

### 목차

* <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_piece_info.md#%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%B3%80%EC%88%98%EC%9D%98-scope-%EB%B2%94%EC%9C%84">파이썬에서 변수의 scope 범위</a>
* <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_piece_info.md#2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8-%EC%8B%9C-%EC%9C%A0%EC%9D%98-%EC%82%AC%ED%95%AD">2차원 배열 선언 시 유의 사항</a>

<br/>

## 파이썬에서 변수의 scope 범위

* 파이썬에서 <code>for</code>문이나 <code>if</code>문, 또는 함수의 내부에 선언한 지역 변수는 놀랍개도 main 함수 영역(indent가 없는 코드 영역)에서도 전역 변수처럼 그대로 사용된다.

* 다만 이러한 지역 변수는 다른 함수(<code>for</code>문, <code>if</code>문도 표함)의 내부 영역에선 참조할 수 없다.

<br/>

## 2차원 배열 선언 시 유의 사항

* 다음과 같이 2차원 배열을 선언하면 안 된다.

```python
[ [0] * n ] * n
```