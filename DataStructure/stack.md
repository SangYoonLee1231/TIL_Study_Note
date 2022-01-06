# 순차적 자료구조 : 스택 (Stack)

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 스택 (Stack)

* <strong>가장 고전적인 자료구조</strong> 중 하나로 거의 모든 애플리케이션 개발에 사용된다.

* 1차원의 선형(linear) 자료구조이다.

* 2가지 기본 연산을 제공한다. (다른 추가 연산도 제공)

    * 기본 연산 : <strong>push(삽입), pop(삭제)</strong>

    * 추가 연산 : <strong>top, isEmpty, size(len)</strong>

* <strong>LIFO : Last In First Out</strong>

    * 마지막으로 들어온 요소가 제일 먼저 나간다.

<img src="img/stack1.png">

<br/>

## Stack 구현 (파이썬)

* 파이썬의 대표적인 자료구조인 리스트(List)를 Stack의 자료구조처럼 사용할 수 있다.

    * push 연산 (삽입) : append 함수 이용 

    * pop 연산 (삭제) : pop 함수 이용

* But, <strong>리스트는 다른 강력한 연산들을 제공</strong>하기 때문에, 사용 도중 실수로 append, pop 외의 다른 함수를 사용해 내부값을 참고하고나 변경할 수 있다.

* 따라서, <strong>Stack은 Stack 클래스를 따로 만들어서 쓰고</strong>, 리스트는 내부에서 값을 저장하는 역할로만 쓴다.

<br/>

```python
class Stack:
    # 생성 함수 - 객체 생성시 자동으로 실행
    def __init__(self):
        self.items = []  # 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:  # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:  # IndexError 발생
            print("Stack is Empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")
    
    def __len__(self):  # len()로 호출하면, Stack의 item 수를 반환
        return len(self.items)
```
```python
S = Stack()  # S을 Stack의 객채로 사용

S.push(10)  # S에 10을 push (삽입)  S = [10]
S.push(12)  # S에 12을 push (삽입)  S = [10, 12]

print(S.pop())  # S에서 마지막 값을 pop (삭제하고 return)  ☞  12가 출력  S = [10]
print(S.top())  # S에서 마지막 값을 return (삭제 X)  ☞  10이 출력  S = [10]

print(len(S))  # S의 요소의 개수 출력  ☞  1이 출력  S = [10]
# len(S) == S.__len__()
```

<br/>

## Stack 연산 수행시간

* <strong>push, pop, top, len : O(1)</strong>

    * list에서 요소의 개수를 계속 확인하고 그 값을 이미 저장하고 있기 때문에, len 함수도 O(1)만에 수행된다.

<br/>

## Stack 활용 예제

* <a href="https://www.acmicpc.net/problem/9012" target="_blank">괄호 맞추기 (백준 9012번)</a>

> 1. 오른쪽과 왼쪽 괄호로만 이루어진 문자열을 입력으로 받고 ☞ ex) ()(()))
> 2. '괄호쌍이 모두 맞춰졌는가'에 따라 True/False 결과값을 출력하는 문제 ☞ ex) True

<br/>

* 계산기 문제

> 1. 수식의 문자열을 입력으로 받아서 ☞ ex) "2+3*5"
> 2. 피연산자와 연산자로 문자열을 분리한 후 ☞ ex) '2' '+' '3' '*' '5'
> 3. '연산자의 우선순위'에 따라 차례대로 계산하여 ☞ ex) (2+(3*5))
> 4. 최종 결과값을 출력하는 문제  ☞ ex) 17

<br/>

> 사진 출처 : http://www.incodom.kr/%EC%8A%A4%ED%83%9D