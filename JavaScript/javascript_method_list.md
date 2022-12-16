# JavaScript - 내장 메소드 정리

<br/>

### 목차

- <a href="">수학 관련 메소드</a>
- <a href="">문자 관련 메소드</a>
- <a href="">알고리즘 관련 메소드</a>

<br/><br/>

## 수학 관련 메소드

- <strong><code>[수].toString(2)</code></strong> : [수]를 2진수로 변환

- <strong><code>Number.isInteger([수])</code></strong> : [수]가 정수이면 "true", 실수이면 "false" 반환

  - JS는 정수와 실수를 모두 <code>'number'</code> 하나의 타입으로 다룬다.

- <strong><code>Number()</code> VS <code>parseInt()</code></strong> :

  - <strong><code>Number()</code></strong> : 전체가 숫자인 문자열에서 소수점까지 모두 형변환

  - <strong><code>parseInt()</code></strong> : (숫자로 시작하는) 문자열에서 정수 부분만 뽑아서 형변환 (소수점 버리기 가능)

<br/><br/>

## 문자 관련 메소드

- <strong><code>[문자열].match(new RegExp(/^[0-9]/))</code></strong> : [문자열]에서 정규표현식 /^[0-9]/에 매칭되는 항목들을 배열로 반환, 매칭되는 항목이 없으면 null을 반환

<br/><br/>

## 알고리즘 관련 메소드

- <strong><code>[배열].sort()</code></strong> : 배열을 유니코드 문자 순으로 정렬

  - <strong><code>[배열].sort((a, b) => a - b)</code></strong> : 숫자 배열을 오름차순으로 정렬

  - <strong><code>[배열].sort((a, b) => b - a)</code></strong> : 숫자 배열을 내림차순으로 정렬
