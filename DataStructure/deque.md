# 순차적 자료구조 : 덱 (Deque)

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

### 목차

- <a href="">덱 (Deque) 소개</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## 덱 (Deque) 소개

- <strong>덱</strong>은 스택과 큐의 특성을 모두 합친 새로운 선형(linear) 자료구조이다.

- 덱은 <strong>앞에서 삽입</strong>, <strong>뒤에서 삽입</strong>, <strong>앞에서 삭제</strong>, <strong>뒤에서 삭제</strong>가 모두 가능하며, 모든 연산의 시간복잡도는 <code>O(1)</code>이다.

    <img src="img/deque1.png">

<br/>

- 4가지 기본 연산을 제공한다.

  - 삽입 연산 : <strong>push front(앞에서 삽입), push back(뒤에서 삽입)</strong>

  - 삭제 연산 : <strong>pop front(앞에서 삭제), pop back(뒤에서 삭제)</strong>

<br/><br/>

## (Python) collections 모듈에 있는 deque 패캐지 설명

- 파이썬에선 deque 패캐지를 제공한다. 이는 collections라는 모듈에 있다.

- 사용을 위해서는 <code>from collections import deque</code>를 가장 위에 적어주어야 한다.

<br/>

- deque에 자주 쓰이는 8가지 함수 및 표현(expression) 정리

  - <code>dq.appendleft(E)</code>

  - <code>dq.append(E)</code>

  - <code>dq.popleft()</code>

  - <code>dq.pop()</code>

  - <code>len(dq)</code>

  - <code>if dq</code>

  - <code>dq[0]</code>

  - <code>dq[-1]</code>

  - <code></code>

> 사진 출처 : <a href="https://www.codetree.ai/missions">Code Tree - Novice High</a>
