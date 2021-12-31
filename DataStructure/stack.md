# 순차적 자료구조 : 스택과 큐

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/data_structure_introduction.md">자료구조 소개</a>》 페이지 참고

<br/>

## 스택 (Stack)

* 가장 고전적인 자료구조 중 하나로 거의 모든 애플리케이션 개발에 사용된다.

* 2가지 기본 연산을 제공한다.

    * push(삽입), pop(삭제)

* LIFO : Last In First Out

    * 마지막으로 들어온 요소가 제일 먼저 나간다.

<img src="img/stack1.png">

<br/>

## Stack 구현 (파이썬)

* 파이썬의 대표적인 자료구조인 리스트(List)를 Stack의 자료구조처럼 사용할 수 있다.

    * push 연산 (삽입) : append 함수 이용 

    * pop 연산 (삭제) : pop 함수 이용

* But, 리스트는 다른 강력한 연산들을 제공하기 때문에, 사용 도중 append, pop 외의 다른 함수를 사용하는 실수를 범할 가능성이 높다.

* 따라서, Stack은 Stack 클래스를 따로 만들어서 쓰고, 리스트는 내부에서 값을 저장하는 역할로만 쓴다.

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
    
    def __len(self):  # len()로 호출하면, Stack의 item 수를 반환
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