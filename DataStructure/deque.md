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

<br/>

- ✨ <strong>Deque은 탐색 연산을 제공하지 않는다.</strong> Stack와 Deque처럼 일반적인 탐색이 안 되는 자료구조이기 때문이다.  
  이는 Deque을 리스트로 구현하든 연결 리스트로 구현하든 마찬가지이다.

<br/><br/>

## (Python) collections 모듈에 있는 deque 패캐지 설명

- 파이썬에선 deque 패캐지를 제공한다. 이는 collections라는 모듈에 있다.

- 사용을 위해서는 <code>from collections import deque</code>를 가장 위에 적어주어야 한다.

<br/>

- deque에 자주 쓰이는 8가지 함수 및 표현(expression) 정리

  왼쪽 끝이 맨 앞, 오른쪽 끝이 맨 뒤라 가정한다.

  - <code>dq.appendleft(value)</code> : 맨 앞에 value 데이터를 삽입한다.

  - <code>dq.append(value)</code> :
    맨 뒤에 value 데이터를 삽입한다.

  - <code>dq.popleft()</code> : 맨 앞의 데이터를 삭제 후 반환한다.

  - <code>dq.pop()</code> : 맨 뒤의 데이터를 삭제 후 반환한다.

  - <code>len(dq)</code> : 덱에 남아있는 데이터의 수를 반환한다.

  - <code>if dq</code> : 덱에 데이터가 존재하는 확인한다. 반대로 <code>if not dq</code>는 덱이 비어있는지를 확인한다.

  - <code>dq[0]</code> : 맨 앞의 데이터를 반환한다. (삭제 X)

  - <code>dq[-1]</code> : 맨 뒤의 데이터를 반환한다. (삭제 X)

<br/><br/>

> 사진 출처 : <a href="https://www.codetree.ai/missions">Code Tree - Novice High</a>
