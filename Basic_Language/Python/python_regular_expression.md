# Python - 정규표현식 (Regular Expression)

<br/>

참고 자료 : <a href="https://youtu.be/yQ20jZwDjTE?si=iMQWiK98m6y3RUgM">파이썬 코딩 무료 강의 (활용편3) [나도코딩] (유튜브 강의)</a>

<br/>

### 목차

- <a href=""></a>

<br/>

## 정규식 기본

```python
import re

p = re.compile("ca.e")

m = p.match("case")
print(m.group())  # case

n = p.match("caffe")
print(n.group())  # Error 발생
```

- <strong>.</strong> (ca.e) : 하나의 문자를 의미 - care, cafe, case (O) | caffe (X)

- <strong>^</strong> (^de) : 문자열의 시작 - desk, destination (O) | fade (X)

- <strong>$</strong> (se$) : 문자열의 끝 - case, base (O) | face (X)

<br/>

- <strong>match</strong> : 주어진 문자열의 처음부터 일치하는지 확인 (.일 경우, 뒷부분에 다른 것이 있어도 상관 없음)

  ```python
  import re

  p = re.compile("ca.e")

  m = p.match("careless")
  print(m.group())  # careless (Error 발생 X)
  ```

<br/>

- <strong>search</strong> : 주어진 문자열 중에 일치하는 것이 있는지 확인

<br/>
