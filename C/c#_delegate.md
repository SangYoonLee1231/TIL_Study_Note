# C# - Delegate (대리자)

<br/>

> 참고 자료 : <a href="https://www.inflearn.com/course/%EC%9C%A0%EB%8B%88%ED%8B%B0-mmorpg-%EA%B0%9C%EB%B0%9C-part1">[C#과 유니티로 만드는 MMORPG 게임 개발 시리즈] Part1: C# 기초 프로그래밍 입문 (Rookiss님)</a>

<br/><br/>

## Delegate (대리자) 문법이란?

- 함수 자체를 인자로 넘겨주는 하나의 형식이다. (콜백 방식)

- JavaScript의 비동기와 비슷한 개념

- React의 '관심사의 분리'처럼 게임 C# 스크립트에서 UI 로직과 게임 로직을 분리하여 관리하는 것이 좋다.

<br/>

### 예제 코드

```c#
namespace CSharp
{
    class Program
    {
        delegate int OnClicked(); // 하나의 형식
        // 반환값 : int / 입력값 : void

        // 버튼을 눌렀을 때 동작하는 함수
        static void ButtonPressed(OnClicked clickedFunction/* 함수 자체를 인자로 넘겨줌 */)
        {
            // 매개 변수(인자)로 받은 함수를 호출!
            // (콜백 방식)
            clickedFunction();
        }

        static int TestDelegate()
        {
            Console.WriteLine("Hello Delegate");
            return 0;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            ButtonPressed(TestDelegate);
        }
    }
}
```

<br/>

- delegate 객체에 한 개가 아닌 <strong>여러 개의 함수를 동시에</strong> 넘겨줄 수도 있다.

```c#
namespace CSharp
{
    class Program
    {
        delegate int OnClicked(); // 하나의 형식
        // 반환값 : int / 입력값 : void

        // 버튼을 눌렀을 때 동작하는 함수
        static void ButtonPressed(OnClicked clickedFunction/* 함수 자체를 인자로 넘겨줌 */)
        {
            // 매개 변수(인자)로 받은 함수를 호출!
            // (콜백 방식)
            clickedFunction();
        }

        static int TestDelegate()
        {
            Console.WriteLine("Hello Delegate");
            return 0;
        }

        static int TestDelegate2()
        {
            Console.WriteLine("Hello Delegate 2");
            return 0;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            OnClicked clicked = new OnClicked(TestDelegate);
            clicked += TestDelegate2;

            ButtonPressed(clicked);
        }
    }
}
```
