# JavaScript - 내장 메소드 정리

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_method_list.md#%EC%88%98%ED%95%99-%EA%B4%80%EB%A0%A8-%EB%A9%94%EC%86%8C%EB%93%9C">수학 관련 메소드</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_method_list.md#%EB%AC%B8%EC%9E%90-%EA%B4%80%EB%A0%A8-%EB%A9%94%EC%86%8C%EB%93%9C">문자 관련 메소드</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_method_list.md#%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B4%80%EB%A0%A8-%EB%A9%94%EC%86%8C%EB%93%9C">알고리즘 관련 메소드</a>

<br/><br/>

## 수 관련 메소드

- <strong><code>[수].toString(2)</code></strong> : [수]를 2진수로 변환

- <strong><code>Number.isInteger(n)</code></strong> : n이 정수이면 "true", 실수이면 "false" 반환

  - JS는 정수와 실수를 모두 <code>'number'</code> 하나의 타입으로 다룬다.

- <strong><code>Number()</code> VS <code>parseInt()</code></strong> :

  - <strong><code>Number()</code></strong> : 전체가 숫자인 문자열에서 소수점까지 모두 형변환

  - <strong><code>parseInt()</code></strong> : (숫자로 시작하는) 문자열에서 정수 부분만 뽑아서 형변환 (소수점 버리기 가능)

- <strong><code>Math.sqrt(n)</code></strong> : n의 제곱근을 반환

- <strong><code>Math.min(a, b, c)</code></strong> : 인자로 들어온 수들 a, b, c중 최솟값을 반환 (인자의 개수는 상관없다.)

- <strong><code>Math.max(a, b, c)</code></strong> : 인자로 들어온 수들 a, b, c중 최댓값을 반환 (인자의 개수는 상관없다.)

- <strong><code>isNaN()</code></strong> : 인자의 자료형이 <code>NaN</code>인지 확인

  - <code>[NaN인 값] === NaN</code>의 결과값은 <code>false</code>이다.

  - 따라서 <code>if ([NaN인 어떤 값] === NaN) { ... }</code>와 같이 자료형을 판단하면, 조건식이 <code>false</code>로 평가되므로 올바른 결과를 얻을 수 없다.

<br/><br/>

## 문자 관련 메소드

- <strong><code>"문자열".match(new RegExp(/^[0-9]/))</code></strong> : "문자열"에서 정규표현식 /^[0-9]/에 매칭되는 항목들을 배열로 반환, 매칭되는 항목이 없으면 null을 반환

- <strong><code>"문자열".toUpperCase()</code></strong> : 영어 "문자열"을 모두 대문자로 변환

- <strong><code>"문자열".toLowerCase()</code></strong> : 영어 "문자열"을 모두 소문자로 변환

- <strong><code>"문자열".substring(n, m)</code></strong> : 문자열 자르기 (index가 n인 위치부터 m인 위치 바로 전까지)

- <strong><code>"문자열".slice(n, m)</code></strong> : 문자열 자르기 (index가 n인 위치부터 m인 위치 바로 전까지) + 음수 인덱스 지원

- <strong><code>"문자열".repeat(n)</code></strong> : 문자열 n회 반복 출력 (ex : "n".repeat(3) => "nnn")

  - n에 소수값이 들어가면 이를 버림하여 정수로 계산된다. (ex: "n".repeat(2.8) => "n".repeat(2) => "nn")

- <strong><code>"문자열".split("문자열")</code></strong> : 문자열을 배열로 나누기 (split 인자의 문자열을 기준으로 분리)

- <strong><code>[배열].join("문자열")</code></strong> : 배열을 문자열로 합치기 (join 인자의 문자열을 배열 각각의 요소 사이에 삽입. default값은 ",")

<br/><br/>

## 배열 관련 메소드

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_array_function.md">여기서 확인</a>

<br/><br/>

## 알고리즘 관련 메소드

- <strong><code>[배열].sort()</code></strong> : 배열을 유니코드 문자 순으로 정렬

  - <strong><code>[배열].sort((a, b) => a - b)</code></strong> : 숫자 배열을 오름차순으로 정렬

  - <strong><code>[배열].sort((a, b) => b - a)</code></strong> : 숫자 배열을 내림차순으로 정렬

<br/><br/>
